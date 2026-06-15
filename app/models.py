# =====================================================================
# SCHEMA DEFINITION & SEED DATA (MySQL)
# =====================================================================

# 1. Feedbacks table schema
CREATE_FEEDBACKS_TABLE = """
CREATE TABLE IF NOT EXISTS feedbacks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    rating INT NOT NULL,
    category VARCHAR(100) NOT NULL,
    feedback TEXT NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
"""

# 2. EV Models table schema
CREATE_MODELS_TABLE = """
CREATE TABLE IF NOT EXISTS ev_models (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    brand VARCHAR(100) NOT NULL,
    price DOUBLE NOT NULL,
    `range` INT NOT NULL,
    battery DOUBLE NOT NULL,
    charging_time VARCHAR(100) NOT NULL,
    top_speed INT NOT NULL,
    description TEXT,
    features VARCHAR(255),
    image_path VARCHAR(255) NOT NULL,
    learn_more_link VARCHAR(255)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
"""

# 3. Charging Stations table schema
CREATE_STATIONS_TABLE = """
CREATE TABLE IF NOT EXISTS charging_stations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    address VARCHAR(255) NOT NULL,
    city VARCHAR(100) NOT NULL,
    is_fast TINYINT DEFAULT 0,
    open_hours VARCHAR(100),
    directions_link VARCHAR(255)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
"""

# 4. Users table schema
CREATE_USERS_TABLE = """
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) NOT NULL UNIQUE,
    email VARCHAR(255) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
"""

# 5. User Favorites table schema
CREATE_FAVORITES_TABLE = """
CREATE TABLE IF NOT EXISTS user_favorites (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    model_id INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (model_id) REFERENCES ev_models(id) ON DELETE CASCADE,
    UNIQUE KEY unique_user_model (user_id, model_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
"""

# Seeding Data Datasets
SEED_MODELS = [
    ("Tata Nexon EV", "tata", 14.49, 489, 46.0, "6 hrs", 150, "A compact and extremely popular electric SUV that defines Indian electric mobility.", "Fast Charging,Connected Car Technology,Regenerative Braking", "../static/model1.jpg", "https://ev.tatamotors.com/nexon/ev.html"),
    ("Tata Punch EV", "tata", 10.99, 421, 35.0, "5 hrs", 140, "A stylish, compact SUV built on the new advanced acti.ev platform for pure electric convenience.", "Fast Charging,Connected Car Technology,Regenerative Braking", "../static/pics/punch.webp", "https://ev.tatamotors.com/punch/ev.html"),
    ("Tata Tiago EV", "tata", 7.99, 250, 19.2, "4 hrs", 120, "An affordable and compact electric hatchback designed for daily city driving.", "Fast Charging,Connected Car Technology,Regenerative Braking", "../static/pics/tiago.webp", "https://ev.tatamotors.com/tiago/ev.html"),
    ("Tesla Model 3", "tesla", 39.90, 513, 60.0, "6.5 hrs", 201, "A high-performance luxury electric sedan with class-leading drag and smart automation.", "Fast Charging,Autopilot driver-assist,Regenerative Braking", "../static/pics/model3.webp", "https://www.tesla.com/model3"),
    ("Tesla Model Y", "tesla", 49.90, 533, 75.0, "7 hrs", 217, "A versatile and spacious electric crossover utility vehicle with dual electric motors.", "Fast Charging,Connected Car Technology,Regenerative Braking", "../static/pics/modely.avif", "https://www.tesla.com/modely"),
    ("Hyundai Ioniq 5", "hyundai", 46.05, 631, 72.6, "6.8 hrs", 185, "A retro-futuristic SUV styled with geometric lighting patterns and V2L charging power.", "Fast Charging,Connected Car Technology,Regenerative Braking", "../static/pics/hondai.webp", "https://ioniq5.hyundai.co.in/"),
    ("Hyundai Kona Electric", "hyundai", 23.84, 452, 39.2, "6 hrs", 167, "A reliable and sporty electric utility vehicle built with a sleek aerodynamic nose.", "Fast Charging,Connected Car Technology,Regenerative Braking", "../static/pics/kona.jpg", "https://www.hyundai.com/in/en/find-a-car/kona-electric/highlights"),
    ("BMW i4", "bmw", 72.50, 590, 80.7, "8.5 hrs", 190, "A dynamic, stylish, and high-performance all-electric gran coupe with classical handling.", "Fast Charging,Connected Car Technology,Regenerative Braking", "../static/pics/bmwi4.jpg", "https://www.bmw-bavariamotors.in/new-cars/i-series-i4"),
    ("BMW iX", "bmw", 121.00, 425, 71.0, "7.2 hrs", 200, "A high-end luxury electric SUV with a futuristic modular front grille and smart cabin tech.", "Fast Charging,Connected Car Technology,Regenerative Braking", "../static/pics/bmwix.jpg", "https://www.bmw-bavariamotors.in/new-cars/bmw-iX"),
    ("Ola S1 Pro", "ola", 1.40, 181, 4.0, "6.5 hrs", 116, "A high-tech electric scooter with smart connectivity, cruise control, and class-leading performance.", "Smart touch console,Music & navigation,Fast charging support", "../static/pics/ola_s1_pro.jpg", "https://www.olaelectric.com/s1-pro"),
    ("Ather 450X", "ather", 1.38, 150, 3.7, "5.7 hrs", 90, "A premium, sporty electric scooter with a tough aluminum frame and smart Google Maps integration.", "TrueRange technology,Google Maps navigation,AutoHold assist", "../static/pics/ather_450x.jpg", "https://www.atherenergy.com/"),
    ("TVS iQube", "tvs", 1.17, 145, 3.4, "4.5 hrs", 78, "A reliable family electric scooter with silent drive, smooth handling, and premium build quality.", "SmartXonnect display,Regenerative braking,Silent hub motor", "../static/pics/tvs_iqube.jpg", "https://www.tvsmotor.com/iqube"),
    ("Bajaj Chetak Electric", "bajaj", 1.15, 113, 2.9, "4.8 hrs", 73, "A classic metal-bodied electric scooter blending retro design with modern battery technology.", "Full metal body,IP67 water resistance,Retro LED headlamp", "../static/pics/chetak.jpg", "https://www.chetak.com/"),
    ("Hero Vida V1 Pro", "hero", 1.26, 165, 3.9, "5.9 hrs", 80, "A highly customizable electric scooter featuring dual removable batteries for easy home charging.", "Dual removable batteries,Custom riding modes,Fast charge capable", "../static/pics/vida_v1.jpg", "https://www.vidaworld.com/"),
    ("Ultraviolette F77", "ultraviolette", 3.80, 307, 10.3, "5 hrs", 152, "A high-performance electric sports motorcycle with aggressive styling and fighter jet inspired tech.", "Aero winglets,Advanced battery analytics,LTE connectivity", "../static/pics/ultraviolette_f77.jpg", "https://www.ultraviolette.com/"),
    ("Revolt RV400", "revolt", 1.43, 150, 3.2, "4.5 hrs", 85, "A popular electric street bike featuring artificial exhaust sound profiles and swappable battery access.", "Exhaust sound simulator,Swappable battery network,MyRevolt App support", "../static/pics/revolt_rv400.jpg", "https://www.revoltmotors.com/"),
    ("Oben Rorr", "oben", 1.49, 187, 4.4, "2 hrs", 100, "A stylish electric commuter motorcycle with high ground clearance and ultra-fast charging capabilities.", "LFP battery chemistry,0-40 km/h in 3s,Fast charging support", "../static/pics/oben_rorr.jpg", "https://www.obenelectric.com/"),
    ("Tork Kratos R", "tork", 1.67, 180, 4.0, "4.5 hrs", 105, "An indigenous electric motorcycle built with an axial flux motor and robust trellis frame chassis.", "Axial Flux motor,Trellis frame,Geofencing and telemetry", "../static/pics/kratosr.jpg", "https://www.torkmotors.com/")
]

SEED_STATIONS = [
    ("Tata Power EV Station Pune", "Phoenix Marketcity, Viman Nagar, Pune", "pune", 1, "Open 24 Hours", "https://maps.google.com/?q=Phoenix+Marketcity+Pune"),
    ("Ather Grid FC Road", "Fergusson College Road, Pune", "pune", 0, "Open 7 AM - 11 PM", "https://maps.google.com/?q=FC+Road+Pune"),
    ("Zeon Charging Hub Hinjewadi", "Rajiv Gandhi Infotech Park, Hinjewadi, Pune", "pune", 1, "Open 24 Hours", "https://maps.google.com/?q=Hinjewadi+Pune"),
    ("Jio-bp Pulse Bandra", "Bandra Kurla Complex, Mumbai", "mumbai", 1, "Open 24 Hours", "https://maps.google.com/?q=BKC+Mumbai"),
    ("Tata Power Vashi", "Sector 17, Vashi, Navi Mumbai", "mumbai", 1, "Open 24 Hours", "https://maps.google.com/?q=Vashi+Navi+Mumbai"),
    ("Statiq CP Charger", "Connaught Place, New Delhi", "delhi", 1, "Open 24 Hours", "https://maps.google.com/?q=Connaught+Place+Delhi"),
    ("Jio-bp Pulse Aerocity", "Aerocity, New Delhi", "delhi", 1, "Open 24 Hours", "https://maps.google.com/?q=Aerocity+Delhi"),
    ("Ather Grid Whitefield", "Whitefield Main Road, Bengaluru", "bengalore", 0, "Open 6 AM - 11 PM", "https://maps.google.com/?q=Whitefield+Bangalore"),
    ("Tata Power Electronic City", "Electronic City Phase 1, Bengaluru", "bengalore", 1, "Open 24 Hours", "https://maps.google.com/?q=Electronic+City+Bangalore"),
    ("ChargeZone Chennai Hub", "OMR Road, Chennai", "chennai", 1, "Open 24 Hours", "https://maps.google.com/?q=OMR+Chennai"),
    ("Zeon Charging Coimbatore", "Avinashi Road, Coimbatore", "coimbatore", 1, "Open 24 Hours", "https://maps.google.com/?q=Avinashi+Road+Coimbatore"),
    ("Tata Power Hyderabad", "Hitech City, Hyderabad", "hyderabad", 1, "Open 24 Hours", "https://maps.google.com/?q=Hitech+City+Hyderabad"),
    ("Jio-bp Pulse Ahmedabad", "SG Highway, Ahmedabad", "ahmedabad", 1, "Open 24 Hours", "https://maps.google.com/?q=SG+Highway+Ahmedabad"),
    ("ChargeZone Jaipur", "Malviya Nagar, Jaipur", "jaipur", 0, "Open 8 AM - 10 PM", "https://maps.google.com/?q=Malviya+Nagar+Jaipur"),
    ("EVRE Charging Station Goa", "Panjim, Goa", "goa", 1, "Open 24 Hours", "https://maps.google.com/?q=Panjim+Goa")
]
