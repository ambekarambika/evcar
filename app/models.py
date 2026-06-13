# =====================================================================
# STEP 2: SCHEMA DEFINITION & INITIALIZATION GUIDE
# =====================================================================
# To define your database schemas and run initialization scripts:
#
# Define multi-line string variables containing 'CREATE TABLE IF NOT EXISTS' SQL statements:
#
# 1. Feedbacks table schema:
#    - Table name: feedbacks
#    - Columns: 
#      - id: INTEGER PRIMARY KEY AUTOINCREMENT
#      - name: TEXT NOT NULL
#      - email: TEXT NOT NULL
#      - rating: INTEGER NOT NULL
#      - category: TEXT NOT NULL
#      - feedback: TEXT NOT NULL
#
# 2. EV Models table schema:
#    - Table name: ev_models
#    - Columns:
#      - id: INTEGER PRIMARY KEY AUTOINCREMENT
#      - name: TEXT NOT NULL
#      - brand: TEXT NOT NULL
#      - price: REAL NOT NULL (stores price in Lakhs)
#      - range: INTEGER NOT NULL
#      - battery: REAL NOT NULL
#      - charging_time: TEXT NOT NULL
#      - top_speed: INTEGER NOT NULL
#      - description: TEXT
#      - features: TEXT (comma-separated list, e.g. "Fast Charging,Regenerative Braking")
#      - image_path: TEXT NOT NULL
#      - learn_more_link: TEXT
#
# 3. Charging Stations table schema:
#    - Table name: charging_stations
#    - Columns:
#      - id: INTEGER PRIMARY KEY AUTOINCREMENT
#      - name: TEXT NOT NULL
#      - address: TEXT NOT NULL
#      - city: TEXT NOT NULL
#      - is_fast: INTEGER DEFAULT 0 (1 = Fast Charger, 0 = Level 2 Charger)
#      - open_hours: TEXT
#      - directions_link: TEXT
#
# Seeding Guidelines:
# Define list templates containing default vehicle data and charging stations 
# (e.g. Tata Nexon EV, Pune chargers) which you can execute using conn.executemany() 
# on app startup if the tables are empty.
# =====================================================================
