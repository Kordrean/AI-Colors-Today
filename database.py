import sqlite3


class ColorDatabase:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS color_responses (
                id INTEGER PRIMARY KEY,
                date TEXT,
                color_code TEXT,
                reason TEXT
            )
        ''')
        self.connection.commit()

    def insert_response(self, date, color_code, reason):
        self.cursor.execute('''
            INSERT INTO color_responses (date, color_code, reason)
            VALUES (?, ?, ?)
        ''', (date, color_code, reason))
        self.connection.commit()

    def retrieve_responses(self):
        self.cursor.execute('''
            SELECT color_code, reason FROM color_responses
        ''')
        return self.cursor.fetchall()


if __name__ == "__main__":
    db_file = "color_responses.db"
    color_db = ColorDatabase(db_file)
    color_db.insert_response("2024-04-17", "#FF0000", "Red represents excitement.")
    responses = color_db.retrieve_responses()
    # print("All responses:")
    # for response in responses:
        # print(response)

