from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy #for working with databases

#create an app instance with a double underscore name
app = Flask(__name__)

#creating routes is as simple as defining a function and using apprpriate decorators

@app.route('/')
def index():
    return "Hello World"
