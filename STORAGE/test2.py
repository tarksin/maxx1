from flask import Flask, render_template, session, flash, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import (StringField, SubmitField, DateTimeField, BooleanField, RadioField,
                     SelectField, TextField,TextAreaField, SubmitField)
from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY'] = 'ousontlesneiges'


class InfoForm(FlaskForm):
    center_name = StringField("Center name", validators=[DataRequired()])
    director = StringField("Director")
    undergrad = BooleanField('Undergraduate research')
    prime_field = SelectField(u'Primary research field:',
                              choices=[('bio', 'Biology'), ('chm', 'Chemistry'), ('eng', 'Engineering'), ('csi', 'Computer Science'), ('vet', 'Veterinary Medicine')])
    budget = StringField("Annual budget")    # staff, operations, facilities
    funds_source = RadioField('Primary funding source:',
                              choices=[('fed', 'federal'),
                                       ('state', 'state'),
                                       ('corp', 'corporate')
                                       ])
    mission = TextAreaField("Mission Statement")
    url = StringField("link")

    submit = SubmitField("Submit")

@app.route('/', methods=['GET', 'POST'])
def index():

    form = InfoForm()

    if form.validate_on_submit():
        flash('36 test2.py Successful creation of record for new center {}'.format(form.center_name.data))

        session['center_name'] = form.center_name.data
        session['director'] = form.director.data
        session['undergrad'] = form.undergrad.data
        session['prime_field'] = form.prime_field.data
        session['funds_source'] = form.funds_source.data
        session['budget'] = form.budget.data
        session['mission'] = form.mission.data
        session['url'] = form.url.data
#         form.center_name.data = ''
#        form.director.data = ''
#    form.undergrad.data = ''
#    form.prime_field.data = ''
#    form.budget.data = ''
#    form.funds_source.data = ''
#    form.mission.data = ''
#    form.url.data = ''

        return redirect(url_for('thankyou'))
    print(form.errors)
#
    return render_template('index.html', form=form)

@app.route('/thankyou')
def thankyou():
    # comment = ''
    # if 'PhD' in director:
    #     comment = 'Aha! A qualified academic administrator!'
    # else:
    #     comment = '(Temporarily until we find a fully academically qualified adminstrator)'
    # return render_template('thankyou.html', comment=comment)
    return render_template('thankyou.html')


if __name__ == "__main__":
    app.run(debug=True)
