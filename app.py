from flask import Flask, render_template, request, redirect, url_for

from models.database import Database
from models.user import User
from models.product import Product
from controllers.routing import Routing
app = Flask(__name__)
app.config["SECRET_KEY"] = "123456789"  # Klucz do obsługi CSRF
DB_NAME = "sklep.db"


# Inicjalizacja bazy i obiektów
db = Database(DB_NAME)
user_manager = User(db)
product_manager = Product(db)

routing = Routing(app, user_manager, product_manager)

if __name__ == "__main__":
    app.run(debug=True, port=8081)