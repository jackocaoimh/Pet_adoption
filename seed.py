from models import db, Pet
from app import app

with app.app_context():
# This assumes you have a Flask app instance in app.py
# connect_db(app)


# If you want to start fresh with each seed, you can drop all data first
    db.drop_all()
    db.create_all()

    # Creating some pet instances
    pet1 = Pet(name='Buddy', species='Dog', photo_url='https://example.com/buddy.jpg', age=3, notes='Friendly and energetic.', available=True)
    pet2 = Pet(name='Whiskers', species='Cat', photo_url='https://example.com/whiskers.jpg', age=2, notes='Loves to nap and cuddle.', available=True)
    pet3 = Pet(name='Goldie', species='Fish', photo_url='', age=1, notes='Beautiful goldfish.', available=True)

    # Adding pets to the session
    db.session.add(pet1)
    db.session.add(pet2)
    db.session.add(pet3)

    # Committing the changes to the database
    db.session.commit()
