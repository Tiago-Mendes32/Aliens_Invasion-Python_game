import sqlite3

class DBProxy:
    def __init__(self, db_name: str):
        self.db_name = db_name
        self.connection = sqlite3.connect(db_name)
        self.connection.execute('''
            CREATE TABLE IF NOT EXISTS data(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                enemies_destroyed INTEGER NOT NULL,
                level_arrived TEXT NOT NULL,
                time FLOAT NOT NULL,
                date TEXT NOT NULL)
        ''')

    def save(self, score_dict: dict):
        self.connection.execute(
            'INSERT INTO data (name, enemies_destroyed, level_arrived, time, date) VALUES (:name, :enemies_destroyed, :level_arrived, :time, :date)',
            score_dict)
        self.connection.commit()

    def retrieve_top10(self) -> list:
        return self.connection.execute(
            'SELECT * FROM data ORDER BY level_arrived DESC, time ASC LIMIT 10').fetchall()

    def close(self):
        self.connection.close()