from flask import render_template, redirect, url_for
from views.user_form import UserForm
from views.product_form import ProductForm

class Routing:

    def __init__(self, app, user_manager, product_manager):
        self.app = app
        self.user_manager = user_manager
        self.product_manager = product_manager

        # Rejestracja tras
        self.register_routes()

    def register_routes(self):
        """ Rejestracja tras w aplikacji """
        self.app.add_url_rule("/", view_func=self.home)
        self.app.add_url_rule("/users", view_func=self.users, methods=["GET", "POST"])
        self.app.add_url_rule("/delete_user/<int:user_id>", view_func=self.delete_user)
        self.app.add_url_rule("/products", view_func=self.products, methods=["GET", "POST"])
        self.app.add_url_rule("/delete_product/<int:product_id>", view_func=self.delete_product)

    def home(self):
        """ Strona główna """
        return render_template("index.html")

    def users(self):
        """ Strona użytkowników z formularzem dodawania """
        form = UserForm()
        if form.validate_on_submit():
            self.user_manager.add_user(
                form.name.data, form.surname.data, form.email.data, form.password.data
            )
            return redirect(url_for("users"))

        users = self.user_manager.get_users()
        return render_template("users.html", form=form, users=users)

    def delete_user(self, user_id):
        """ Usuwa użytkownika """
        self.user_manager.delete_user(user_id)
        return redirect(url_for("users"))

    def products(self):
        """ Strona produktów z formularzem dodawania """
        form = ProductForm()
        if form.validate_on_submit():
            self.product_manager.add_product(
                form.name.data, form.description.data, form.price.data, form.stock.data, form.category_id.data
            )
            return redirect(url_for("products"))

        products = self.product_manager.get_products()
        return render_template("products.html", form=form, products=products)

    def delete_product(self, product_id):
        """ Usuwa produkt """
        self.product_manager.delete_product(product_id)
        return redirect(url_for("products"))