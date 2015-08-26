__author__ = 'LMai'
from flask_wtf import Form
from wtforms import StringField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, InputRequired, Length


class SearchForm(Form):
    server = StringField('Server', validators=[InputRequired(), Length(5, 35)])
    databases = StringField('Databases', validators=[InputRequired(), Length(5, 45)])
    query = StringField('Search', validators=[InputRequired(), Length(5, 35)])
    containing_text = BooleanField('Containing text')

