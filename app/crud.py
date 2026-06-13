# =====================================================================
# STEP 4: CRUD QUERY OPERATIONS GUIDE (Raw SQL)
# =====================================================================
# To write database CRUD handlers using raw SQL:
#
# Define Python functions that accept your database connection object (conn) and parameters:
#
# 1. Save Feedback record:
#    - Write a function: save_feedback(conn, name, email, rating, category, feedback)
#    - Create cursor: cursor = conn.cursor()
#    - Execute INSERT SQL using parameterized values to prevent SQL Injection:
#      cursor.execute("INSERT INTO feedbacks (name, email, rating, category, feedback) VALUES (?, ?, ?, ?, ?)", (name, email, rating, category, feedback))
#    - Call conn.commit() to save changes.
#
# 2. Fetch EV Models:
#    - Write a function: fetch_ev_models(conn)
#    - Execute: SELECT * FROM ev_models
#    - Return cursor.fetchall()
#
# 3. Fetch Charging Stations:
#    - Write a function: fetch_stations(conn, city_query=None)
#    - If city_query is provided, execute matching filter query:
#      SELECT * FROM charging_stations WHERE LOWER(city) LIKE ?
#      (Pass f"%{city_query.lower()}%" as the parameter)
#    - Else execute: SELECT * FROM charging_stations
#    - Return cursor.fetchall()
# =====================================================================
