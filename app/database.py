import pymysql

# =====================================================================
# DATABASE CONNECTION CONFIGURATION (MySQL)
# =====================================================================
# Change these values to match your local MySQL configuration:
DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "root"  # Enter your local MySQL password here
DB_NAME = "ev_database"

def get_db_connection():
    """
    Establishes a connection to the MySQL database.
    Configures DictCursor so columns can be fetched dynamically by name.
    """
    return pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
        cursorclass=pymysql.cursors.DictCursor
    )

def initialize_database_if_needed():
    """
    Establishes a connection to the MySQL server and creates the
    database automatically if it does not exist.
    """
    conn = pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD
    )
    try:
        with conn.cursor() as cursor:
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME};")
        conn.commit()
    finally:
        conn.close()
