#!/usr/bin/env python3
"""
A simple Flask app
"""


# Import statements
from flask import Flask, render_template, request
from flask_babel import Babel


class Config(object):
    """
    A function that configures available
    languages using a babel.localeselector
    decorator
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


# Creating the Flask app
app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """
    Matching the best language
    to the requested language
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def home_page():
    """
    Rendering the home page
    """
    return render_template('2-index.html')


if __name__ == "__main__":
    app.run(debug=True)
