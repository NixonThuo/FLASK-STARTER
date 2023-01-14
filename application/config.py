from urllib.parse import quote_plus as urlquote


class Config(object):
    HOST = "localhost"
    PORT = "3306"
    SECRET_KEY = "randomstuff"
    DBUSERNAME = "root"
    RAW_PASS = r'fiverr@2030'
    DBPASSWORD = urlquote(RAW_PASS)
    DBNAME = "policy_bot"
    SQLALCHEMY_DATABASE_URI = "mysql://{}:{}@{}:{}/{}".format(
        DBUSERNAME, DBPASSWORD, HOST, PORT, DBNAME)
    SQLALCHEMY_ENGINE_OPTIONS = {
        'pool_pre_ping': True,
        'echo_pool': True
    }
    SQLALCHEMY_BINDS = {
        'policy': SQLALCHEMY_DATABASE_URI
    }
    WTF_CSRF_ENABLED = False


class ProductionConfig(Config):
    pass


class TestingConfig(Config):
    pass


class DevelopmentConfig(Config):
    pass
