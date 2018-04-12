""" Farmers Market App """


from jinja2 import StrictUndefined

from flask_debugtoolbar import DebugToolbarExtension

from flask import (Flask, render_template, redirect, request, flash, jsonify,

                   session)

from model import User, Market, Vendor, MarketVendor, connect_to_db, db

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
    return render_template(

        "market_profile.html", market=market)


@app.route('/markets/<market_id>.json')
def market_json(market_id):
    market = Market.query.get(market_id)

    market_info = {
        'address': market.market_address,
        'name': market.market_name
    }
    return jsonify(market_info)


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


@app.route('/markets.json')
def market_info():
    """JSON information about markets."""
    markets = {}

    for market in Market.query.all():
        market_data = {
            "marketId": market.market_id,
            "name": market.market_name,
            "day": market.market_day,
            "startTime": market.market_start.strftime('%I:%M %p'),
            "endTime": market.market_end.strftime('%I:%M %p'),
            "address": market.market_address
        }
        markets[market.market_name] = market_data
    return jsonify(markets)


@app.route('/vendors/<vendor_id>/json')
def vendor_info_json(vendor_id):
    """JSON information about specific vendors markets."""
    markets = {}
    vendor = Vendor.query.get(vendor_id)
    for market in vendor.markets:
        market_data = {
            "marketId": market.market_id,
            "name": market.market_name,
            "day": market.market_day,
            "startTime": market.market_start.strftime('%I:%M %p'),
            "endTime": market.market_end.strftime('%I:%M %p'),
            "address": market.market_address,
            "icon": vendor.map_icon
        }
        markets[market.market_name] = market_data
    return jsonify(markets)

if __name__ == "__main__":

    app.debug = True

    # make sure templates, etc. are not cached in debug mode

    app.jinja_env.auto_reload = app.debug

    connect_to_db(app)

    app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

    # Use the DebugToolbar

    DebugToolbarExtension(app)

    app.run(port=5000, host='0.0.0.0')
