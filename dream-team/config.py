# config.py

class Config(object):
    """
    Common configurations
    """
<<<<<<< HEAD
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USERNAME = 'fygptest@gmail.com'
    MAIL_PASSWORD = 'admin2018'
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
=======


    app.config['MAIL_SERVER']='smtp.gmail.com'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USERNAME'] = 'fygptest@gmail.com'
    app.config['MAIL_PASSWORD'] = 'admin2018'
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USE_SSL'] = True

>>>>>>> def3878ebec906fc666c0c8dd1f00b5f59155842
    # Put any configurations here that are common across all environments

class DevelopmentConfig(Config):
    """
    Development configurations
    """

    DEBUG = True
    SQLALCHEMY_ECHO = True

class ProductionConfig(Config):
    """
    Production configurations
    """

    DEBUG = False

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
