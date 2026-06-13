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
