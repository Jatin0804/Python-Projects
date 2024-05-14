from flask import Flask, render_template, redirect, url_for, jsonify, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
import csv
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
from random import randint, choice
from forms import CafeForm, Search, Update

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


# CREATE DB
class Base(DeclarativeBase):
    pass

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(self):
        dictionary = {}
        for column in self.__table__.columns:
            dictionary[column.name] = getattr(self, column.name)

        return dictionary

        # second method
        # return {column.name: getattr(self, column.name) for column in self.__table__.columns}

with app.app_context():
    db.create_all()

# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/random')
def get_random_cafe():
    all_cafes = db.session.query(Cafe).all()
    random_cafe = choice(all_cafes)
    return render_template('cafes.html', cafes=[random_cafe])


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        new_cafe = Cafe(
            name=form.cafe_name.data,
            map_url=form.map_url.data,
            img_url=form.img_url.data,
            location=form.location.data,
            has_sockets=bool(form.has_sockets.data),
            has_toilet=bool(form.has_toilet.data),
            has_wifi=bool(form.has_wifi.data),
            can_take_calls=bool(form.can_calls.data),
            seats=form.seats.data,
            coffee_price=bool(form.price.data),
        )
        db.session.add(new_cafe)
        db.session.commit()
        return redirect(url_for('cafes'))


    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    all_cafes = db.session.query(Cafe).all()
    return render_template('cafes.html', cafes=all_cafes)


@app.route('/search', methods=['GET', 'POST'])
def search():
    form = Search()
    if form.validate_on_submit():
        location = form.location.data.title()
        searched_cafes = db.session.query(
            Cafe).filter(Cafe.location == location)
        return render_template('search.html', form=form, cafes=searched_cafes)
    return render_template('search.html', form=form)


@app.route('/update', methods=['POST', 'GET', 'PATCH'])
def update():
    cafe_id = request.args.get('id')
    selected_cafe = Cafe.query.get(cafe_id)
    form = Update(
        seats=selected_cafe.seats,
        price=selected_cafe.coffee_price
    )
    if form.validate_on_submit():
        has_sockets = bool(1 if form.has_sockets.data == '✅' else 0)
        has_toilet = bool(1 if form.has_toilet.data == '✅' else 0)
        has_wifi = bool(1 if form.has_wifi.data == '✅' else 0)
        can_take_calls = bool(1 if form.can_take_calls.data == '✅' else 0)
        seats = form.seats.data
        price = form.price.data
        selected_cafe.has_sockets = has_sockets
        selected_cafe.has_toilet = has_toilet
        selected_cafe.has_wifi = has_wifi
        selected_cafe.can_take_calls = can_take_calls
        selected_cafe.seats = seats
        selected_cafe.coffee_price = price

        db.session.commit()
        return redirect(url_for('cafes'))
    return render_template('update.html', form=form)


@app.route('/delete', methods=['GET', 'DELETE'])
def delete():
    cafe_id = request.args.get('id')
    selected_cafe = Cafe.query.get(cafe_id)
    db.session.delete(selected_cafe)
    db.session.commit()
    return redirect(url_for('cafes'))


if __name__ == '__main__':
    app.run(debug=True)
