from twilio.rest import TwilioRestClient

account = "ACee602631b49abf6c3c6d759237683b5b"
token = "e5b9d682049ceeec4fb19478bd594051"
client = TwilioRestClient(account, token)


#message = client.messages.create(to="+14088384091", from_="+14087249293", 
#				 body="Hello there!")

call = client.calls.create(to="4082212915",
			  from_="14087249293",
			  url="http://www.myinstants.com/media/sounds/and-his-name-is-john-cena-1.mp3")

print(call.sid)
	
