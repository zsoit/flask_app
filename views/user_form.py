from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email


class UserForm(FlaskForm):
    name = StringField("Imię", validators=[DataRequired()])
    surname = StringField("Nazwisko", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Hasło", validators=[DataRequired()])
    submit = SubmitField("Dodaj użytkownika")
