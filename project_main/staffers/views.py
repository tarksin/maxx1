from flask import Blueprint, render_template, redirect, url_for
from project_main import db
from project_main.models import Staffer
from project_main.staffers.forms import AddForm

staffers_blueprint = Blueprint('staffers', __name__, template_folder='templates/staffers')


@staffers_blueprint.route('/add', methods=['GET', 'POST'])
def add():

    form = AddForm()

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

        return redirect(url_for('staffers.list'))

    return render_template('add_staffer.html', form=form)


@staffers_blueprint.route('/list')
def list():
    staffers = Staffer.query.all()
    return render_template('list_staffers.html', staffers=staffers)
