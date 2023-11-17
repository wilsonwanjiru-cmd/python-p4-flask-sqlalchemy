# add_data.py

from app import app, db  # Assuming your Flask app instance is in app.py
from models import Owner, Pet

# Flask app context
with app.app_context():
    # Create and add owners
    owner1 = Owner(name='John Doe')
    owner2 = Owner(name='Jane Doe')
    db.session.add_all([owner1, owner2])

    # Commit the changes to the database
    db.session.commit()

    # Create and add pets
    pet1 = Pet(name='Buddy', species='Dog', owner=owner1)
    pet2 = Pet(name='Whiskers', species='Cat', owner=owner2)
    pet3 = Pet(name='Fluffy', species='Rabbit', owner=owner1)
    db.session.add_all([pet1, pet2, pet3])

    # Commit the changes to the database
    db.session.commit()
