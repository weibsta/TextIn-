from twilio.rest import TwilioRestClient

account = ""
token = ""
client = TwilioRestClient(account, token)


call = client.calls.create(to="",
			  from_="",
			  url="http://www.myinstants.com/media/sounds/and-his-name-is-john-cena-1.mp3")

print(call.sid)
	
