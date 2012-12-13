# -*- coding: utf-8 -*-
import os, datetime
import re
from unidecode import unidecode
import random

from flask import Flask, request, render_template, redirect, abort, jsonify
import requests

# Twilio
from twilio.rest import TwilioRestClient

# create Flask app
app = Flask(__name__)   # create our flask app


# --------- Routes ----------

@app.route('/', methods=['GET','POST'])
def twilio():
	if request.method == "GET":
		return render_template('twilio.html')

	elif request.method == "POST":

		telephone = request.form.get('telephone')
		person_name = request.form.get('person_name')
		if request.form["action"] == "What should I wear today?":
			foo=['Rain boots', 'Lots of make up', 'Boat shoes and a toupe']
			from random import choice
			text= choice(foo)
			#text = "It's November. Whatever you do, be sure to put on a jacket"
		elif request.form["action"] == "What should I eat for lunch?":
			foo=['Tofu', 'Check your fridge, do not ask me', 'Call your mom']
			from random import choice
			text= choice(foo)
			#text = "You will OD on meat later this week, so get some veggies"
		elif request.form["action"] == "What makes me happy?":
			foo=['British Royalty', 'Bunnies and Cats on Buzzfeed', 'Movies based on movies based on books']
			from random import choice
			text= choice(foo)
			#text = "Having all the answers with minimal work"
		

		#prepare telephone number. regex, only numbers
		telephone_num = re.sub("\D", "", telephone)
		if len(telephone_num) !=10:
			return "Make sure you entered the right number"
		else:
			to_number = "+1" + str(telephone_num) #US country only now


			account = os.environ.get('TWILIO_ACCOUNT_SID')
			token = os.environ.get('TWILIO_AUTH_TOKEN')

			client = TwilioRestClient(account, token)

			from_telephone = os.environ.get('TWILIO_PHONE_NUMBER') # format +19171234567

			message = client.sms.messages.create(to=to_number, from_=from_telephone,
	                                     body="Hello " + person_name + text)

			return "Check your phone '%s'" % person_name
			


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404



# --------- Server On ----------
# start the webserver
if __name__ == "__main__":
	app.debug = True
	
	port = int(os.environ.get('PORT', 5000)) # locally PORT 5000, Heroku will assign its own port
	app.run(host='0.0.0.0', port=port)



	