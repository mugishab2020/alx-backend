#!/usr/bin/env python3.7
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    '''this is the index page'''
    return render_template('9-number.html')


if __name__ == '__main__':
    app.run(debug=True)
