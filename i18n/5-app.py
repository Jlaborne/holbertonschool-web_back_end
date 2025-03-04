#!/usr/bin/env python3
"""
Flask app with Babel, forced locale, and mock login system.

This application supports language selection via URL parameters and mocks user authentication.
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, _


class Config:
    """
    Configuration class for Flask app.

    Attributes:
        LANGUAGES (list): List of supported languages.
        BABEL_DEFAULT_LOCALE (str): Default locale set to English.
        BABEL_DEFAULT_TIMEZONE (str): Default timezone set to UTC.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel()

# Mock user database
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> dict | None:
    """
    Retrieve user information based on the `login_as` parameter.

    Returns:
        dict | None: User dictionary if found, otherwise None.
    """
    user_id = request.args.get("login_as")
    if user_id and user_id.isdigit():
        return users.get(int(user_id))
    return None


@app.before_request
def before_request() -> None:
    """
    Executed before handling any request.

    If `login_as` is provided in the URL, retrieve the user and store it in `g.user`.
    """
    g.user = get_user()


def get_locale() -> str:
    """
    Determine the best match for supported languages.

    - If a `locale` query parameter is present and valid, use it.
    - Otherwise, use the best match from the request's `Accept-Language` headers.

    Returns:
        str: The chosen locale.
    """
    locale = request.args.get("locale")
    if locale and locale in app.config["LANGUAGES"]:
        return locale

    # If the user is logged in, use their locale preference if available
    if g.get("user") and g.user.get("locale") in app.config["LANGUAGES"]:
        return g.user["locale"]

    return request.accept_languages.best_match(app.config["LANGUAGES"])


babel.init_app(app, locale_selector=get_locale)


@app.route('/')
def index() -> str:
    """
    Render the homepage with translated content.

    Returns:
        str: Rendered HTML template.
    """
    return render_template('5-index.html')


@app.context_processor
def inject_locale() -> dict:
    """
    Make `get_locale` function available inside Jinja templates.

    Returns:
        dict: Dictionary containing the `get_locale` function.
    """
    return {"get_locale": get_locale}


if __name__ == '__main__':
    app.run()
