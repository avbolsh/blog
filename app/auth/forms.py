from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SubmitField, PasswordField


class LoginForm(FlaskForm):
    name = SubmitField("Name")
    email = EmailField("Email")
    passwod = PasswordField("Password")
    submit = SubmitField("Login") 