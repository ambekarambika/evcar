# =====================================================================
# STEP 1: DATABASE CONNECTION GUIDE (Raw SQL)
# =====================================================================
# To implement database connectivity in this file:
# 
# 1. Import the sqlite3 library:
#    import sqlite3
#
# 2. Define your database file name:
#    DATABASE_FILE = "ev_database.db"
#
# 3. Create a connection function:
#    - Open a connection to your SQLite database file using:
#      sqlite3.connect(DATABASE_FILE)
#    - Configure row_factory so that column values can be fetched by name:
#      conn.row_factory = sqlite3.Row
#    - Return the connection object.
#
# 4. Call this connection function inside your FastAPI endpoints in main.py,
#    always ensuring you close the connection at the end of each request.
# =====================================================================
