# app/user/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, IntegerField
from wtforms.validators import DataRequired, NumberRange

list_choices = [('Don', 'Donation'), ('Pl', 'Pledge'), ('Ti', 'Ticket')]

class paymentForm(FlaskForm):
	dol_amount = IntegerField('$', validators=[DataRequired()])
	cent_amount = IntegerField('.', validators=[DataRequired(), NumberRange(min=0, max=99, message="please enter a number between 0 and 99")])
	pay_type = SelectField('Type', choices = list_choices, validators=[DataRequired()])
	event = SelectField('Event', coerce=int)
	submit = SubmitField('Submit')