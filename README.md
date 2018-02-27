# fyp-group-project
Group 7: Final Year Group Project

Dependencies
- Ubuntu 16.04 LTS
- Python
- pip

## Install and Run Instructions using scripts
1. Install Git and clone the repo
```
sudo apt install git
git clone https://github.com/weijielam/fygroupproject.git
```

2. Run install.sh script, activate virtualenv, install requirements

```
sudo bash install.sh
source Envs/my-venv/bin/activate
sudo pip install -r requirements.txt
``` 

3. Set up sql user and database
```
mysql -u root -p
--enter admin password
CREATE USER 'dt_admin'@'localhost' IDENTIFIED BY 'dt2016';
CREATE DATABASE dreamteam_db;
GRANT ALL PRIVILEGES ON dreamteam_db . * TO 'dt_admin'@'localhost';
\q
```

4. Set up ENVIRONMENT VARIABLES and database
```
cd dream-team
export FLASK_CONFIG=development
export FLASK_APP=run.py
flask db upgrade
```

5. Create an admin account 
```
flask shell
```

```
from app.models import User
from app import db
admin = User(email="admin@admin.com",username="admin",password="admin2018",is_admin=True)
db.session.add(admin)
db.session.commit()
exit()
```

6. Running Flask App: run.sh
```
cd ..
bash run.sh
```
7. Open up browser at localhost:5000

For Feature Documentation go to Documentation folder

[Feature Documentation](repo/blob/master/Documentation/Feature Documentation.md)
## Manual Install and Run Instructions from Fresh Install Of Ubuntu 16.04
1. Install Git and clone the repo
```
sudo apt install git
git clone https://github.com/weijielam/fygroupproject.git
```

2. Install aptitude
```
sudo apt install aptitude
```

3. Install sql dependencies using aptitude
```
sudo aptitude install build-essential python-dev libmysqlclient-dev
```

4. Install and and setup mySQL
```
sudo apt-get install mysql-server
--enter admin password when prompted
```

5. Set up sql user and database
```
mysql -u root -p
--enter admin password
CREATE USER 'dt_admin'@'localhost' IDENTIFIED BY 'dt2016';
CREATE DATABASE dreamteam_db;
GRANT ALL PRIVILEGES ON dreamteam_db . * TO 'dt_admin'@'localhost';
\q
```

6. Install python-pip
```
sudo apt-get install python-pip
pip install --upgrade pip
```

7. Install pip dependencies
```
cd fygroupproject/
source Envs/my-venv/bin/activate
sudo pip install -r requirements.txt
```

8. Setup flask environment
```
cd dream-team
export FLASK_CONFIG=development
export FLASK_APP=run.py
```

9. Initialise database tables
```
flask db upgrade
```

10. Create an admin account 
```
flask shell
```

```
from app.models import User
from app import db
admin = User(email="admin@admin.com",username="admin",password="admin2018",is_admin=True)
db.session.add(admin)
db.session.commit()
exit()
```

11. Run server
```
flask run
```

12. Open site
```
Open browser
enter "localhost:5000" into url bar
```

13. Login as admin
```
Enter email "admin@admin.com"
Enter password "admin2018"
```

-------

For Feature Documentation go to Documentation folder
