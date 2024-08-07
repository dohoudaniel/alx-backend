#!/usr/bin/env python3
"""
A simple Flask app
"""


# Import statements
from flask import Flask, render_template, request, g
from flask_babel import Babel


class Config(object):
    """
    A translation class
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


# Creating the Flask app
app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


# Users' data (dictionary)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """
    A function that returns a user
    """
    login_id = request.args.get('login_as')
    if login_id:
        return users.get(int(login_id))
    return None


@app.before_request
def before_request() -> None:
    """
    A function that sets the user
    """
    user = get_user()
    g.user = user


@babel.localeselector
def get_locale():
    """
    A translation function
    """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        print(locale)
        return locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])
# babel.init_app(app, locale_selector=get_locale)


@app.route('/')
def home_page():
    """
    Rendering the home page
    """
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(debug=True)
