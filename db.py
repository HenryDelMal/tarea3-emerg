import sqlite3
DATABASE_NAME = "iot.db"

def get_db():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn

def create_tables():
    with open('init.sql', 'r') as file:
        tables = file.read().split(';')
    db = get_db()
    cursor = db.cursor()
    for table in tables:
        cursor.execute(table)
