# =====================================================================
# CRUD QUERY OPERATIONS (MySQL)
# =====================================================================

def save_feedback(conn, name, email, rating, category, feedback):
    """
    Saves a user feedback record in the database feedbacks table.
    """
    with conn.cursor() as cursor:
        query = """
        INSERT INTO feedbacks (name, email, rating, category, feedback)
        VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(query, (name, email, rating, category, feedback))
    conn.commit()

def fetch_ev_models(conn):
    """
    Fetches all electric vehicle models from the database ev_models table.
    """
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM ev_models")
        return cursor.fetchall()

def fetch_stations(conn, city_query=None):
    """
    Fetches charging station locations, optionally filtering by city pattern match.
    """
    with conn.cursor() as cursor:
        if city_query:
            query = "SELECT * FROM charging_stations WHERE LOWER(city) LIKE %s"
            cursor.execute(query, (f"%{city_query.lower()}%",))
        else:
            cursor.execute("SELECT * FROM charging_stations")
        return cursor.fetchall()

def create_user(conn, username, email, hashed_password):
    """
    Saves a new user record in the users table.
    """
    with conn.cursor() as cursor:
        query = """
        INSERT INTO users (username, email, password_hash)
        VALUES (%s, %s, %s)
        """
        cursor.execute(query, (username, email, hashed_password))
    conn.commit()

def get_user_by_username(conn, username):
    """
    Retrieves user record matching username.
    """
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        return cursor.fetchone()

def get_user_by_email(conn, email):
    """
    Retrieves user record matching email.
    """
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        return cursor.fetchone()

def add_favorite(conn, user_id, model_id):
    """
    Registers a new favorite EV mapping.
    """
    with conn.cursor() as cursor:
        query = """
        INSERT IGNORE INTO user_favorites (user_id, model_id)
        VALUES (%s, %s)
        """
        cursor.execute(query, (user_id, model_id))
    conn.commit()

def remove_favorite(conn, user_id, model_id):
    """
    Removes a favorite EV mapping.
    """
    with conn.cursor() as cursor:
        query = "DELETE FROM user_favorites WHERE user_id = %s AND model_id = %s"
        cursor.execute(query, (user_id, model_id))
    conn.commit()

def is_favorite(conn, user_id, model_id):
    """
    Checks if an EV is favorited by the user.
    """
    with conn.cursor() as cursor:
        query = "SELECT 1 FROM user_favorites WHERE user_id = %s AND model_id = %s"
        cursor.execute(query, (user_id, model_id))
        return cursor.fetchone() is not None

def fetch_user_favorites(conn, user_id):
    """
    Fetches all EV models favorited by the user.
    """
    with conn.cursor() as cursor:
        query = """
        SELECT m.* FROM ev_models m
        JOIN user_favorites f ON m.id = f.model_id
        WHERE f.user_id = %s
        """
        cursor.execute(query, (user_id,))
        return cursor.fetchall()

