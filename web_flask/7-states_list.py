#!/usr/bin/python3
'''Something useful'''
from flask import Flask
from flask import render_template
from models import storage

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def func1():
    objects = storage.all("State").values()
    sortobjs = sorted(objects, key=lambda a:a["name"])
    return render_template('7-states_list.html', sortobjs=sortobjs)


@app.teardown_appcontext
def func2(app):
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
