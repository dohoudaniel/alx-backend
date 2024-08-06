#!/usr/bin/env python3
"""
A simple Flask app
"""


from flask import Flask, render_template
from flask_babel import Babel


class Config(object):
    """
    Configuring available languages
    for our app, and setting some defaults
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


# Creating the Flask app
app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def home_page():
    """
    Rendering the home page
    """
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run(debug=True)
