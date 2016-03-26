# coding: utf-8
from flask import app

__author__ = 'Harald Floor Wilhelmsen'

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello World'