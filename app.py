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

@app.route('/us')
def us():
    return render_template('us.html')

@app.route('/global')
def global_page():
    return render_template('global.html')

@app.route('/predict')
def predict():
    return render_template('predict.html')

@app.route('/mobility')
def mobility():
    return render_template('mobility.html')

@app.route('/test')
def test():
    return render_template('test.html')

if __name__ == "__main__":
    app.run(debug=True)
