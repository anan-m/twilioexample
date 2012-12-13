
Download code. Open code directory in Terminal.

#### #1 Create virtualenv

	virtualenv venv


#### #2 Install requirements

In your code directory run the command below to install new requirements.

	. runpip

or

	. venv/bin/activate
	pip install -r requirements.txt


2 new libraries we're using in this example, Twilio and Requests


#### #3 Start server

Start server

	. start

or 

	. venv/bin/activate
	foreman start

-----------


## Twilio demo

demo /twilio

### Getting Twilio Account

* Register [https://www.twilio.com/try-twilio](https://www.twilio.com/try-twilio).
* Verify phone number with access code.
* Pick a phone number.
* Poke around all their API endpoints, make and receive calls, make and receive SMS.

When you are registered locate your your Account SID and Auth Token here,[https://www.twilio.com/user/account](https://www.twilio.com/user/account) and add them to your .env file

**.env**	

	TWILIO_ACCOUNT_SID=xxxxxxxxxxxxxx
	TWILIO_AUTH_TOKEN=xxxxxxxxx
	TWILIO_PHONE_NUMBER=+XXXXXXXXX

Now let's add the Twilio account variables to Heroku.

**In your code directory in Terminal run,**

	heroku config:add TWILIO_ACCOUNT_SID=xxxxxxxxxxxxxx
	heroku config:add TWILIO_AUTH_TOKEN=xxxxxxxxxxxxxx
	heroku config:add TWILIO_PHONE_NUMBER=+XXXXXXXXX


