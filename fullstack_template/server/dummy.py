import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tabledef import *
 
engine = create_engine('sqlite:///fygp.db', echo=True)
 
# create a Session
Session = sessionmaker(bind=engine)
session = Session()
 
user = User("admin","password")
session.add(user)
 
user = User("python","python")
session.add(user)
 
user = User("jumpiness","python")
session.add(user)

user = User("laura","passcode")
session.add(user)

user = User("wei","lam")
session.add(user)
 
user = User("patrick","berry")
session.add(user)

user = User("james","leni")
session.add(user)

# commit the record the database
session.commit()
 
session.commit()
