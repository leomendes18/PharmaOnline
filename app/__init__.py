# Import flask and template operators
from flask import Flask, render_template

# Import Peewee
from config import DATABASE
from peewee import SqliteDatabase

from flask_login import LoginManager
# Define the WSGI application object
pharmaonline = Flask(__name__)

# CSRF
from flask_wtf.csrf import CSRFProtect
csrf = CSRFProtect()
csrf.init_app(pharmaonline)


# Configurations
pharmaonline.config.from_object('config')


# Define the database object which is imported
# by modules and controllers
db = SqliteDatabase(DATABASE)
login_manager = LoginManager()
login_manager.init_app(pharmaonline)

# Database:
from app.models.tables import *

# This will create the database file
db.connect()
db.create_tables([User, Medicamento])
db.close
#import sqlite3
#conn = sqlite3.connect(DATABASE)


from app.controllers import views
print("aki1")