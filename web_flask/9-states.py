#!/usr/bin/python3
'''Something useful'''
from flask import Flask
from flask import render_template
from models import storage

app = Flask(__name__)
states = storage.all("State").values()
zor1 = sorted(states, key=lambda a: getattr(a, "name"))
cities = storage.all("City").values()
zor2 = sorted(cities, key=lambda b: getattr(b, "name"))


@app.route("/states", strict_slashes=False)
def func1():
    return render_template('7-states_list.html', sortobjs=zor1)


@app.route("/states/<id>", strict_slashes=False)
def func2(id):
    for state in zor1:
        if state.id == id:
            return render_template('9-states.html', state=state, zor2=zor2)
    return render_template('9-states.html', state=None)


@app.teardown_appcontext
def func2(app):
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
