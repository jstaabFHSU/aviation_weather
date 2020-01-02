from datetime import datetime
from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
import smtplib, ssl
from bs4 import BeautifulSoup
import requests
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sdkjnw4o98ryuawef(*Lzsd09wfh'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

airport = 'KLWC'
url = ("""https://aviationweather.gov/adds/tafs/?station_ids=%s&std_trans=translated&submit_both=Get+TAFs+and+METARs""" % (airport))
response = requests.get(url) #acts like browser and gets HTML from url
soup = BeautifulSoup(response.text, "html.parser")
METAR = soup.findAll('strong')[1].text

sender_email = "yourflightweather@gmail.com"
receiver_email = "jake@staab.dev"
message = str(METAR)
smtp_server = "smtp.gmail.com"
port = 465
password = '' # need to determine how to make login secure
context = ssl.create_default_context()

def send_email():
	with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
		server.login(sender_email, password)
		server.sendmail(sender_email, receiver_email, message)

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


if __name__ == '__main__':
	app.run(debug=True)
