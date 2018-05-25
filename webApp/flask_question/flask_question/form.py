from flask_wtf import FlaskForm
from wtforms import TextField, SubmitField
from wtforms.validators import DataRequired

class Login_form(FlaskForm):
	username = TextField('username', validators=[DataRequired()])
	password = TextField('password',  validators=[DataRequired()])
	submit = SubmitField('Login')
