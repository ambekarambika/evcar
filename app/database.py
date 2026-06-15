import os
import pymysql
from dotenv import load_dotenv

# Load local environment variables from .env file
load_dotenv()

# =====================================================================
# DATABASE CONNECTION CONFIGURATION (MySQL)
# =====================================================================
# Connection parameters are loaded securely from your local .env file.
# Default fallback values are specified here:
DB_HOST = os.getenv("DB_HOST", "")
DB_USER = os.getenv("DB_USER", "")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")  # Enter password in your local .env file
DB_NAME = os.getenv("DB_NAME", "")

db_port_env = os.getenv("DB_PORT", "")
DB_PORT = int(db_port_env) if db_port_env.isdigit() else 3306
print("DB_HOST =", DB_HOST)
print("DB_USER =", DB_USER)
print("DB_NAME =", DB_NAME)
print("DB_PORT =", DB_PORT)

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
        port=DB_PORT,
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
        password=DB_PASSWORD,
        port=DB_PORT
    )
    try:
        with conn.cursor() as cursor:
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME};")
        conn.commit()
    finally:
        conn.close()
