import requests
from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

from dotenv import load_dotenv
from api_key import WEATHER_API_KEY

load_dotenv()

WEATHER_API_KEY = WEATHER_API_KEY
WEATHER_API_ENDPOINT = "https://api.weatherbit.io/v2.0/current"

weather_api_param = {
    "key": WEATHER_API_KEY,
    "city": ""
}

app = Flask(__name__)
Bootstrap5(app)
app.config['SECRET_KEY'] = '9JYkEfBA808helloWlSihBXox7C0sHR8g'


class SearchForm(FlaskForm):
    city = StringField(label=None, render_kw={"placeholder": "Search for a city"}, validators=[DataRequired()])
    submit = SubmitField(label="Search")


@app.route("/", methods=["GET", "POST"])
def home():
    search_form = SearchForm()
    if search_form.validate_on_submit():
        weather_api_param = {
            "key": WEATHER_API_KEY,
            "city": search_form.city.data
        }

        response = requests.get(url=WEATHER_API_ENDPOINT, params=weather_api_param)
        weather_data = response.json()


        return render_template("index.html", search_form=search_form, weather_data=weather_data)

    return render_template("index.html", search_form=search_form)


if __name__ == "__main__":
    app.run(debug=True)