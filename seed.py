"""Seed file to make sample data for db"""
from models import Pet, db
from app import app

# create all tables 
db.drop_all()
db.create_all()

Pet.query.delete()

pepper = Pet(name="Pepper", species="cat", photo_url="http://placekitten.com/200/300", age=4, notes="Great with kids and great personality.")

cory = Pet(name="Cory", species="cat", photo_url="http://placekitten.com/200/200", age=4, notes="Loves adventuring and the outdoors.")

db.session.add_all([pepper, cory])
db.session.commit()