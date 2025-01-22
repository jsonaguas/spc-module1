class DevelopmentConfig:
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:a3$pa202O.@localhost/mechanic_db'
    DEBUG = True
    CACHE_TYPE = "SimpleCache"


class TestingConfig:
    pass


class ProductionConfig:
    pass

