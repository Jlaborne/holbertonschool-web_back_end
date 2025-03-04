#!/usr/bin/env python3
"""
Flask app with Babel and forced locale via URL parameter.

This application allows users to specify a locale using a URL parameter (?locale=fr or ?locale=en).
If the locale is not provided or is unsupported, it defaults to the best match from the request headers.
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

    - If a `locale` query parameter is present and valid, use it.
    - Otherwise, use the best match from the request's `Accept-Language` headers.

    Returns:
        str: The chosen locale.
    """
    locale = request.args.get('locale')
    if locale and locale in app.config["LANGUAGES"]:
        return locale  # Force locale via URL parameter

    return request.accept_languages.best_match(app.config["LANGUAGES"])


babel.init_app(app, locale_selector=get_locale)


@app.route('/')
def index() -> str:
    """
    Render the homepage with translated content.

    Returns:
        str: Rendered HTML template.
    """
    return render_template('4-index.html')


@app.context_processor
def inject_locale() -> dict:
    """
    Make `get_locale` function available inside Jinja templates.

    Returns:
        dict: Dictionary containing the `get_locale` function.
    """
    return {"get_locale": get_locale}


if __name__ == '__main__':
    app.run(debug=True)
