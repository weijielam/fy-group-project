source Envs/my-venv/bin/activate
sudo pip install -r requirements.txt




export FLASK_APP=dream-team/run.py
export FLASK_CONFIG=development
# flask db init
flask db migrate
flask db upgrade

PUBLISHABLE_KEY=pk_test_6pRNASCoBOKtIshFeQd4XMUh SECRET_KEY=sk_test_BQokikJOvBiI2HlWgH4olfQ2 flask run
