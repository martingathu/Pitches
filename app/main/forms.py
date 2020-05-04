# from .forms import UpdateProfile
# from .. import db

# class UpdateProfile(FlaskForm):
#     bio = TextAreaField('Tell us about you.',validators = [Required()])
#     submit = SubmitField('Submit')


from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, SelectField
from wtforms.validators import InputRequired, Length, EqualTo, ValidationError, Email
from ..models import User

def invalid_credentials(form, field):
    """Username and password checker"""
    username_entered =form.username.data
    password_entered = field.data

    user_object = User.query.filter_by(username=username_entered).first()
    if user_object is None or not user_object.verify_password(password_entered):
        raise ValidationError("Username or Password is incorrect")

    
class RegistrationForm(FlaskForm):
    """Restration form"""
    email = StringField('Your Email Address',validators=[InputRequired(),Email()])
    username = StringField('username', validators=[InputRequired(message='Username required'), Length(min=4, max=25, message='Username must be between 4 and 25 characters')])
    password = PasswordField('password', validators=[InputRequired(message='Password required'), Length(min=4, max=25, message='Password must be between 4 and 25 characters')])
    confirm_pswd = PasswordField('confirm Password', validators=[InputRequired(message='Password required'), EqualTo('password', message="Passwords must match")])
    submit_button = SubmitField('Create')

    def validate_username(self, username):
        user_object = User.query.filter_by(username=username.data).first()
        if user_object:
            raise ValidationError("Username already taken!")

class LoginForm(FlaskForm):
    """Login form"""

    username = StringField('username', validators=[InputRequired(message="Username required")])
    password = PasswordField('password', validators=[InputRequired(message="Password required"), invalid_credentials])
    submit_button = SubmitField('Login')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [InputRequired(message="Bio is required")])
    submit= SubmitField('Update')

class PitchForm(FlaskForm):
    title = StringField('title', validators=[InputRequired(message="Title required")])
    category = SelectField('category', choices=[('product', 'product'), ('interview', 'interview'), ('promotion', 'promotion')], validators=[InputRequired(message="Category required")])
    description = StringField('description', validators=[InputRequired(message="Description required")])
    submit= SubmitField('Update')