from flask_wtf import FlaskForm
from wtforms import (StringField, IntegerField, DateTimeField, BooleanField,
                     RadioField, SelectField, TextField, TextAreaField, SubmitField)

class AddForm(FlaskForm):
    first_name = StringField("First name")
    last_name = StringField("Last name")
    degree = StringField('Academic degree')
    title = StringField('Academic title')
    role = StringField("Job role")
    center_id = IntegerField("Center ID")

    submit = SubmitField("Submit")
