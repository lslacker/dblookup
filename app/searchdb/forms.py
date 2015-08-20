__author__ = 'LMai'
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, InputRequired, Length


class SearchForm(Form):
    query = StringField('Search', validators=[InputRequired(), Length(3, 20)])
