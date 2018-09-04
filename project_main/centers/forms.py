from flask_wtf import FlaskForm
from wtforms import (StringField, IntegerField, DateTimeField, BooleanField,
                     RadioField, SelectField, TextField, TextAreaField, SubmitField)

class AddForm(FlaskForm):
    name = StringField("Center name")
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
