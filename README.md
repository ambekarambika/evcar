# Electric Vehicle Guidance Portal

A  modern  web application designed to educate and guide users on transitioning to Electric Vehicles (EVs). It features interactive client-side calculators, dynamic locator maps, model comparisons, and is fully structured to bind with a FastAPI and raw SQL database backend.

---

## 🌟 Key Features & Pages

1. **Interactive Tools (Client-Side JS)**:
   - **Cost Savings Calculator**: Compare petrol/diesel fuel costs with EV charging rates over a monthly commute.
   - **EV Buying Guide**: A step-by-step guidance questionnaire that recommends suitable EVs.
   - **Compare EVs**: Side-by-side comparison of two models highlighting battery capacity, speed, range, and safety.
   - **Environmental Impact Calculator**: Visualize carbon offsets and dynamically watch trees grow as savings accumulate.
   - **Station Locator & Model Finder**: Dynamic searches that filter records matching input queries instantly.

2. **Educational Guides**:
   - **About EVs**: Explains types of EVs (BEV, PHEV, HEV) with visual flowchart node layouts.
   - **Charging Guide**: Information on charging levels, standards, and safety tips.
   - **Maintenance Checklist**: A structured table outlining upkeep instructions.
   - **Myths vs Facts**: Interactive click-to-slide accordions answering common queries.
   - **Government Incentives**: Subsidies listed nationally national and organized state-wise.

3. **User Dashboard**:
   - An authenticated user space displaying account metadata, custom initials icons, and the user's saved **Favorite EV Models** catalog.
   - Features the integrated **AJAX Feedback form** directly in the dashboard sidebar, allowing logged-in users to submit suggestions seamlessly.

4. **Premium Redesigned Authentication Flow**:
   - Glassmorphic card layouts (`backdrop-filter: blur(20px)`), Outfit google fonts, custom tabler inline form field icons, and animated button transitions for login and registration.

---

## 📂 Project Structure

```text
evcar-updated/
├── app/                  # FastAPI Backend Modules
│   ├── database.py       # SQL Connection settings (MySQL configurations)
│   ├── models.py         # DB Schemas & table scripts (CREATE TABLE & seeds)
│   ├── schemas.py        # Request & Request body validation (Pydantic models)
│   ├── crud.py           # SQL Query Operations templates (INSERT & SELECT)
│   └── auth.py           # JWT Authentication functions, hashing & token verification
├── static/               # Consolidated Static Assets
│   ├── pics/             # EV Model and Station images
│   ├── auth.css          # Premium Auth glassmorphic theme styling sheet
│   └── *.css             # Modular stylesheets for each page
├── templates/            # HTML Views (Jinja-compatible with static fallbacks)
│   ├── dashboard.html    # Authenticated user dashboard & feedback card
│   ├── login.html        # Redesigned Login screen
│   ├── register.html     # Redesigned Sign Up screen
│   └── *.html            # Active web pages containing dynamic script tags
├── main.py               # Application Entry Point, startup hooks, & API routes
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

---

## 🚀 How to Run

### Setup Environment
Create a `.env` file in the root directory specifying your local MySQL connection parameters and security configurations:
```env
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_mysql_password
DB_NAME=ev_database
DB_PORT=3306
JWT_SECRET_KEY=your_secure_jwt_key
```

### Option A: Static View (Offline Preview)
For immediate offline preview, simply double-click any HTML file in the `templates/` folder (e.g., `templates/index.html`). The pages will load with static placeholder data and the client-side JavaScript calculators will run completely offline.

### Option B: Dynamic View (FastAPI + MySQL Database)
1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Start the FastAPI Server**:
   ```bash
   uvicorn main:app --reload
   ```
   *Note: On startup, uvicorn will automatically verify database connectivity, create the tables if they do not exist, and seed initial EV models and charging station data.*

3. **Access the Portal**:
   Open http://127.0.0.1:8000 in your web browser.

---

## 🛠 Project Development Sequence
The EV Guidance Portal was built following this structured development sequence:
1. **Database Schema Design**: Defined SQL tables with relationships and joint constraints (e.g., `users`, `user_favorites`).
2. **Backend Foundation**: Set up MySQL connections, automatic startup hooks, and CRUD helper templates.
3. **Authentication Layer**: Implemented bcrypt password hashing, JWT encoding/decoding claims, and FastAPI security header dependencies.
4. **API Route Endpoints**: Built endpoints for user login, signup, favorite toggles, and feedback insertion.
5. **Static Frontend (HTML & CSS)**: Crafted modular stylesheets and semantic HTML layouts for all 15 views.
6. **Frontend AJAX Integration**: Standardized navigation check scripts to verify local storage tokens, highlight active menu tabs, and map dynamic logout/login routes.
7. **Testing & Optimization**: Verified all flows via automated browser subagents and cleared dev diagnostic utilities.

---

## 🔒 Frontend-Backend Dual Compatibility
The frontend pages use advanced CSS selectors (`.dynamic-only` class) and HTML-commented Jinja blocks (`<!-- {% ... %} -->`) to run seamlessly in both static browser mode (file protocol) and server-rendered dynamic mode.


