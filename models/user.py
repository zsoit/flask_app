class User:
    def __init__(self, db):
        self.db = db

    def add_user(self, name, surname, email, password):
        """ Dodaje nowego użytkownika """
        query = """
        INSERT INTO Uzytkownik (UZ_imie, UZ_Nazwisko, UZ_Email, UZ_Haslo, UZ_DataRejestracji)
        VALUES (?, ?, ?, ?, datetime('now'))
        """
        self.db.execute_query(query, (name, surname, email, password))

    def get_users(self):
        """ Pobiera listę użytkowników """
        query = "SELECT UZ_id, UZ_imie, UZ_Nazwisko, UZ_Email FROM Uzytkownik"
        return self.db.fetch_query(query)

    def delete_user(self, user_id):
        """ Usuwa użytkownika po ID """
        query = "DELETE FROM Uzytkownik WHERE UZ_id = ?"
        self.db.execute_query(query, (user_id,))

