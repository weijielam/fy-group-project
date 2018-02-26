# app/auth/views.py

from flask import flash, redirect, render_template, url_for, request
from flask_login import login_required, login_user, logout_user
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from . import auth
from forms import LoginForm, RegistrationForm, ResetPassword, ResetPasswordSubmit
from .. import db
from ..models import User
from flask_mail import Mail, Message 
from app import mail


@auth.route('/register', methods=['GET', 'POST'])
def register():
    """
    Handle requests to the /register route
    Add an user to the database through the registration form
    """
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,
                            username=form.username.data,
                            first_name=form.first_name.data,
                            last_name=form.last_name.data,
                            password=form.password.data)

        # add user to the database
        db.session.add(user)
        db.session.commit()
        flash('You have successfully registered! You may now login.')

        # redirect to the login page
        return redirect(url_for('auth.login'))

    # load registration template
    return render_template('auth/register.html', form=form, title='Register')

@auth.route('/login', methods=['GET', 'POST'])
def login():
    """
    Handle requests to the /login route
    Log an user in through the login form
    """
    form = LoginForm()
    if form.validate_on_submit():

        # check whether user exists in the database and whether
        # the password entered matches the password in the database
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(
                form.password.data):
            # log user in
            login_user(user)

            # redirect to the dashboard page after login
            if user.is_admin:
                return redirect(url_for('home.admin_dashboard'))
            else:
            	return redirect(url_for('home.dashboard'))

        # when login details are incorrect
        else:
            flash('Invalid email or password.')

    # load login template
    return render_template('auth/login.html', form=form, title='Login')

####### RESET PASSWORD CODE ########
@auth.route('/reset', methods=['GET', 'POST',])
def forgot_password():
    token = request.args.get('token')
    form = ResetPassword()
    if form.validate_on_submit():
        email = form.email.data
        user = User.query.filter_by(email=email).first()
        if user:
            token = user.get_token()
            print ("HERE'S THE OUL TOKEN LOVE",token)
        with mail.connect() as conn:
            message = 'Hello I see you would like to change your password! Please click this link. localhost:5000/reset?token='+token
            subject = "Password Reset"
            msg = Message(recipients=[user.email],
                            sender="fygptest@gmail.com",
                          body=message,
                          subject=subject)

<<<<<<< HEAD
            conn.send(msg)
=======
    verified_result = User.verify_token(token)        
######email stufff###########
    msg = Message('Hello', sender = MAIL_USERNAME, recipients = [verified_result.email])
    url = 'localhost:5000/reset?token='+token
    msg.body = "Hello I see you want to change your password for your charity partner event. Please click the link below to be taken to the reset page." + "\n" + url
    mail.send(msg)


>>>>>>> dd1e907276152a7dcc68bf18daab83d733870240

    verified_result = User.verify_token(token)
    if token and verified_result:
        is_verified_token = True
        form = ResetPasswordSubmit()
        if form.validate_on_submit():
            verified_result.password=form.password.data
            db.session.commit()
            
            flash("Password updated successfully")
            return redirect(url_for('auth.login'))                 
    return render_template('auth/reset.html', form=form, title='Reset')

def get_token(self, expiration=100):
        s = Serializer(['SECRET_KEY'])
        return s.dumps({'user': self.id}).decode('utf-8')

def verify_token(token):
    s = Serializer(['SECRET_KEY'])
    try:
        data = s.loads(token)
    except:
        return None
    id = data.get('user')
    if id:
        return User.query.get(id)
    return None   

######### END RESET PASSWORD CODE ########    

@auth.route('/logout')
@login_required
def logout():
    """
    Handle requests to the /logout route
    Log an user out through the logout link
    """
    logout_user()
    flash('You have successfully been logged out.')

    # redirect to the login page
    return redirect(url_for('auth.login'))
