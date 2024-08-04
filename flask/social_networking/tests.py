##Application and Request Contexts

from app import app
from flask import current_app

#RuntimeError: working outside of application context
#print(current_app.name)

app_ctx = app.app_context()
app_ctx.push()
print(current_app.name)
app_ctx.pop()

'''
current_app.name fails when there is no application context active but
becomes valid once a context is pushed. Note how an application context is obtained
by invoking app.app_context() on the application instance.
'''
#Request Dispatching 
#To see what the URL map in a Flask application looks like

x=app.url_map  
print(x)













