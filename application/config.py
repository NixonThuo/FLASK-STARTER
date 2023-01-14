class Config(object):
    SECRET_KEY = "veryuniquekey"


class ProductionConfig(Config):
    pass


class TestingConfig(Config):
    pass


class DevelopmentConfig(Config):
    pass
