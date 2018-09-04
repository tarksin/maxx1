import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

Migrate(app, db)


class Center(db.Model):
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
    # ONE TO MANY
    # One ResearchCenter has many Staff
    staffers = db.relationship('Staffer', backref='center', lazy='dynamic')

    def __init__(self, name, director, url, primary_field, budget, mission, img, undergrad_research):
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

    def report_staffers(self):
        print("Staff:")
        for staffer in self.staffers:
            print(staffer.first_name, staffer.last_name)

# ------------------------------------------

class Staffer(db.Model):  #  One Staffer has One ResearchCenter
    __tablename__ = 'staffers'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.Text)
    last_name = db.Column(db.Text)
    degree = db.Column(db.Text)  #PhD
    title = db.Column(db.Text)  #Ingrid Pfeiffer Prof of Inveterate Obstinacy
    role = db.Column(db.Text)   #Director
    #  ONE TO MANY   One Staffer has many Projects
    center_id = db.Column(db.Integer, db.ForeignKey('centers.id'))
    projects = db.relationship('Project', backref='staffer', lazy='dynamic')

    def __init__(self, first_name, last_name, degree, title, role, center_id):
        self.first_name = first_name
        self.last_name = last_name
        self.degree = degree
        self.title = title
        self.role = role
        self.center_id = center_id

    def __repr__(self):
        return ("id={} first_name={} last_name={} degree={} title={} role={} center_id={}\n".format(
            {self.id}, {self.first_name}, {self.last_name}, {self.degree}, {self.title}, {self.role}, {self.center_id}))

    # def report_projects(self):
    #     print("Projects:")
    #     for project in self.projects:
    #         print(project.project_name)


# ------------------------------------------

class Project(db.Model):
    __tablename__ = 'projects'

    id = db.Column(db.Integer, primary_key=True)
    project_name = db.Column(db.Text)
    staffer_id = db.Column(db.Integer, db.ForeignKey('staffers.id'))
    # staffer_id   many-to-one link to Staff   i.e, each staffer has multiple projects.  yeah, yeah....

    def __init__(self, project_name, staffer_id ):
        self.project_name = project_name
        self.staffer_id = staffer_id

    def __repr__(self):
        return "id={} project_name={} staffer_id={}\n".format({self.id}, {self.project_name}, {self.staffer_id})
