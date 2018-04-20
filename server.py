""" Farmers Market App """

from sqlalchemy import and_
from jinja2 import StrictUndefined
from flask_debugtoolbar import DebugToolbarExtension
from flask import (Flask, render_template, redirect, request, flash, jsonify,
                   session)
from model import User, Market, Vendor, MarketVendor, UserFavoriteMarket, UserFavoriteVendor, connect_to_db, db
import requests
from passlib.hash import sha256_crypt


app = Flask(__name__)

app.secret_key = "FARMLIFE"

app.jinja_env.undefined = StrictUndefined


@app.route('/flip')
def flip():
    return render_template('flip.html')


@app.route('/')
def homepage():

    """Homepage."""

    return render_template("homepage.html")


@app.route('/search', methods=['GET', 'POST'])
def search_results():
    """ Displays results of a vendor search"""
    search_by = request.form.get("search_by")
    keyword = request.form.get("keyword")
    days = request.form.getlist("day")
    # submit = request.form.get("submit")

    if search_by == "vendor":  # if vendor seach box was selected
        results = Vendor.query.filter(Vendor.vendor_name.ilike('%' + keyword + '%'))

    elif search_by == "market":
        if days:
            results = Market.query.filter(Market.market_day.in_(days)).filter(Market.market_name.ilike('%' + keyword + '%'))
        else:
            results = Market.query.filter(Market.market_name.ilike('%' + keyword + '%'))

    elif search_by == "address":
        if days:
            results = Market.query.filter(Market.market_day.in_(days)).filter(Market.market_address.ilike('%' + keyword + '%'))
        else:
            results = Market.query.filter(Market.market_address.ilike('%' + keyword + '%'))

    elif search_by == "commodity":
        results = Vendor.query.filter(Vendor.vendor_commodity.ilike('%' + keyword + '%'))

    else:
        return render_template('homepage.html')

    return render_template("results.html", search=search_by, results=results.all())


@app.route('/markets')
def display_markets():
    """ Display all markets """

    markets = Market.query.all()

    return render_template("markets.html", markets=markets)


@app.route('/markets/<market_id>', methods=['GET'])
def market_profile(market_id):

    """Show info about Market. """
    market = Market.query.get(market_id)
    vendors = market.vendors
    user_id = session.get("user_id")

    if user_id:
        user_favorite = UserFavoriteMarket.query.filter_by(
            market_id=market_id, user_id=user_id).first()

    else:
        user_favorite = None

    return render_template(

        "market_profile.html", market=market, vendors=vendors, favorite=user_favorite, user_id=user_id)


@app.route('/markets/<market_id>', methods=['POST'])
def market_added_favorites(market_id):
    """Add a market to favorites."""

    # Get form variables
    favorite_market = int(request.form["favorite"])

    user_id = session.get("user_id")
    if not user_id:
        flash("No User Logged In. Please Login!")

    # favorites = UserFavoriteMarkets.query.filter_by(user_id=user_id, market_id=market_id).first()

    else:
        favorite = UserFavoriteMarket(user_id=user_id, market_id=favorite_market)
        flash("Favorite added.")
        db.session.add(favorite)
        db.session.commit()

    return redirect('/markets/' + market_id)


@app.route('/vendors/<vendor_id>', methods=['POST'])
def vendor_added_favorites(vendor_id):
    """Add a vendor to favorites."""

    # Get form variables
    favorite_vendor = int(request.form["favorite"])

    user_id = session.get("user_id")
    if not user_id:
        flash("No User Logged In. Please Login!")
    else:
        favorite = UserFavoriteVendor(user_id=user_id, vendor_id=favorite_vendor)
        flash("Favorite added.")
        db.session.add(favorite)
        db.session.commit()

    return redirect('/vendors/' + vendor_id)


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


@app.route('/vendors/<vendor_id>')
def vendor_profile(vendor_id):

    """Show info about Vendor. """

    vendor = Vendor.query.get(vendor_id)
    commodity_list = vendor.vendor_commodity.split("|")
    return render_template(

        "vendor_profile.html", vendor=vendor, commodities=commodity_list)


@app.route('/markets.json')
def market_info_json():
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


@app.route('/markets/<market_id>/weather')
def get_market_weather(market_id):
    market = Market.query.get(market_id)
    city = market.market_city
    api_key = '2b567d4c7398383e9dabfe1f94e814e3'

    r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=' +
                     city + ',us&units=imperial&mode=html&appid=' + api_key)
    html = r.content.decode('utf-8')

    return html


@app.route('/register', methods=['GET'])
def register_form():
    """Show form for user signup."""

    return render_template("registration.html")


@app.route('/register', methods=['POST'])
def register_process():
    """Process registration."""

    # Get form variables
    email = request.form["email"]
    password = request.form["password"]
    age = int(request.form["age"])
    zipcode = request.form["zipcode"]

    hashpass = sha256_crypt.encrypt(password)

    user = User.query.filter_by(email=email).first()

    if not user:
        new_user = User(email=email, password=hashpass, age=age, zipcode=zipcode)

        db.session.add(new_user)
        db.session.commit()

        flash("User {} added.".format(email))
    if user:
        flash("User {} already exists. Please sign in".format(email))

    return redirect("/")


@app.route('/login', methods=['POST'])
def login_process():
    """Process login."""

    # Get form variables
    email = request.form["email"]
    password = request.form["password"]

    user = User.query.filter_by(email=email).first()

    if not user:
        flash("No such user")
        return redirect("/register")

    if sha256_crypt.verify(password, user.password):
        flash("Incorrect password")
        return redirect("/")

    session["user_id"] = user.user_id

    flash("Logged in")
    return redirect('/markets')


@app.route('/logout')
def logout():
    """Log out."""

    del session["user_id"]
    # flash("Logged Out.")
    return redirect("/")


@app.route('/favorites/<user_id>')
def display_user_favorites(user_id):
    user_id = session.get("user_id")
    user = User.query.get(user_id)

    markets = user.favorite_markets
    vendors = user.favorite_vendors

    return render_template("user_favorites.html", user=user, fav_vendors=vendors, fav_markets=markets)


if __name__ == "__main__":

    app.debug = True

    # make sure templates, etc. are not cached in debug mode

    app.jinja_env.auto_reload = app.debug

    connect_to_db(app)

    app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

    # Use the DebugToolbar

    DebugToolbarExtension(app)

    app.run(port=5000, host='0.0.0.0')
