import sqlite3

conn = sqlite3.connect("game_scores.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS scores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        score INTEGER,
        date TEXT
    )
""")

conn.commit()
conn.close()
print("✅ Banco de dados inicializado corretamente!")
