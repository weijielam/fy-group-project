# config.py

class Config(object):
    """
    Common configurations
    """

    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USERNAME = 'fygptest@gmail.com'
    MAIL_PASSWORD = 'admin2018'
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    
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
