#!/usr/bin/env python

import requests
from flask import Flask, render_template, request, url_for, redirect
from flask.ext.sqlalchemy import SQLAlchemy

from config import config

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy( app )


@app.route('/')
def home():
    #home page
    return render_template("home.html")

@app.route('/working')
def serverTest():
    #testing and debug page
    return render_template("working.html")


if __name__ == '__main__':
    app.run()
