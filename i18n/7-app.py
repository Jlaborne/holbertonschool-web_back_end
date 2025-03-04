#!/usr/bin/env python3
"""API Basic Flask app with Babel, locale selection, and user login simulation
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Dict, Optional
import pytz
from pytz.exceptions import UnknownTimeZoneError


class Config:
    """Define the Config class for Babel translation"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)

# Mock user database
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Optional[Dict]:
    """Retrieve a user from the mock database based on the 'login_as'
        URL parameter.
    """
    try:
        user_id = int(request.args.get('login_as', ''))
        return users.get(user_id)
    except (TypeError, ValueError):
        return None


@app.before_request
def before_request() -> None:
    """Set the user on Flask's global object 'g' before each request."""
    g.user = get_user()


def get_locale() -> Optional[str]:
    """Determine the best match with our supported languages or use locale
        parameter from URL.
    """
    # Check if 'locale' parameter is present in the query string
    locale_param = request.args.get('locale')
    if locale_param in app.config['LANGUAGES']:
        return locale_param

    # Check the user's preferred locale if a user is logged in
    if g.user and g.user.get('locale') in app.config['LANGUAGES']:
        return g.user['locale']

    # Otherwise, return the best match based on the browser's accepted lang..
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_timezone() -> str:
    """Determine the best match for the timezone or use timezone parameter
        from URL.
    """
    # Check if 'timezone' parameter is present in the query string
    timezone_param = request.args.get('timezone')
    if timezone_param:
        try:
            return str(pytz.timezone(timezone_param))
        except UnknownTimeZoneError:
            pass

    # Check the user's preferred timezone if a user is logged in
    if g.user:
        user_timezone = g.user.get('timezone')
        if user_timezone:
            try:
                return str(pytz.timezone(user_timezone))
            except UnknownTimeZoneError:
                pass

    # Default to the application's default timezone
    return app.config['BABEL_DEFAULT_TIMEZONE']


babel = Babel(app, locale_selector=get_locale, timezone_selector=get_timezone)


@app.route('/')
def index() -> str:
    """Return the homepage index when the application startup"""
    return render_template('7-index.html')


if __name__ == '__main__':
    app.run()
