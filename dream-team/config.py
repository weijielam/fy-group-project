# config.py

class Config(object):
    """
    Common configurations
    """

<<<<<<< HEAD
=======
=======
>>>>>>> 33deedb61cda40663a655947d1511f4b3f97f0bc
>>>>>>> dd1e907276152a7dcc68bf18daab83d733870240
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USERNAME = 'fygptest@gmail.com'
    MAIL_PASSWORD = 'admin2018'
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
<<<<<<< HEAD

=======
>>>>>>> dd1e907276152a7dcc68bf18daab83d733870240
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
