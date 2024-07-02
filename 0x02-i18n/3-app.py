#!/usr/bin/env python3
"""
to parametrize the templates
"""

from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)

class Config:
    """
    to config class
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

app.config.from_object(Config)

def get_locale():
    """
     gets the best match with our supported languages.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])

babel = Babel()
babel.init_app(app, locale_selector=get_locale)

@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """
    for hello world
    """
    return render_template('3-index.html')

if __name__ == '__main__':
    app.run(debug=True, port=8000)

