#!/usr/bin/python3
'''Something useful'''
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def func1():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def func2():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def func3(text):
    return f"C {text.replace('_', ' ')}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)