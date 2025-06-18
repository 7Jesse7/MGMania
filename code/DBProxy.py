import sqlite3

class DBProxy:
    def __init__(self, db_name: str):
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

# O que foi mantido e ajustado: ✔ Banco de dados SQLite3 funcionando corretamente para salvar scores. ✔ Sistema de ranking Top 10 para mostrar os melhores jogadores. ✔ O banco de dados é inicializado automaticamente se não existir (__initialize_db). ✔ Função save() para armazenar nome, score e data.

# Onde substituir assets: 🔹 Banco de dados → O arquivo .db será criado automaticamente dentro do diretório ./data/.