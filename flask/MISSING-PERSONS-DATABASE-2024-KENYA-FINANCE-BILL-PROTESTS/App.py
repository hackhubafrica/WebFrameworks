from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# Create the SQLAlchemy instance
db = SQLAlchemy()

def create_app():
    print("Initializing Flask app...")
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///missing_persons.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)    # Initialize SQLAlchemy with the app
    
    # Import and register blueprints or other configurations
    with app.app_context():
        print("Creating database tables...")
        from Models import MissingPerson
        db.create_all()

    @app.route('/')
    def index():
        persons = MissingPerson.query.all()
        return render_template('index.html', persons=persons)

    @app.route('/add', methods=['GET', 'POST'])
    def add_person():
        if request.method == 'POST':
            name = request.form['name']
            age = request.form['age']
            photo_url = request.form['photo_url']
            occupation = request.form['occupation']
            last_known_location = request.form['last_known_location']
            contact_info = request.form['contact_info']
            
            new_person = MissingPerson(
                name=name,
                age=age,
                photo_url=photo_url,
                occupation=occupation,
                last_known_location=last_known_location,
                contact_info=contact_info
            )
            
            db.session.add(new_person)
            db.session.commit()
            
            return redirect(url_for('index'))
        
        return render_template('add_person.html')
    print("App initialized:", app)
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
