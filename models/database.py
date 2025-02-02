# 📌 Klasa do obsługi bazy danych
import sqlite3

class Database:
    def __init__(self, db_name):
        self.db_name = db_name

    def execute_query(self, query, params=()):
        """ Wykonuje zapytania INSERT, UPDATE, DELETE """
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            conn.commit()

    def fetch_query(self, query, params=()):
        """ Wykonuje zapytania SELECT i zwraca wynik """
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            return cursor.fetchall()

