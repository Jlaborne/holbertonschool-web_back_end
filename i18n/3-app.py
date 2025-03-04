#!/usr/bin/env python3
"""API Basic Flask app with Babel and locale selection"""
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
    """Determine the best match with our supported languages."""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


babel = Babel(app, locale_selector=get_locale)


@app.route('/')
def index() -> str:
    """Return the homepage index when the application startup"""
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run()
