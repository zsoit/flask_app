class Product:
    def __init__(self, db):
        self.db = db

    def add_product(self, name, description, price, stock, category_id):
        """ Dodaje nowy produkt """
        query = """
        INSERT INTO Produkt (PROD_Nazwa, PROD_Opis, PROD_Cena, PROD_StanMagazynowy, KAT_id)
        VALUES (?, ?, ?, ?, ?)
        """
        self.db.execute_query(query, (name, description, price, stock, category_id))

    def get_products(self):
        """ Pobiera listę produktów """
        query = "SELECT PROD_id, PROD_Nazwa, PROD_Cena FROM Produkt"
        return self.db.fetch_query(query)

    def delete_product(self, product_id):
        """ Usuwa produkt po ID """
        query = "DELETE FROM Produkt WHERE PROD_id = ?"
        self.db.execute_query(query, (product_id,))