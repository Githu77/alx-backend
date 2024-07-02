#!/usr/bin/env python3
"""
to use user locale
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel
import pytz

app = Flask(__name__)

class Config:
    """
    to configure class
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app.config.from_object(Config)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

def get_user(login_as):
    """
    to get_user
    """
    try:
        return users.get(int(login_as))
    except Exception:
        return

@app.before_request
def before_request():
    """
    before request
    """
    g.user = get_user(request.args.get("login_as"))

def get_locale():
    """
    to get_locale
    """
    locale = request.args.get("locale")
    if locale:
        return locale
    user = g.user
    if user:
        lang = user.get('locale')
        if lang in app.config['LANGUAGES']:
            return lang
    headers = request.headers.get('locale')
    if headers:
        return headers
    return request.accept_languages.best_match(app.config['LANGUAGES'])

def get_timezone():
    """
    to get_timezone
    """
    try:
        timezone = request.args.get("timezone")
        if timezone:
            return pytz.timezone(timezone)
        user = g.user
        if user:
            timezone = user.get('timezone')
            if timezone:
                return pytz.timezone(timezone)
        timezone = request.headers.get("timezone")
        if timezone:
            return pytz.timezone(timezone)
    except pytz.UnknownTimeZoneError:
        return app.config.get('BABEL_DEFAULT_TIMEZONE')
    return app.config.get('BABEL_DEFAULT_TIMEZONE')

babel = Babel()
babel.init_app(app, locale_selector=get_locale, timezone_selector=get_timezone)

@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """
    for hello world
    """
    return render_template('7-index.html')

if __name__ == '__main__':
    app.run(debug=True, port=8000)

