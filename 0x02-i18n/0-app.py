#!/usr/bin/env python3
"""
A simple Flask App
"""


# Import statements
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def home_page():
    """
    Renders the Home page
    """
    return render_template('0-index.html')


# Running the Flask app
if __name__ == "__main__":
    app.run(debug=True)
