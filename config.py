import os

# C:\Users\Wayne\Documents\Coding Temple Work\Week 5\in-class
basedir = os.path.abspath(os.path.dirname(__file__))
# this code works for ANY filepath in ANY os.




# SECRET KEY
class Config:

    """
        Sets configuration variables for our Flask app here.
        Eventually will use hidden variable items - but for now,
        we'll leave them exposed in config
    """
    SECRET_KEY = "You will never guess..."
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEPLOY_DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
