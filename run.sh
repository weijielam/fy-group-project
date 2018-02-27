source Envs/my-venv/bin/activate
sudo pip install -r requirements.txt

export FLASK_CONFIG=development
export FLASK_APP=dream-team/run.py
flask db upgrade

flask run
