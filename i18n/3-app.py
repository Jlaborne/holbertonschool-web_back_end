#!/usr/bin/env python3
"""
Flask app with Babel and template translation
"""
from flask import Flask, render_template, request
from flask_babel import Babel, _


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
    return render_template('3-index.html')


@app.context_processor
def inject_locale():
    """Determine the best match for supported lang"""
    return {"get_locale": get_locale}


if __name__ == '__main__':
    app.run(debug=True)
