import sqlite3
import os

class DBProxy:
    def __init__(self, db_name: str):
        os.makedirs("data", exist_ok=True)  #  Cria a pasta se não existir
        self.conn = sqlite3.connect(f'./data/{db_name}.db')
        self.cursor = self.conn.cursor()
        self.__initialize_db()

    def __initialize_db(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS scores (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                score INTEGER NOT NULL,
                date TEXT NOT NULL
            )
        ''')
        self.conn.commit()

    def save(self, data: dict):
        self.cursor.execute('''
            INSERT INTO scores (name, score, date)
            VALUES (:name, :score, :date)
        ''', data)
        self.conn.commit()

    def retrieve_top10(self):
        self.cursor.execute('''
            SELECT id, name, score, date
            FROM scores
            ORDER BY score DESC
            LIMIT 10
        ''')
        return self.cursor.fetchall()

    def close(self):
        self.conn.close()
