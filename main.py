from fastapi import FastAPI, Request, HTTPException, Depends
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app import database, models, schemas, crud
from app.auth import hash_password, verify_password, create_access_token, get_current_user_id

app = FastAPI(title="EV Guidance Portal")

# Mount static files folder
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates setup
templates = Jinja2Templates(directory="templates")

@app.on_event("startup")
async def startup_event():
    """
    Startup hook to initialize MySQL database database structure and seed data.
    """
    try:
        # Create database if not exists
        database.initialize_database_if_needed()
        
        # Connect to target database and construct tables
        conn = database.get_db_connection()
        try:
            with conn.cursor() as cursor:
                cursor.execute(models.CREATE_FEEDBACKS_TABLE)
                cursor.execute(models.CREATE_MODELS_TABLE)
                cursor.execute(models.CREATE_STATIONS_TABLE)
                cursor.execute(models.CREATE_USERS_TABLE)
                cursor.execute(models.CREATE_FAVORITES_TABLE)
            conn.commit()

            # Seed default models if table is empty
            with conn.cursor() as cursor:
                cursor.execute("SELECT COUNT(*) AS count FROM ev_models")
                if cursor.fetchone()["count"] == 0:
                    query = """
                    INSERT INTO ev_models (name, brand, price, `range`, battery, charging_time, top_speed, description, features, image_path, learn_more_link)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                    """
                    cursor.executemany(query, models.SEED_MODELS)
                    conn.commit()

            # Seed default charging stations if table is empty
            with conn.cursor() as cursor:
                cursor.execute("SELECT COUNT(*) AS count FROM charging_stations")
                if cursor.fetchone()["count"] == 0:
                    query = """
                    INSERT INTO charging_stations (name, address, city, is_fast, open_hours, directions_link)
                    VALUES (%s, %s, %s, %s, %s, %s)
                    """
                    cursor.executemany(query, models.SEED_STATIONS)
                    conn.commit()
        finally:
            conn.close()
    except Exception as e:
        print(f"WARNING: Failed to initialize database: {e}")
        print("Please run 'python setup_db.py' manually to diagnose and setup database.")

@app.get("/", response_class=HTMLResponse)
async def read_index(request: Request):
    """
    Home page rendering endpoint.
    """
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/models.html", response_class=HTMLResponse)
async def read_models(request: Request):
    """
    EV Models dynamic page rendering endpoint.
    """
    try:
        conn = database.get_db_connection()
        try:
            db_models = crud.fetch_ev_models(conn)
        finally:
            conn.close()
    except Exception as e:
        print(f"Error loading models from DB: {e}")
        db_models = []
    
    return templates.TemplateResponse("models.html", {"request": request, "models": db_models})

@app.get("/stations.html", response_class=HTMLResponse)
async def read_stations(request: Request, city: str = None):
    """
    Charging Stations locator rendering endpoint with optional query search filters.
    """
    try:
        conn = database.get_db_connection()
        try:
            db_stations = crud.fetch_stations(conn, city)
        finally:
            conn.close()
    except Exception as e:
        print(f"Error loading stations from DB: {e}")
        db_stations = []
        
    return templates.TemplateResponse("stations.html", {"request": request, "stations": db_stations})

@app.post("/submit_feedback")
async def submit_feedback(submission: schemas.FeedbackSubmission):
    """
    Feedback submission receiver endpoint.
    """
    try:
        conn = database.get_db_connection()
        try:
            crud.save_feedback(
                conn, 
                submission.name, 
                submission.email, 
                submission.rating, 
                submission.category, 
                submission.feedback
            )
        finally:
            conn.close()
        return JSONResponse(content={"status": "success", "message": "Feedback submitted successfully!"})
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"status": "error", "message": f"Failed to submit feedback: {e}"}
        )

@app.post("/register")
async def api_register(payload: schemas.UserRegister):
    try:
        conn = database.get_db_connection()
        try:
            # Check if username or email already exists
            existing_user = crud.get_user_by_username(conn, payload.username)
            if existing_user:
                raise HTTPException(status_code=400, detail="Username already registered")
            
            existing_email = crud.get_user_by_email(conn, payload.email)
            if existing_email:
                raise HTTPException(status_code=400, detail="Email already registered")
            
            hashed_pass = hash_password(payload.password)
            crud.create_user(conn, payload.username, payload.email, hashed_pass)
            return {"status": "success", "message": "User registered successfully!"}
        finally:
            conn.close()
    except HTTPException as he:
        raise he
    except Exception as e:
        return JSONResponse(status_code=500, content={"status": "error", "message": f"Registration failed: {e}"})

@app.get("/{page}.html", response_class=HTMLResponse)
async def read_page(request: Request, page: str):
    """
    Catch-all endpoint for general static pages.
    """
    try:
        return templates.TemplateResponse(f"{page}.html", {"request": request})
    except Exception:
        raise HTTPException(status_code=404, detail="Page not found")


@app.post("/login")
async def api_login(payload: schemas.UserLogin):
    try:
        conn = database.get_db_connection()
        try:
            user = crud.get_user_by_username(conn, payload.username)
            if not user or not verify_password(payload.password, user["password_hash"]):
                raise HTTPException(status_code=401, detail="Invalid username or password")
            
            token = create_access_token(data={"user_id": user["id"], "username": user["username"]})
            return {"status": "success", "access_token": token, "username": user["username"]}
        finally:
            conn.close()
    except HTTPException as he:
        raise he
    except Exception as e:
        return JSONResponse(status_code=500, content={"status": "error", "message": f"Login failed: {e}"})

@app.post("/favorites/toggle")
async def api_toggle_favorite(payload: schemas.FavoriteToggle, user_id: int = Depends(get_current_user_id)):
    try:
        conn = database.get_db_connection()
        try:
            # First, verify if model_id is valid
            with conn.cursor() as cursor:
                cursor.execute("SELECT 1 FROM ev_models WHERE id = %s", (payload.model_id,))
                if not cursor.fetchone():
                    raise HTTPException(status_code=404, detail="EV Model not found")
            
            favorited = crud.is_favorite(conn, user_id, payload.model_id)
            if favorited:
                crud.remove_favorite(conn, user_id, payload.model_id)
                action = "removed"
            else:
                crud.add_favorite(conn, user_id, payload.model_id)
                action = "added"
            return {"status": "success", "action": action, "message": f"Model {action} successfully!"}
        finally:
            conn.close()
    except HTTPException as he:
        raise he
    except Exception as e:
        return JSONResponse(status_code=500, content={"status": "error", "message": f"Favorite toggle failed: {e}"})

@app.get("/favorites")
async def api_get_favorites(user_id: int = Depends(get_current_user_id)):
    try:
        conn = database.get_db_connection()
        try:
            favorites = crud.fetch_user_favorites(conn, user_id)
            return {"status": "success", "favorites": favorites}
        finally:
            conn.close()
    except Exception as e:
        return JSONResponse(status_code=500, content={"status": "error", "message": f"Failed to fetch favorites: {e}"})

@app.get("/me")
async def api_get_me(user_id: int = Depends(get_current_user_id)):
    try:
        conn = database.get_db_connection()
        try:
            with conn.cursor() as cursor:
                cursor.execute("SELECT id, username, email FROM users WHERE id = %s", (user_id,))
                user = cursor.fetchone()
            if not user:
                raise HTTPException(status_code=404, detail="User not found")
            return {"status": "success", "user": user}
        finally:
            conn.close()
    except HTTPException as he:
        raise he
    except Exception as e:
        return JSONResponse(status_code=500, content={"status": "error", "message": f"Failed to fetch profile: {e}"})
