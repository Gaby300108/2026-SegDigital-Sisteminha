import sqlite3


class DatabaseService:
    connection: sqlite3.Connection = None
    cursor: sqlite3.Cursor = None
    db_url: str = None

    def __init__(self, db_url: str):
        self.db_url = db_url
        if self.connection:
             self.disconnect()

    def connect(self):
        if not self.db_url or self.db_url.strip() == "":
            raise ValueError("Database URL is not set. Cannot connect to the database.")
        self.connection = sqlite3.connect(self.db_url)
        self.cursor = self.connection.cursor()

    def disconnect(self):
        if self.connection:
            self.connection = None

    def execute_query(self, query):
        if not self.connection:
            raise RuntimeError("Cannot execute query: No active database connection.")

