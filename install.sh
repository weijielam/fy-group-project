# install virtualenv

sudo apt-get install aptitude -y
sudo aptitude install build-essential python-dev libmysqlclient-dev -y
sudo apt-get install mysql-server -y
sudo apt-get install python-pip -y
pip install virtualenv

# source sql.sh
# enter admin password when prompted
# sudo mysql -u root -p
# echo "SELECT * FROM dreamteam_db" | mysql 
# --enter admin password
# CREATE USER 'dt_admin'@'localhost' IDENTIFIED BY 'dt2016';
# CREATE DATABASE dreamteam_db;
# GRANT ALL PRIVILEGES ON dreamteam_db . * TO 'dt_admin'@'localhost';

mysql -u root -p << EOF
CREATE USER 'dt_admin'@'localhost' IDENTIFIED BY 'dt2016';
CREATE DATABASE dreamteam_db;
GRANT ALL PRIVILEGES ON dreamteam_db . * TO 'dt_admin'@'localhost';
EOF



pip install -r requirements.txt

# set up environment variables for the Flask Appplication
export FLASK_CONFIG=development

export FLASK_APP=dream-team/run.py      
export PUBLISHABLE_KEY=pk_test_6pRNASCoBOKtIshFeQd4XMUh 
export SECRET_KEY=sk_test_BQokikJOvBiI2HlWgH4olfQ2 
flask db migrate
flask db upgrade

