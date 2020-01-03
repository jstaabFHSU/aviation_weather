from flask import render_template, url_for, redirect
from app1 import app
from app1.forms import RegistrationForm, LoginForm
from app1.models import User, Post
from app1.weather import METAR

@app.route("/")
@app.route("/index")
def home():
	return render_template('index.html', metar=METAR)

@app.route("/register", methods=['GET', 'POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		return redirect(url_for('home'))
	return render_template('register.html', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		return redirect(url_for('home'))
	return render_template('login.html', form=form)
