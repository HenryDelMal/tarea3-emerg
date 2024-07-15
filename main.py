import sqlite3
from flask import Flask
DATABASE_NAME = "iot.db"

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(port=3000)