from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, RadioField, SelectField, URLField
from wtforms.validators import InputRequired, Optional, URL, NumberRange

class AddPet(FlaskForm):
    """Form for adding pet"""
    name = StringField("Pet Name", validators=[InputRequired(message="Pet name cannot be blank.")])
    species = SelectField("Species", choices=[('cat', 'cat'), ('dog', 'dog'), ('porcupine', 'porcupine')])
    photo_url = URLField("Photo URL", validators=[URL(), Optional()])
    age = IntegerField("How old?", validators=[Optional(), NumberRange(min=0, max=30)])
    notes = StringField("Anything Else?")

class EditPet(FlaskForm):
    """Form for editing pet"""
    photo_url = URLField("Photo URL", validators=[URL(), Optional()])
    notes = StringField("Anything Else?")
    available = BooleanField("Available?")