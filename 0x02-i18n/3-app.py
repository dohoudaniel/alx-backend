#!/usr/bin/env python3
"""
A simple Flask app
"""


# Import statements
from flask import Flask, render_template, request
from flask_babel import Babel


class Config(object):
    """
    Translation class
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


# Creating the Flask app
app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale():
    """
    Function that renders the best languages
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """
    Rendering the home page
    """
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run(debug=True)
