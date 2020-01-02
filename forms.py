from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm): #still need to validate fields
	email = StringField('Email')
	password = PasswordField('Password')
	confirm_password = PasswordField('Confirm Password')
	submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
	email = StringField('Email')
	password = PasswordField('Password')
	submit = SubmitField('Login')
