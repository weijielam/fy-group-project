from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os
from sqlalchemy.orm import sessionmaker
from tabledef import *
engine = create_engine('sqlite:///fygp.db', echo=True)
 
app = Flask(__name__)

@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    if session.get('logged_in'):
	return "Hello Boss!  <a href='/logout'>Logout</a>"
    
 
@app.route('/login', methods=['POST'])
def do_admin_login():
 
    POST_USERNAME = str(request.form['username'])
    POST_PASSWORD = str(request.form['password'])

    Session = sessionmaker(bind=engine)
    s = Session()
    query = s.query(User).filter(User.username==POST_USERNAME, User.password==POST_PASSWORD, User.is_admin=="Y")
    result = query.first()
    if result:
        session['logged_in'] = True
    else:
        flash('wrong password!')
    return home()

@app.route('/register', methods=['POST'])
def register(): 
   # render_template('register.html')
    POST_USERNAME = str(request.form['username'])
    POST_EMAIL = str(request.form['username'])
    POST_PASSWORD1 = str(request.form['password'])
    POST_PASSWORD2 = str(request.form['password1'])

    if (POST_PASSWORD1 != POST_PASSWORD2):
	flash('Passwords do not match')
 
    Session = sessionmaker(bind=engine)
    s = Session()
 
    user = User(POST_USERNAME ,POST_PASSWORD1, POST_EMAIL, "Y" )
    s.add(user)	
    print("YOOOOOOOOOOOOOOO") 
    return home()
 
@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()
 
if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True,host='0.0.0.0', port=4000)
