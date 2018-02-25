#!/bin/bash
source Envs/my-venv/bin/activate
cd dream-team
sudo pip install -r requirements.txt
export FLASK_CONFIG=development
export FLASK_APP=run.py
export MAIL_SERVER = 'smtp.gmail.com'
export MAIL_USERNAME = 'weijielam@gmail.com'
export MAIL_PASSWORD = 'its not really my fault'
flask db upgrade
flask run
