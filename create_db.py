import os.path
from config import SQLALCHEMY_DATABASE_URI
from storage_api import db

db.create_all()
