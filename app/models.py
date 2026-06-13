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
    ("BMW iX", "bmw", 121.00, 425, 71.0, "7.2 hrs", 200, "A high-end luxury electric SUV with a futuristic modular front grille and smart cabin tech.", "Fast Charging,Connected Car Technology,Regenerative Braking", "../static/pics/bmwix.jpg", "https://www.bmw-bavariamotors.in/new-cars/bmw-iX")
]

SEED_STATIONS = [
    ("Tata Power EV Station Pune", "Phoenix Marketcity, Viman Nagar, Pune", "pune", 1, "Open 24 Hours", "https://maps.google.com/?q=Phoenix+Marketcity+Pune"),
    ("Ather Grid FC Road", "Fergusson College Road, Pune", "pune", 0, "Open 7 AM - 11 PM", "https://maps.google.com/?q=FC+Road+Pune"),
    ("Zeon Charging Hub Hinjewadi", "Rajiv Gandhi Infotech Park, Hinjewadi, Pune", "pune", 1, "Open 24 Hours", "https://maps.google.com/?q=Hinjewadi+Pune"),
    ("Jio-bp Pulse Bandra", "Bandra Kurla Complex, Mumbai", "mumbai", 1, "Open 24 Hours", "https://maps.google.com/?q=BKC+Mumbai"),
    ("Tata Power Vashi", "Sector 17, Vashi, Navi Mumbai", "mumbai", 1, "Open 24 Hours", "https://maps.google.com/?q=Vashi+Navi+Mumbai"),
    ("Statiq CP Charger", "Connaught Place, New Delhi", "delhi", 1, "Open 24 Hours", "https://maps.google.com/?q=Connaught+Place+Delhi"),
    ("Jio-bp Pulse Aerocity", "Aerocity, New Delhi", "delhi", 1, "Open 24 Hours", "https://maps.google.com/?q=Aerocity+Delhi"),
    ("Ather Grid Whitefield", "Whitefield Main Road, Bengaluru", "bangalore", 0, "Open 6 AM - 11 PM", "https://maps.google.com/?q=Whitefield+Bangalore"),
    ("Tata Power Electronic City", "Electronic City Phase 1, Bengaluru", "bangalore", 1, "Open 24 Hours", "https://maps.google.com/?q=Electronic+City+Bangalore"),
    ("ChargeZone Chennai Hub", "OMR Road, Chennai", "chennai", 1, "Open 24 Hours", "https://maps.google.com/?q=OMR+Chennai"),
    ("Zeon Charging Coimbatore", "Avinashi Road, Coimbatore", "coimbatore", 1, "Open 24 Hours", "https://maps.google.com/?q=Avinashi+Road+Coimbatore"),
    ("Tata Power Hyderabad", "Hitech City, Hyderabad", "hyderabad", 1, "Open 24 Hours", "https://maps.google.com/?q=Hitech+City+Hyderabad"),
    ("Jio-bp Pulse Ahmedabad", "SG Highway, Ahmedabad", "ahmedabad", 1, "Open 24 Hours", "https://maps.google.com/?q=SG+Highway+Ahmedabad"),
    ("ChargeZone Jaipur", "Malviya Nagar, Jaipur", "jaipur", 0, "Open 8 AM - 10 PM", "https://maps.google.com/?q=Malviya+Nagar+Jaipur"),
    ("EVRE Charging Station Goa", "Panjim, Goa", "goa", 1, "Open 24 Hours", "https://maps.google.com/?q=Panjim+Goa")
]
