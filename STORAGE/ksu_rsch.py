# ksu_rsch.py
import os
from forms import AddForm, DelForm, AddStaffForm
from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SECRET_KEY'] = 'ousontlesneiges'

# #####################
# SQLite
# ####################

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)

# #####################
#  Models
# #####################


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
    undergrad = db.Column(db.Boolean)
#      ONE TO MANY
#    staffers = db.relationship('Staffer', backref='center', lazy=True)

    def __init__(self, name, director, url, primary_field, budget, mission, img, undergrad):
        self.name = name
        self.director = director
        self.url = url
        self.primary_field = primary_field
        self.budget = budget
        self.mission = mission
        self.img = img
        self.undergrad = undergrad

    def __repr__(self):
        return ("id={} name={} director={} url={} primary_field={} budget={} undergrad_research={}\n".format(
            {self.id}, {self.name}, {self.director}, {self.url}, {self.primary_field}, {self.budget}, {self.img},
            {self.undergrad}))

    # def list_staff(self):
    #     print("Staff:")
    #     for staffer in self.staffers:
    #         print(staffer.first_name)

    # def get_staffers(self):
    #     the_staffers = []
    #     for staffer in self.staffers:
    #         the_staffers.append(staffer)
    #     return the_staffers


# ##################################################################
class Staffer(db.Model):  #  One Staffer has One ResearchCenter
    __tablename__ = 'staffers'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.Text)
    last_name = db.Column(db.Text)
    degree = db.Column(db.Text)  #PhD
    title = db.Column(db.Text)   #Ingrid Pfeiffer Prof of Inveterate Obstinacy
    role = db.Column(db.Text)    #Director
    center_id = db.Column(db.Integer, db.ForeignKey('centers.id'))
    center = db.relationship('Center', backref='staffers', lazy=True)


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




######################
# View functions
######################


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add', methods=['GET', 'POST'])
def add_center():

    form = AddForm()

    if form.validate_on_submit():
        name = form.name.data
        director = form.director.data
        url = form.url.data
        primary_field = form.primary_field.data
        budget = form.budget.data
        mission = form.mission.data
        img = form.img.data
        undergrad = form.undergrad.data

        new_center = Center(name, director, url, primary_field, budget, mission, img, undergrad)
        db.session.add(new_center)
        db.session.commit()

        return redirect(url_for('list_centers'))

    return render_template('add.html', form=form)

@app.route('/center/<id>')
def center(id):

    the_center = Center.query.get(id)
    return render_template('center.html', center=the_center)



@app.route('/list_centers')
def list_centers():

    centers = Center.query.all()
    return render_template('list_centers.html', centers=centers)


@app.route('/delete', methods=['GET', 'POST'])
def del_center():

    form = DelForm()

    if form.validate_on_submit():
        id = form.id.data
        center = Center.query.get(id)
        db.session.delete(center)
        db.session.commit()

        return redirect(url_for('list_centers'))

    return render_template('delete.html', form=form)



@app.route('/add_staff', methods=['GET', 'POST'])
def add_staff():

    form = AddStaffForm()

    if form.validate_on_submit():
        center_id = form.center_id.data
        first_name = form.first_name.data
        last_name = form.last_name.data
        degree = form.degree.data
        title = form.title.data
        role = form.role.data

        new_staffer = Staffer(first_name, last_name, degree, title, role, center_id)
        db.session.add(new_staffer)
        db.session.commit()

        return redirect(url_for('list_staffers'))

    return render_template('add_staff.html', form=form)


@app.route('/list_staffers')
def list_staffers():

    staffers = Staffer.query.all()

    return render_template('list_staffers.html', staffers=staffers)


if __name__ == "__main__":
    app.run(debug=True)

















