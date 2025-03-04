#!/usr/bin/env python3
"""
Flask app with Babel and template translation.

This application sets up a simple web page with internationalization support
using Flask-Babel. It determines the locale based on the request headers
and renders the page with the appropriate translations.
"""

from flask import Flask, render_template, request
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


def get_locale() -> str:
    """
    Determine the best match for supported languages.

    Returns:
        str: The best match locale based on the request.
    """
    return request.accept_languages.best_match(app.config["LANGUAGES"])


babel.init_app(app, locale_selector=get_locale)


@app.route('/')
def index() -> str:
    """
    Render the homepage.

    Returns:
        str: Rendered HTML template.
    """
    return render_template('3-index.html')


@app.context_processor
def inject_locale() -> dict:
    """
    Make the `get_locale` function available inside Jinja templates.

    Returns:
        dict: Dictionary containing the `get_locale` function.
    """
    return {"get_locale": get_locale}


if __name__ == '__main__':
    app.run(debug=True)
