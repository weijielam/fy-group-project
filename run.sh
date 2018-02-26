#!/bin/bash
source Envs/my-venv/bin/activate
cd dream-team
sudo pip install -r requirements.txt
export FLASK_CONFIG=development
export FLASK_APP=run.py
flask db upgrade
flask run
