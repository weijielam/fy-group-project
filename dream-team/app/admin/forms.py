# app/admin/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class EventForm(FlaskForm):
    """
    Form for admin to add or edit a Event
    """
    name = StringField('Name', validators=[DataRequired()])
    timeD = StringField('Time', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Submit')


class AdminAccessForm(FlaskForm):
    """
    Form to grant admin access
    """
    email = StringField('Email', validators=[DataRequired()])
    submit = SubmitField('Grant Access')
    
