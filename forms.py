from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField

class SignUpForm(FlaskForm):
    username = StringField("Enter username")
    password = PasswordField("Enter password")
    submit = SubmitField("Sign Up")