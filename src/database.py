import sqlite3
import os

DB_PATH = "data/tjk_proje.db"

def get_connection():
    os.makedirs("data", exist_ok=True)
    return sqlite3.connect(DB_PATH)

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS horses (
            horse_id INTEGER PRIMARY KEY AUTOINCREMENT,
            horse_name TEXT NOT NULL UNIQUE,
            birth_year INT,
            gender TEXT,
            sire TEXT,
            dam TEXT,
            total_earnings REAL DEFAULT 0.0
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS jockeys (
            jockey_id INTEGER PRIMARY KEY AUTOINCREMENT,
            jockey_name TEXT NOT NULL UNIQUE,
            total_rides INT DEFAULT 0,
            total_wins INT DEFAULT 0,
            win_rate REAL DEFAULT 0.0
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS races (
            race_id INTEGER PRIMARY KEY AUTOINCREMENT,
            race_date TEXT NOT NULL,
            hippodrome TEXT NOT NULL,
            race_number INT NOT NULL,
            track_type TEXT NOT NULL,
            distance INT NOT NULL,
            prize_pool REAL,
            race_condition TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS race_results (
            result_id INTEGER PRIMARY KEY AUTOINCREMENT,
            race_id INT,
            horse_id INT,
            jockey_id INT,
            finish_position INT,
            weight_carried REAL,
            finish_time TEXT,
            starting_gate INT,
            ganyan REAL,
            FOREIGN KEY(race_id) REFERENCES races(race_id),
            FOREIGN KEY(horse_id) REFERENCES horses(horse_id),
            FOREIGN KEY(jockey_id) REFERENCES jockeys(jockey_id)
        )
    """)

    conn.commit()
    conn.close()
    print("[INFO] Veritabanı ve tablolar başarıyla oluşturuldu.")
