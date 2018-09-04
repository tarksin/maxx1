import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SECRET_KEY'] = 'ousontlesneiges'

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)

# Have to import register blueprints after db is created....

from project_main.centers.views import centers_blueprint
from project_main.staffers.views import staffers_blueprint

app.register_blueprint(centers_blueprint, url_prefix='/centers')
app.register_blueprint(staffers_blueprint, url_prefix='/staffers')
