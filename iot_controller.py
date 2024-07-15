from db import get_db

# Insert a new admin record
def create_admin(username, password):
    db = get_db()
    cursor = db.cursor()
    query = "INSERT INTO admin (username, password) VALUES (?, ?)"
    cursor.execute(query, (username, password))
    db.commit()

# Retrieve all admin records
def read_admins():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT * FROM admin"
    cursor.execute(query)
    admins = cursor.fetchall()
    return admins

# Update an admin record
def update_admin(username, new_password):
    db = get_db()
    cursor = db.cursor()
    query = "UPDATE admin SET password = ? WHERE username = ?"
    cursor.execute(query, (new_password, username))
    db.commit()

# Delete an admin record
def delete_admin(username):
    db = get_db()
    cursor = db.cursor()
    query = "DELETE FROM admin WHERE username = ?"
    cursor.execute(query, (username,))
    db.commit()

# Insert a new company record
def create_company(id, company_name, company_api_key):
    db = get_db()
    cursor = db.cursor()
    query = "INSERT INTO company (id, company_name, company_api_key) VALUES (?, ?, ?)"
    cursor.execute(query, (id, company_name, company_api_key))
    db.commit()

# Retrieve all company records
def read_companies():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT * FROM company"
    cursor.execute(query)
    companies = cursor.fetchall()
    return companies

# Update a company record
def update_company(id, new_company_name, new_company_api_key):
    db = get_db()
    cursor = db.cursor()
    query = "UPDATE company SET company_name = ?, company_api_key = ? WHERE id = ?"
    cursor.execute(query, (new_company_name, new_company_api_key, id))
    db.commit()

# Delete a company record
def delete_company(id):
    db = get_db()
    cursor = db.cursor()
    query = "DELETE FROM company WHERE id = ?"
    cursor.execute(query, (id,))
    db.commit()

# Insert a new location record
def create_location(id, location_name, location_country, location_city, location_meta):
    db = get_db()
    cursor = db.cursor()
    query = "INSERT INTO location (id, location_name, location_country, location_city, location_meta) VALUES (?, ?, ?, ?, ?)"
    cursor.execute(query, (id, location_name, location_country, location_city, location_meta))
    db.commit()

# Retrieve all location records
def read_locations():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT * FROM location"
    cursor.execute(query)
    locations = cursor.fetchall()
    return locations

# Update a location record
def update_location(id, new_location_name, new_location_country, new_location_city, new_location_meta):
    db = get_db()
    cursor = db.cursor()
    query = "UPDATE location SET location_name = ?, location_country = ?, location_city = ?, location_meta = ? WHERE id = ?"
    cursor.execute(query, (new_location_name, new_location_country, new_location_city, new_location_meta, id))
    db.commit()

# Delete a location record
def delete_location(id):
    db = get_db()
    cursor = db.cursor()
    query = "DELETE FROM location WHERE id = ?"
    cursor.execute(query, (id,))
    db.commit()

# Insert a new sensor record
def create_sensor(id, sensor_id, sensor_name, sensor_category, sensor_meta, sensor_api_key, location_id):
    db = get_db()
    cursor = db.cursor()
    query = "INSERT INTO sensor (id, sensor_id, sensor_name, sensor_category, sensor_meta, sensor_api_key, location_id) VALUES (?, ?, ?, ?, ?, ?, ?)"
    cursor.execute(query, (id, sensor_id, sensor_name, sensor_category, sensor_meta, sensor_api_key, location_id))
    db.commit()

# Retrieve all sensor records
def read_sensors():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT * FROM sensor"
    cursor.execute(query)
    sensors = cursor.fetchall()
    return sensors

# Update a sensor record
def update_sensor(id, new_sensor_id, new_sensor_name, new_sensor_category, new_sensor_meta, new_sensor_api_key, new_location_id):
    db = get_db()
    cursor = db.cursor()
    query = "UPDATE sensor SET sensor_id = ?, sensor_name = ?, sensor_category = ?, sensor_meta = ?, sensor_api_key = ?, location_id = ? WHERE id = ?"
    cursor.execute(query, (new_sensor_id, new_sensor_name, new_sensor_category, new_sensor_meta, new_sensor_api_key, new_location_id, id))
    db.commit()

# Delete a sensor record
def delete_sensor(id):
    db = get_db()
    cursor = db.cursor()
    query = "DELETE FROM sensor WHERE id = ?"
    cursor.execute(query, (id,))
    db.commit()


