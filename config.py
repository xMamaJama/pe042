class Config:
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{yourusername}:{yourpassword}@localhost:5432/postgres'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_BLACKLIST_ENABLED = True
    JWT_BLACKLIST_TOKEN_CHECK = ['access', 'refresh']

    SECRET_KEY='super-secret-key'
    JWT_ERROR_MESSAGE_KEY = 'message'
