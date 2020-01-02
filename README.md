# aviation_weather

The purpose of this program is for pilots to receive automated emails at set time intervals prior to scheduled flights
that contain important weather information.

Users will need to create profiles in order to login and submit their flight information.

Users will enter upcoming flight dates, times, and which airports will be used. They will then receive an email one hour
prior to each flight (this timeframe can be adjusted) that provides METAR info taken from www.aviationweather.gov.


Required Packages:
------------------
beautifulsoup4
Flask
Flask-SQLAlchemy
requests
SQLAlchemy
WTForms
