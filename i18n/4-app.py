#!/usr/bin/env python3
"""API Basic Flask app with Babel and locale selection with URL parameter"""
from flask import Flask, render_template, request
from flask_babel import Babel, get_locale


class Config():
    """Define the Config class for Babel translation"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)


def get_locale() -> str:
    """Determine the best match with our supported languages or
        use locale parameter from URL.
    """
    # Check if 'locale' parameter is present in the query string
    locale_param = request.args.get('locale')

    # If 'locale' is present and is a supported language, return it
    if locale_param in app.config['LANGUAGES']:
        return locale_param

    # Otherwise, return the best match based on the browser's accepted lang.
    return request.accept_languages.best_match(app.config['LANGUAGES'])


babel = Babel(app, locale_selector=get_locale)


@app.route('/')
def index() -> str:
    """Return the homepage index when the application startup"""
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run()
