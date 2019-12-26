import smtplib, ssl
from bs4 import BeautifulSoup
import requests

airport = input("Enter airport call sign: ") #Ex. KLWC for Lawrence

# three lines make the '%s' easier to see (which is the airport)
url = ("""https://aviationweather.gov/adds/tafs/?station_ids=
%s
&std_trans=translated&submit_both=Get+TAFs+and+METARs""" % (airport))
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
METAR = soup.findAll('strong')[1] #2nd <strong> is METAR as of 12/26/2019


print(test1)


sender_email = "yourflightweather@gmail.com"
receiver_email = "jake@staab.dev"
message = str(METAR)
smtp_server = "smtp.gmail.com"
port = 465
password = input("Enter your password and press enter: ")

context = ssl.create_default_context()

with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
	server.login(sender_email, password)
	server.sendmail(sender_email, receiver_email, message)


