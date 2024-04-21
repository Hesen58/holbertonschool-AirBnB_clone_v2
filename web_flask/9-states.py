#!/usr/bin/python3
'''Something useful'''
from flask import Flask
from flask import render_template
from models import storage

app = Flask(__name__)
states = storage.all("State").values()
sStates = sorted(states, key=lambda a: getattr(a, "name"))
for state in sStates:
    sCities = sorted(state.cities, key=lambda b: getattr(b, "name"))


@app.route("/states", strict_slashes=False)
def func1():
    return render_template('7-states_list.html', sortobjs=sStates)


@app.route("/states/<id>", strict_slashes=False)
def func2(id):
    states = storage.all("State").values()
    sStates = sorted(states, key=lambda a: getattr(a, "name"))
    for state in sStates:
        sCities = sorted(state.cities, key=lambda b: getattr(b, "name"))
        if getattr(state, "id") == id:
            return render_template('9-states.html', state=state, zor2=sCities)
    return render_template('9-states.html', state=None)


@app.teardown_appcontext
def func2(app):
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
