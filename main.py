from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app import database, models, schemas, crud

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
            conn.commit()

            # Seed default models if table is empty
            with conn.cursor() as cursor:
                cursor.execute("SELECT COUNT(*) FROM ev_models")
                if cursor.fetchone()["COUNT(*)"] == 0:
                    query = """
                    INSERT INTO ev_models (name, brand, price, `range`, battery, charging_time, top_speed, description, features, image_path, learn_more_link)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                    """
                    cursor.executemany(query, models.SEED_MODELS)
                    conn.commit()

            # Seed default charging stations if table is empty
            with conn.cursor() as cursor:
                cursor.execute("SELECT COUNT(*) FROM charging_stations")
                if cursor.fetchone()["COUNT(*)"] == 0:
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

@app.get("/{page}.html", response_class=HTMLResponse)
async def read_page(request: Request, page: str):
    """
    Catch-all endpoint for general static pages.
    """
    try:
        return templates.TemplateResponse(f"{page}.html", {"request": request})
    except Exception:
        raise HTTPException(status_code=404, detail="Page not found")
