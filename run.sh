source Envs/my-venv/bin/activate        # Activate virtualenv
sudo pip install -r requirements.txt    # Install pip libraries


export FLASK_APP=dream-team/run.py      # set up environment variables for the Flask Appplication
export FLASK_CONFIG=development

flask db migrate                        # update database
flask db upgrade                        # 

PUBLISHABLE_KEY=pk_test_6pRNASCoBOKtIshFeQd4XMUh SECRET_KEY=sk_test_BQokikJOvBiI2HlWgH4olfQ2 flask run
