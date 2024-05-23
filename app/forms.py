from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, EmailField
from wtforms.validators import DataRequired, EqualTo, Email, ValidationError
from app.models import User


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Sign in")

    

class RegisterForm(FlaskForm):
    first_name = StringField("First name", validators=[DataRequired()])
    last_name = StringField("Last name", validators=[DataRequired()])
    username = StringField("Username", validators=[DataRequired()])
    password1 = PasswordField("Password", validators=[DataRequired()])
    password2 = PasswordField("(Change) password", validators=[DataRequired(), EqualTo('password1', message="Passwords must match")])
    submit = SubmitField("Register")
    
    def validate_username(self, username):
        user = User.query.filter_by(username = username.data).first()

        if user is not None:
            raise ValidationError('Please use a different username.')
        
    def validate_email(self, email):
        user = User.query.filter_by(email = email.data).first()

        if user is not None:
            raise ValidationError("please use a different email address.")