from flask import Flask, request, redirect
import twilio.twiml
import csv 
import os.path

app = Flask(__name__)
 
@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """Respond to incoming calls with a simple text message."""
 
    resp = twilio.twiml.Response()
    body = request.values.get('Body', None)
    parse_var = ""
    room_name = ""
    timer_count = ""
    email_name = ""
    
    print(body)
    parse_var = body.split()
    print(parse_var)
 #   results = [] 

    if(parse_var[0].lower() == "create"):
      if (os.path.isfile(parse_var[1] + '.csv')):
	resp.message("Please choose another name")
 	return str(resp)
      else:
	results = [['name', 'phone', 'email', 'address', 'birthday']]
	resultFile = open(parse_var[1] + ".csv", 'wb')
	wr = csv.writer(resultFile, dialect="excel")	
        wr.writerows(results)	
      print("The user wants to create a room")
    
    elif(parse_var[0].lower() == "join"):
      print("The user wants to join a room")
      if (os.path.isfile(parse_var[1]+ ".csv") ):
	join_results = [[parse_var[2], parse_var[3], parse_var[4], parse_var[5]]]
        resultFile = open(parse_var[1] + ".csv", 'a')
        wr = csv.writer(resultFile, dialect='excel')
        wr.writerows(join_results)
	resp.message("Thank you, your responses have been recorded into room: %s" % parse_var[1])
      else:
 	resp.message("You have entered a room that has not been created yet. Please ente	r another room or create a room\n") 
    else:
	resp.message("Hi! Here are your usage cases:\n [create roomname hours_of_usage, email] to create an attendance sheet. \n Or do [join roomname name email] to join an existing room. For more information, type HELP ")
        return str(resp)

    
    return str(resp)
    
 
if __name__ == "__main__":
    app.debug = True 
    app.run(host='0.0.0.0')
