from flask import Flask
app = Flask(__name__)
from flask import render_template
from flask import request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models import User

@app.route('/login/')
def login(name=None):
   	error = None
   	if request.method == 'POST':
   		if valid_login(request.form['username'],
   			request.form['password']):
   			return log_the_user_in(request.form['username'])
   		else:
   			error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
	return render_template('test.html', error=error)

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')