from flask import Flask, render_template, url_for, redirect, request
from flask_wtf import FlaskForm
import smtplib, ssl
from bs4 import BeautifulSoup
import requests
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField


app = Flask(__name__)
app.config['SECRET_KEY'] = 'sdkjnw4o98ryuawef(*Lzsd09wfh'

class Airport(FlaskForm):
	callsign = StringField('Airport')
	submit = SubmitField('Enter')

def get_metar(airport):
	METAR = ''
	metar_tag = ''
	if request.form.get(airport) != '':
		callsign = request.form.get(airport)
		url = ("""https://aviationweather.gov/adds/tafs/?station_ids=%s&std_trans=translated&submit_both=Get+TAFs+and+METARs""" % (callsign))
		response = requests.get(url)
		soup = BeautifulSoup(response.text, "html.parser")
		METAR = soup.findAll('strong')
	
	if len(METAR) == 0:
		metar_tag = ''
	else:
		metar_tag = METAR[1].text
	
	return metar_tag
	
		

@app.route("/", methods=['GET', 'POST'])
@app.route("/index", methods=['GET', 'POST'])
def home():
	form = Airport()
	metar = get_metar('callsign')
	return render_template('index.html', form=form, metar=metar)


if __name__ == '__main__':
	app.run(debug=True)


