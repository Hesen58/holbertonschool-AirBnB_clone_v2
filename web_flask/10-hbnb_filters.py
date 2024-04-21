#!/usr/bin/python3
'''Something useful'''
from flask import Flask
from flask import render_template
from models import storage

app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def func1():
    states = storage.all("State").values()
    sStates = sorted(states, key=lambda a: getattr(a, "name"))
    cities = storage.all("City").values()
    sCities = sorted(cities, key=lambda b: getattr(b, "name"))
    amenities = storage.all("Amenity").values()
    sAmenities = sorted(amenities, key=lambda c: getattr(c, "name"))
    return render_template('10-hbnb_filters.html', states=sStates, cities=sCities, amenities=sAmenities)


@app.teardown_appcontext
def func2(app):
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
