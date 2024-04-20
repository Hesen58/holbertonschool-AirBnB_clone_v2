#!/usr/bin/python3
'''Something useful'''
from flask import Flask
from flask import render_template

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


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def func4(text="is cool"):
    return f"Python {text.replace('_', ' ')}"


@app.route("/number/<int:n>", strict_slashes=False)
def func5(n):
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def func6(n):
    return render_template('5-number.html', n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def func7(n):
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
