from flask_wtf import FlaskForm
from wtforms import SubmitField, IntegerField
from wtforms.validators import Length

class PassLengthForm(FlaskForm):
    pass_length = IntegerField("Insert Password Length (minimum: 3): ", validators = [Length(min=2)])
    submit_length = SubmitField("Submit")

