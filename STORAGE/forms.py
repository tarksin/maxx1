# forms.py
from flask_wtf import FlaskForm
from wtforms import (StringField, IntegerField, DateTimeField, BooleanField,
                     RadioField, SelectField, TextField, TextAreaField, SubmitField)
from wtforms.validators import DataRequired


class AddForm(FlaskForm):
    name = StringField("Center name", validators=[DataRequired()])
    director = StringField("Director")
    undergrad = BooleanField('Undergraduate research')
    primary_field = SelectField(u'Primary research field:',
                              choices=[('bio', 'Biology'), ('chm', 'Chemistry'), ('eng', 'Engineering'), ('csi', 'Computer Science'), ('vet', 'Veterinary Medicine')])
    budget = StringField("Annual budget")    # staff, operations, facilities
    mission = TextAreaField("Mission Statement")
    img = StringField("Image")
    url = StringField("link")

    submit = SubmitField("Submit")


class DelForm(FlaskForm):

    id = IntegerField("id of Center to remove")
    submit = SubmitField("Remove Center")


class AddStaffForm(FlaskForm):
    first_name = StringField("First name", validators=[DataRequired()])
    last_name = StringField("Last name", validators=[DataRequired()])
    degree = StringField('Academic degree')
    title = StringField('Academic title')
    role = StringField("Job role")
    center_id = IntegerField("Center ID")

    submit = SubmitField("Submit")

