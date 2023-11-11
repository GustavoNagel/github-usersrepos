"""App configurations."""


class Config:
    DEBUG = True
    TESTING = True
    MONGO_URI = "mongodb://myuser:mypassword@mongodb:27017/test?authSource=admin"
