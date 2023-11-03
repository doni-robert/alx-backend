#!/usr/bin/env python3
"""Basic Babel setup"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, format_datetime
from pytz import timezone
import pytz
from typing import Union, Dict


class Config(object):
    """
    Config class
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@babel.localeselector
def get_locale() -> str:
    """
    Gets the locale
    """
    locale = None
    if request.args.get('locale'):
        locale = request.args.get('locale')
    elif request.args.get('login_as'):
        locale = (get_user()).get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user() -> Union[Dict, None]:
    """
    Retrieves a user
    """
    user_id = request.args.get('login_as')
    if user_id:
        return users.get(int(user_id))
    return None


@app.before_request
def before_request() -> None:
    """
    Gets and sets the user as a global
    """
    user = get_user()
    if user:
        g.user = user


@babel.timezoneselector
def get_timezone() -> str:
    """
    Retrieves the timezone
    """
    tz = None
    if request.args.get('timezone'):
        tz = request.args.get('timezone')
    elif request.args.get('login_as'):
        tz = (get_user()).get('timezone')
    try:
        return timezone(tz).zone
    except pytz.exceptions.UnknownTimeZoneError:
        return app.config['BABEL_DEFAULT_TIMEZONE']


@app.route("/")
def hello_world() -> str:
    """
    Renders 0-index.html
    """
    g.time = format_datetime()
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
