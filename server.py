""" Farmers Market App """


from jinja2 import StrictUndefined

from flask import Flask

from flask_debugtoolbar import DebugToolbarExtension

from model import connect_to_db, db

from flask import (Flask, render_template, redirect, request, flash,

                   session)

#from model import User, Market, Vendor, connect_to_db, db

app = Flask(__name__)

app.secret_key = "FARMLYF"

app.jinja_env.undefined = StrictUndefined


@app.route('/')
def homepage():

    """Homepage."""

    return render_template("homepage.html")


if __name__ == "__main__":

    app.debug = True

    # make sure templates, etc. are not cached in debug mode

    app.jinja_env.auto_reload = app.debug

    connect_to_db(app)

    app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

    # Use the DebugToolbar

    DebugToolbarExtension(app)

    app.run(port=5000, host='0.0.0.0')
