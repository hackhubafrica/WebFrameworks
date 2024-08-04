from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy #for working with databases

#create an app instance with a double underscore name
app = Flask(__name__)

#configuration variables for the database
'''
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///missing_persons.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#db.init_app(app)    # Initialize SQLAlchemy with the app
    
#create a model for the database
class ToDo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)

#to create and initialize the database
db.create_all()

#creating routes is as simple as defining a function and using apprpriate decorators
'''
def create_app():
    @app.route('/')
    def index():
        return "Hello World"
    return app
'''
def create_app():
    @app.route('/')
    def index():
        return "Hello World"
    

    @app.get('/')
    def home():
        todo_list=db.session.query(ToDo).all
        return render_template("base.html", todo_list=todo_list)


    @app.post('/add')
    def add():
        title = request.form.get("title")
        new_todo=ToDo(title=title,complete=False)
        db.session.add(new_todo)   
        db.session.commit()
        return redirect(url_for("home"))


    @app.get('/update/<int:todo_id>')
    def update(todo_id):
        todo=db.session.query(ToDo).filter(ToDo.id == todo_id.first)
        todo.complete = not todo.complete
        db.session.commit()
        return redirect(url_for("home"))


    @app.get('/delete/<int:todo_id>')
    def delete(todo_id):
        todo=db.session.query(ToDo).filter(ToDo.id == todo_id.first)
        todo.delete = delete(todo)
        db.session.commit()
        return redirect(url_for("home"))
    return app
'''

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
