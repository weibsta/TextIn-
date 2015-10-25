from flask import Flask, request, redirect
import twilio.twiml
 
app = Flask(__name__)
 
@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """Respond to incoming calls with a simple text message."""
 
    resp = twilio.twiml.Response()
    resp.message("Hi! Here are your usage cases:\n [create roomname hours_of_usage, email] to create an attendance sheet. \n Or do [join roomname name email] to join an existing room. For more information, type HELP ")
    body = request.values.get('Body', None)
    parse_var = ""
    room_name = ""
    
    print(body)
    parse_var = body.split(' ',1)[0]
    print(parse_var)
    if(parse_var.lower() == "create"):
      print("The user wants to create a room")
      room_name = body.split(' ',2)[1]
      timer_count = body.split(' ',2)[2]
      email_name = body.split(' ',2)[3]
      print(timer_count) 
      print(email_name)
      print(room_name)
    elif(parse_var.lower() == "join"):
      print("The user wants to join a room")
    else:
      return str(resp)

    
    return str(resp)
    
 
if __name__ == "__main__":
    app.debug = True 
    app.run(host='0.0.0.0')
