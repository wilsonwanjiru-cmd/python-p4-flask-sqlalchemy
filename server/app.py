# app.py

from flask import Flask
from models import Owner, Pet, db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/')
def home():
    with app.app_context():
        # Print owners
        owners = Owner.query.all()
        for owner in owners:
            print(f'Owner: {owner.name}')

        # Print pets
        pets = Pet.query.all()
        for pet in pets:
            print(f'Pet: {pet.name}, Species: {pet.species}, Owner: {pet.owner.name}')

    return 'Hello, Flask-SQLAlchemy is working!'

if __name__ == '__main__':
    app.run(port=5555, debug=True)
