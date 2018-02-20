import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tabledef import *
 
engine = create_engine('sqlite:///fygp.db', echo=True)
 
# create a Session
Session = sessionmaker(bind=engine)
session = Session()
 
user = User("admin6","password", "suzy", "Y" )
session.add(user)
 

# commit the record the database
session.commit()
 
session.commit()

session.commit()
