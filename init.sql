CREATE TABLE IF NOT EXISTS admin (
    username TEXT,
    password TEXT
);

CREATE TABLE IF NOT EXISTS company (
    id INT,
    company_name TEXT,
    company_api_key TEXT
);

CREATE TABLE IF NOT EXISTS location (
    id INT,
    location_name TEXT,
    location_country TEXT,
    location_city TEXT,
    location_meta TEXT
);

CREATE TABLE IF NOT EXISTS sensor (
    id INT,
    sensor_id INT,
    sensor_name TEXT,
    sensor_category TEXT,
    sensor_meta TEXT,
    sensor_api_key TEXT,
    location_id INT
);