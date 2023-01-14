"""wtf login form"""
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    """wtf login form"""
    email = StringField('Email', validators=[
        DataRequired(
            message="Email field cannot be empty"
        )])
    password = StringField('Password', validators=[DataRequired(
        message="Password field cannot be empty"
    )])
    submit = SubmitField('Login')
