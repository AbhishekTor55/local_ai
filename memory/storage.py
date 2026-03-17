import sqlite3
import os

DB_FILE = os.path.join(os.path.dirname(__file__), "memory.db")


class StorageEngine:

    def __init__(self):
        self.conn = sqlite3.connect(DB_FILE)
        self.create_tables()

    def create_tables(self):

        cursor = self.conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            preferences TEXT
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS commands (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            command TEXT
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS mistakes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            mistake TEXT
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS errors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            error TEXT
        )
        """)

        self.conn.commit()

    # -------------------------
    # USERS
    # -------------------------

    def add_user(self, name):

        cursor = self.conn.cursor()

        cursor.execute(
            "INSERT INTO users (name) VALUES (?)",
            (name,)
        )

        self.conn.commit()

    # -------------------------
    # COMMANDS
    # -------------------------

    def add_command(self, command):

        cursor = self.conn.cursor()

        cursor.execute(
            "INSERT INTO commands (command) VALUES (?)",
            (command,)
        )

        self.conn.commit()

    # -------------------------
    # ERRORS
    # -------------------------

    def add_error(self, error):

        cursor = self.conn.cursor()

        cursor.execute(
            "INSERT INTO errors (error) VALUES (?)",
            (error,)
        )

        self.conn.commit()

    # -------------------------
    # MISTAKES
    # -------------------------

    def add_mistake(self, mistake):

        cursor = self.conn.cursor()

        cursor.execute(
            "INSERT INTO mistakes (mistake) VALUES (?)",
            (mistake,)
        )

        self.conn.commit()