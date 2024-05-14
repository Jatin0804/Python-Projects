from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL

choices = ['✅', '❌']

class CafeForm(FlaskForm):
    cafe_name = StringField('Cafe name', validators=[DataRequired()])
    map_url = StringField('Cafe location on Google Maps', validators=[DataRequired(), URL()])
    img_url = StringField('Cafe Images', validators=[DataRequired(), URL()])
    location = StringField('Cafe location', validators=[DataRequired()])
    seats = StringField('Number of Seats', validators=[DataRequired()])
    has_toilet = SelectField("Toilet Availability", choices=choices, validators=[DataRequired()])
    can_calls = SelectField("Can take calls", choices=choices, validators=[DataRequired()])
    price = StringField('Coffee Price', validators=[DataRequired()])
    has_wifi = SelectField("Wifi Strength Rating", choices=choices, validators=[DataRequired()])
    has_sockets = SelectField("Power Socket Availability", choices=choices, validators=[DataRequired()])

    submit = SubmitField('Submit')

class Search(FlaskForm):
    location = StringField("Location", validators=[DataRequired()])
    submit = SubmitField("Search")

class Update(FlaskForm):
    has_sockets = SelectField(
        'Has Sockets', choices=choices, validators=[DataRequired()])
    has_toilet = SelectField(
        'Has Toilet', choices=choices, validators=[DataRequired()])
    has_wifi = SelectField('Has Wifi', choices=choices,
                           validators=[DataRequired()])
    can_take_calls = SelectField(
        'Can Take Calls', choices=choices, validators=[DataRequired()])
    seats = StringField('Seats', validators=[DataRequired()])
    price = StringField('Coffee Price', validators=[DataRequired()])
    submit = SubmitField("Update")