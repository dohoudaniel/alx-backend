#!/usr/bin/env python3
"""A simple flask app
"""


# Import statements
from flask import Flask, render_template, request, g
from flask_babel import Babel
from pytz import timezone
import pytz.exceptions


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


# Users' data
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """
    Returns a user
    """
    login_id = request.args.get('login_as')
    if login_id:
        return users.get(int(login_id))
    return None


@app.before_request
def before_request() -> None:
    """
    Handling requests
    """
    user = get_user()
    g.user = user


@babel.localeselector
def get_locale():
    """
    A translation function
    """
    # Locale from URL parameters
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale

    # Locale from user settings
    if g.user:
        locale = g.user.get('locale')
        if locale and locale in app.config['LANGUAGES']:
            return locale

    # ocale from request header
    locale = request.headers.get('locale', None)
    if locale in app.config['LANGUAGES']:
        return locale

        # Default locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])

# babel.init_app(app, locale_selector=get_locale)


@babel.timezoneselector
def get_timezone():
    """
    Select and return appropriate timezone
    """
    # Find timezone parameter in URL parameters
    tzone = request.args.get('timezone', None)
    if tzone:
        try:
            return timezone(tzone).zone
        except pytz.exceptions.UnknownTimeZoneError:
            pass

    # Find time zone from user settings
    if g.user:
        try:
            tzone = g.user.get('timezone')
            return timezone(tzone).zone
        except pytz.exceptions.UnknownTimeZoneError:
            pass

    # Default to UTC
    default_tz = app.config['BABEL_DEFAULT_TIMEZONE']
    return default_tz


@app.route('/')
def home_page():
    """
    Rendering the home page
    """
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(debug=True)
