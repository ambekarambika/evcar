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
   - **Government Incentives**: Subsidies listed nationally and organized state-wise.

3. **User Feedback Form**:
   - Clean feedback interface including star-ratings and email validation, connected via API POST requests.

---

## 📂 Project Structure

```text
evcar-updated/
├── app/                  # FastAPI Backend Modules (Commented Guidelines)
│   ├── database.py       # SQL Connection settings (sqlite3 configuration)
│   ├── models.py         # DB Schemas & table scripts (CREATE TABLE definitions)
│   ├── schemas.py        # API Request validation schemas (Pydantic model)
│   └── crud.py           # SQL Query Operations templates (INSERT & SELECT)
├── static/               # Consolidated Static Assets
│   ├── pics/             # EV Model and Station images
│   └── *.css             # Modular stylesheets for each page
├── templates/            # HTML Views (Jinja-compatible with static fallbacks)
│   └── *.html            # 13 web pages containing commented-out Jinja loops
├── main.py               # Application Entry Point & routing guidelines
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

---

## 🚀 How to Run

### Option A: Static View (Offline Preview)
For immediate offline preview, simply double-click any HTML file in the `templates/` folder (e.g., `templates/index.html`). The pages will load with static placeholder data and the client-side JavaScript calculators will run completely offline.

### Option B: Dynamic View (FastAPI + SQL Database)
Once you implement the database backend functions described in the files under the `app/` folder, run the following:

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Start the FastAPI Server**:
   ```bash
   uvicorn main:app --reload
   ```

3. **Access the Portal**:
   Open localhost in your web browser.

---

## 🔒 Frontend-Backend Dual Compatibility
The frontend pages use advanced CSS selectors (`.dynamic-only` class) and HTML-commented Jinja blocks (`<!-- {% ... %} -->`) to run seamlessly in both static browser mode (file protocol) and server-rendered dynamic mode.
