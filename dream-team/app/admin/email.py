# app/admin/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class EmailForm(FlaskForm):
    """
    Form for admin to add or edit a Event
    """
    subject = StringField('Subject')#, validators=[DataRequired()])
    html = StringField('Message')#, validators=[DataRequired()])
    submit = SubmitField('Send')

