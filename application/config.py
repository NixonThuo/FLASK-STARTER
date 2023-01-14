class Config(object):
    HOST = "localhost"
    PORT = "3306"
    SECRET_KEY = "randomstuff"
    DBUSERNAME = "root"
    DBPASSWORD = "fiverr@2030"
    DBNAME = "policy_bot"
    SQLALCHEMY_DATABASE_URI = "mysql://{}:{}@{}:{}/{}".format(
        DBUSERNAME, DBPASSWORD, HOST, PORT, DBNAME)
    WTF_CSRF_ENABLED = False


class ProductionConfig(Config):
    pass


class TestingConfig(Config):
    pass


class DevelopmentConfig(Config):
    pass
