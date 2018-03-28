# app/auth/views.py

from flask import flash, redirect, render_template, url_for, request
from flask_login import login_required, login_user, logout_user, current_user
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from . import auth
from forms import LoginForm, RegistrationForm, ResetPassword, ResetPasswordSubmit, Unsubscribe
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
                            password=form.password.data, is_subscribed=form.mailing_list.data)

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
                return redirect(request.args.get("next") or url_for("home.admin_dashboard"))
                # return redirect(url_for('home.admin_dashboard'))
            else:
                return redirect(request.args.get("next") or url_for("home.dashboard"))
            	# return redirect(url_for('home.dashboard'))

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
            link_for_token = "<a href=\"http://localhost:5000/reset?token="+ str(token) + "\">" + "Reset Password</a>"
            print("link for token: ",link_for_token)
            with mail.connect() as conn:
                message = "Hello I see you would like to change your password!"+ "Please click this link. " + link_for_token 
    
             
                subject = "Password Reset"
                msg = Message(recipients=[user.email],
                                sender="fygptest@gmail.com",
                              html=message,
                              subject=subject)
                conn.send(msg)
                flash("Email has been sent!")
        else:
            flash ("No such user in the database")
    token = request.args.get('token')       
    verified_result = User.verify_token(token)
    if token and verified_result:
        is_verified_token = True
        form = ResetPasswordSubmit()
        if form.validate_on_submit():
            verified_result.password=form.password.data
            verified_result.is_subscribed=verified_result.is_subscribed
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

######### START SETTINGS TAB CODE ########
@auth.route('/settings', methods=['GET', 'POST',])
@login_required
def settings():
    id = current_user.id
    user = User.query.get(id)
    #Settings tab for both users and admins
    form = ResetPasswordSubmit()
    if form.submit.data and form.validate():
            print("why the fuck is it form1")
            user.password=form.password.data
            db.session.commit()
            flash("Password updated successfully")

    form2 = Unsubscribe()
    if form2.unsubscribe.data and form2.validate():
            print("why the fuck is it form2")
            user.is_subscribed =  not user.is_subscribed
            db.session.commit()
            if user.is_subscribed: 
                flash("You are successfully subscribed")
            else:
                flash("You are successfully unsubscribed")


    return render_template('auth/settings.html', form=form, form2=form2, user=user, title='Settings') 


# @login_manager.unauthorized_handler
# def handle_needs_login():
#     flash("You have to be logged in to access this page.")
#     return redirect(url_for('account.login', next=request.path))

# @login_manager.unauthorized_handler
# def handle_needs_login():
#     flash("You have to be logged in to access this page.")
#     return redirect(url_for('account.login', next=request.path))

# def redirect_dest(home):
#     dest_url = request.args.get('next')
#     if not dest_url:
#         dest_url = url_for(home)
#     return redirect(dest_url)

# def redirect_dest(home):
#     dest_url = request.args.get('next')
#     if not dest_url:
#         dest_url = url_for(home)
#     return redirect(dest_url)


######### END SETTINGS TAB CODE ############    

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
