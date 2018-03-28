source Envs/my-venv/bin/activate        # Activate virtualenv

export FLASK_APP=dream-team/run.py      # set up environment variables for the Flask Appplication
export FLASK_CONFIG=development

PUBLISHABLE_KEY=pk_test_6pRNASCoBOKtIshFeQd4XMUh SECRET_KEY=sk_test_BQokikJOvBiI2HlWgH4olfQ2 flask db upgrade

PUBLISHABLE_KEY=pk_test_6pRNASCoBOKtIshFeQd4XMUh SECRET_KEY=sk_test_BQokikJOvBiI2HlWgH4olfQ2 flask run
