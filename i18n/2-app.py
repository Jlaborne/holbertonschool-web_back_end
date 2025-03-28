#!/usr/bin/env python3
"""
Flask app with Babel and locale selection
"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """Configuration class for Flask app"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel()


def get_locale():
    """Determine the best match for supported languages"""
    return request.accept_languages.best_match(app.config["LANGUAGES"])


babel.init_app(app, locale_selector=get_locale)


@app.route('/')
def index():
    """Renders the homepage"""
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(debug=True)
