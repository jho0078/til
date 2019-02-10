import logging

from flask import Flask


app = Flask(__name__)
@app.route('/')
def index():
    return '안녕하세요'