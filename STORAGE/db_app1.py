import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate  # pip3 install Flask-Migrate --user

basedir = os.path.abspath(os.path.dirname(__file__))
# /home/tark/repos/maxx1
print('basedir is : {}'.format(basedir))


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

Migrate(app, db)  # This enables terminal commands to d/b

###################################

class ResearchCenter(db.Model):
    __tablename__ = 'centers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    director = db.Column(db.Text)
    url = db.Column(db.Text)
    primary_field = db.Column(db.Text)
    budget = db.Column(db.Text)
    mission = db.Column(db.Text)
    img = db.Column(db.Text)
    undergrad_research = db.Column(db.Boolean)

    def __init__(self, name, director, url, primary_field, budget, mission, img, undergrad_research ):
        self.name = name
        self.director = director
        self.url = url
        self.primary_field = primary_field
        self.budget = budget
        self.mission = mission
        self.img = img
        self.undergrad_research = undergrad_research

    def __repr__(self):
        return ("id={} name={} director={} url={} primary_field={} budget={} undergrad_research={}\n".format(
            {self.id}, {self.name}, {self.director}, {self.url}, {self.primary_field}, {self.budget}, {self.img},
            {self.undergrad_research}))