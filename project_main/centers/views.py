from flask import Blueprint, render_template, redirect, url_for
from project_main import db
from project_main.centers.forms import AddForm, DelForm
from project_main.models import Center

centers_blueprint = Blueprint('centers', __name__, template_folder='templates/centers')

@centers_blueprint.route('/add', methods=['GET', 'POST'])
def add():

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

        return redirect(url_for('centers.list'))

    return render_template('add.html', form=form)


@centers_blueprint.route('/list')
def list():
    centers = Center.query.all()
    return render_template('list.html', centers=centers)


@centers_blueprint.route('/delete', methods=['GET', 'POST'])
def delete():
    form = DelForm()

    if form.validate_on_submit():
        id = form.id.data
        center = Center.query.get(id)
        db.session.delete(center)
        db.session.commit()

        return redirect(url_for('centers.list'))

    return render_template('delete.html', form=form)
