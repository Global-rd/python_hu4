import sqlite3
from datetime import datetime

class SearchLogger:
    ''' Saves every search into an SQLite database. '''

    def __init__(self, db_name="weather_logs.db"):
        self.db_name = db_name
        self._create_table()

    def _create_table(self):
        conn = sqlite3.connect(self.db_name)
        cur = conn.cursor()
        cur.execute('''
            CREATE TABLE IF NOT EXISTS logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                city TEXT,
                temperature REAL,
                humidity REAL,
                windspeed REAL,
                timestamp TEXT
            )
        ''')
        conn.commit()
        conn.close()

    def log(self, city, temperature, humidity, windspeed):
        conn = sqlite3.connect(self.db_name)
        cur = conn.cursor()
        cur.execute('''
            INSERT INTO logs (city, temperature, humidity, windspeed, timestamp)
            VALUES (?, ?, ?, ?, ?)
        ''', (city, temperature, humidity, windspeed, datetime.now().isoformat()))
        conn.commit()
        conn.close()
