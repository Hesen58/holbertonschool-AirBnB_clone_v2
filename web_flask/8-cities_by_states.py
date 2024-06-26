#!/usr/bin/python3
'''Something useful'''
from flask import Flask
from flask import render_template
from models import storage

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def func1():
    states = storage.all("State").values()
    zor1 = sorted(states, key=lambda a: getattr(a, "name"))
    cities = storage.all("City").values()
    zor2 = sorted(cities, key=lambda b: getattr(b, "name"))
    return render_template('8-cities_by_states.html', zor1=zor1, zor2=zor2)


@app.teardown_appcontext
def func2(app):
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
