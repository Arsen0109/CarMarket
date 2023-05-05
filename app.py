from flask import Flask, render_template, url_for
from models import Car

app = Flask(__name__)


def car_to_str(car):
    return f"{car.car_id} {car.make} {car.model} {car.year} {car.price} {car.image}"


@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/about')
def about_us():
    return render_template('about.html')


@app.route('/cars')
def get_cars():
    cars = Car.select()
    return render_template('cars.html', cars=cars)


@app.route('/contacts')
def contact_us():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)
