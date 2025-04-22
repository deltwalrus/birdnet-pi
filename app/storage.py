import sqlite3
import os

DB_PATH = os.path.expanduser("~/birdnet-pi/data/detections.db")

def init_db():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS detections (
                id INTEGER PRIMARY KEY,
                timestamp TEXT,
                species TEXT,
                confidence REAL,
                filepath TEXT
            )
        """)

def save_detections(timestamp, filepath, results):
    with sqlite3.connect(DB_PATH) as conn:
        for row in results:
            conn.execute("""
                INSERT INTO detections (timestamp, species, confidence, filepath)
                VALUES (?, ?, ?, ?)
            """, (timestamp, row.get('common_name', 'unknown'), float(row.get('confidence', 0)), filepath))

def get_last_detection():
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.execute("SELECT timestamp FROM detections ORDER BY timestamp DESC LIMIT 1")
        result = cur.fetchone()
        return result[0] if result else None
