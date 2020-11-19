"""Web app"""
import flask
from flask import Flask, render_template, request, redirect, url_for

import pickle
import base64
# from training import prediction
# import requests
app = flask.Flask(__name__)

model = pickle.load(open("model.pickle", 'rb'))

@app.route("/")
def index() -> str:
    """Base page."""
    return flask.render_template("index.html")

@app.route('/livemap')
def livemap():
    return render_template('livemap.html')

@app.route('/plot')
def plot():
    return render_template('plot.html')

@app.route('/predict')
def predict():
    return render_template('predict.html')

@app.route('/analysis')
def analysis():
    return render_template('analysis.html')

@app.route('/test')
def test():
    return render_template('test.html')

if __name__ == "__main__":
    app.run(debug=True)
