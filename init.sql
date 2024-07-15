CREATE TABLE IF NOT EXISTS admin (
    username TEXT,
    password TEXT
);

CREATE TABLE IF NOT EXISTS company (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_name TEXT,
    company_api_key TEXT
);

CREATE TABLE IF NOT EXISTS location (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    location_name TEXT,
    location_country TEXT,
    location_city TEXT,
    location_meta TEXT
);

CREATE TABLE IF NOT EXISTS sensor (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sensor_id INT,
    sensor_name TEXT,
    sensor_category TEXT,
    sensor_meta TEXT,
    sensor_api_key TEXT,
    location_id INT
);

INSERT INTO admin (username, password) VALUES ('admin1', 'password1');