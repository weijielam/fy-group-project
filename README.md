# fyp-group-project
Final Year Group Project


This project shows you how to build a basic web application using popular web technologies 
like NPM, Webpack, React and Python.

Dependencies
- Ubuntu 16.04 LTS
- Node.js v8.9.4
- NPM 5.6.0
- Python
- pip

## Installing and Running from Fresh Install Of Ubuntu 16.04
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
CREATE USER 'dt_admin'@'localhost' IDENTIFIED BY 'dt2016'
CREATE DATABASE dreamteam_db
GRANT ALL PRIVILEGES ON dreamteam_db . * TO 'dt_admin'@'localhost'
```

6. Install python-pip
```
sudo apt-get install python-pip
```

7. Install pip dependencies
```
cd fygroupproject/
source Envs/my-venv/bin/activate
cd dream-team
pip install -r requirements.txt
```

8. Initialise database tables
```
flask db upgrade
```

9. Setup flask environment
```
export FLASK_CONFIG=development
export FLASK_APP=run.py
```

10. Run server
```
flask run
```

11. Open site
```
Open browser
enter "localhost:5000" into url bar
```

