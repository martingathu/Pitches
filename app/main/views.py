from flask import render_template,request,redirect,url_for, abort, flash
from . import main
from ..models import User, Pitch
from flask_login import login_required
from .forms import RegistrationForm, LoginForm
from .. import db
from flask_login import login_user,logout_user,login_required
from ..email import mail_message
from werkzeug.security import generate_password_hash

# @main.route('/')
# def index():

#     '''
#     View root page function that returns the index page and its data
#     '''
#     message = 'Hello Pitchez'

#     title = 'HOME - best pitch of the day'
#     return render_template('index.html', message = message, title=title)

@main.route('/')
def index():

    pitches = Pitch.query.all()
    return render_template('index.html', pitches=pitches)


@main.route('/signup' , methods=['GET', 'POST'])
def signup():

    reg_form = RegistrationForm()

    #updates the db if the validation was successful
    if reg_form.validate_on_submit():
        email = reg_form.email.data
        username = reg_form.username.data
        password = generate_password_hash(reg_form.password.data)
        
        user = User(email=email, username=username, password=password)
        db.session.add(user)
        db.session.commit()

        flash('Registered successfully.Please login', 'success')

        return redirect(url_for('main.login'))
        
    return render_template('register.html', form=reg_form)


@main.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()

    #login if validation is successful
    if login_form.validate_on_submit():

        # Get a user by username and check password matches hash
        user_object =User.query.filter_by(username=login_form.username.data).first()
        login_user(user_object)
        return redirect(url_for('main.profile',uname=login_form.username.data))
        

    return render_template('login.html', form=login_form)

@main.route('/user/<uname>', methods=['GET', 'POST'])
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    form = PitchForm()

    if not current_user.is_authenticated:
        flash('please login', 'danger')
        return redirect(url_for('main.login'))

    if form.validate_on_submit():
        title = form.title.data
        category = form.category.data
        description = form.description.data
        
        pitch = Pitch(owner_id=user.id, title=title, category=category, description=description)
        db.session.add(pitch)
        db.session.commit()

        return redirect(url_for('main.profile', uname=user.username))

    return render_template("profile.html", user=user, form=form)

@main.route('/logout', methods=['GET'])
def logout():
    logout_user()
    flash('you have logged out successfuly', 'success')

    return redirect(url_for('main.index'))

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

