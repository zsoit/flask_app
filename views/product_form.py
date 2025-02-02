from flask_wtf import FlaskForm
from wtforms.fields.numeric import FloatField, IntegerField
from wtforms.fields.simple import StringField, SubmitField
from wtforms.validators import DataRequired


class ProductForm(FlaskForm):
    name = StringField("Nazwa produktu", validators=[DataRequired()])
    description = StringField("Opis", validators=[DataRequired()])
    price = FloatField("Cena", validators=[DataRequired()])
    stock = IntegerField("Stan magazynowy", validators=[DataRequired()])
    category_id = IntegerField("ID kategorii", validators=[DataRequired()])
    submit = SubmitField("Dodaj produkt")

