""" Farmers Market App """


from jinja2 import StrictUndefined

from flask import Flask

from flask_debugtoolbar import DebugToolbarExtension

from model import connect_to_db, db

from flask import (Flask, render_template, redirect, request, flash,

                   session)

from model import User, Market, Vendor, Address, MarketVendor, connect_to_db, db

app = Flask(__name__)

app.secret_key = "FARMLYF"

app.jinja_env.undefined = StrictUndefined


@app.route('/')
def homepage():

    """Homepage."""

    return render_template("homepage.html")


@app.route('/markets')
def display_markets():
    """ Display all markets """

    markets = Market.query.all()

    return render_template("markets.html", markets=markets)


@app.route('/markets/<market_id>/')
def market_profile(market_id):

    """Show info about Market. """

    market = Market.query.get(market_id)
    address = market.address_id
    location = Address.query.get(address)
    street = location.address_street
    city = location.address_city
    state = location.address_state

    return render_template(

        "market_profile.html", market=market, street=street, city=city, state=state)


@app.route('/vendors')
def display_vendors():
    """ Display all vendors """

    vendors = Vendor.query.all()

    return render_template("vendors.html", vendors=vendors)


@app.route('/vendors/<vendor_id>/')
def vendor_profile(vendor_id):

    """Show info about Vendor. """

    vendor = Vendor.query.get(vendor_id)
    #FIND ALL MARKETS FOR VENDOR

    return render_template(

        "vendor_profile.html", vendor=vendor)

if __name__ == "__main__":

    app.debug = True

    # make sure templates, etc. are not cached in debug mode

    app.jinja_env.auto_reload = app.debug

    connect_to_db(app)

    app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

    # Use the DebugToolbar

    DebugToolbarExtension(app)

    app.run(port=5000, host='0.0.0.0')
