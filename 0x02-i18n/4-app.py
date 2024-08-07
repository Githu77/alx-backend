#!/usr/bin/env python3
"""
to force the locale with URL parameter
"""


from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


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
    check the request contains locale
    argument and ifs value is a supported locale, return it
    """
    locale = request.args.get('locale')
    if locale:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])

babel = Babel()
babel.init_app(app, locale_selector=get_locale)

@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """
    for hello world
    """
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(debug=True, port=8000)
