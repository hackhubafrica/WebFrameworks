from flask import Flask ,request,make_response,redirect
app = Flask(__name__)

#This is a decorator and they can modify the behavior of a function in different ways.
#A common pattern is to use decorators to register functions as handlers for an event.
@app.route('/')   
def index():
   #return '<h1>Bad Request</h1>', 400    #The following view function returns a 400 status code, the code for a bad request error:
   
   return redirect('http://www.example.com')  #Flask provides a redirect() helper function that creates this response:
   
   response = make_response('<h1>This document carries a cookie!</h1>')
   response.set_cookie('answer', '42')
   return response

   user_agent = request.headers.get('User-Agent')
   return '<h1>Hello World!</h1> <b>Your browser is %s</b>' % user_agent
   #return '<h1>Hello World!</h1>'

@app.route('/user/<name>')
def user(name):
 return '<h1>Hello, %s!</h1>' % name


@app.route('/user/<id>')
def get_user(id):
 user = load_user(id)
 if not user:
   abort(404)                        #the abort function, which is used for error handling
 return '<h1>Hello, %s</h1>' % user.name


#Ensures that the development web server is started only when the script is executed directly
 if __name__ == '__main__': 
    app.run(debug=True)

'''
Flask’s development web server supports a number of startup configuration options,
but the only way to specify them is by passing them as arguments to the app.run() call
in the script. This is not very convenient; the ideal way to pass configuration options is
through command-line arguments.

Flask-Script is an extension for Flask that adds a command-line parser to your Flask
application. It comes packaged with a set of general-purpose options and also supports
custom commands.
'''