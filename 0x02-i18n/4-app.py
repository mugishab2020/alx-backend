#!/usr/bin/env python3
'''This is to make the incoming request have locale in URL'''


from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


@babel.localeselector
def get_locale():
    '''get locale from request'''

    have_locale = request.args.get('locale')
    if have_locale in app.config.get['LANGUAGES']:
        return have_locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def home():
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(debug=True)
