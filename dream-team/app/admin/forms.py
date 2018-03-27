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
    date = StringField('Date', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    menu = StringField('Menu name eg Menu1.png')
    submit = SubmitField('Submit')


class AdminAccessForm(FlaskForm):
    """
    Form to grant admin access
    """
    email = StringField('Would you like to grant admin access to someone? Enter their email below!', validators=[DataRequired()])
    submit = SubmitField('Grant Access')
    
class GuestListForm(FlaskForm):
    """
    Form for edit needs of user on guestlist
    """
    needs = StringField('needs')
    submit = SubmitField('Submit')

class SelectedGuestsForm(FlaskForm):
    """
    Form for edit needs of user on guestlist
    """
    submit = SubmitField('Invite Selected?')
