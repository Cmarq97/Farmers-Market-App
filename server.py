""" Farmers Market App """
import os
import sys
from jinja2 import StrictUndefined
from flask_debugtoolbar import DebugToolbarExtension
from flask import (Flask, render_template, redirect, request, flash, jsonify,
                   session)
from model import User, Market, Vendor, UserFavoriteMarket, UserFavoriteVendor
from model import connect_to_db, db
import requests
from passlib.hash import sha256_crypt
from datetime import datetime
from pytz import timezone

app = Flask(__name__)

app.secret_key = "BAFM"

app.jinja_env.undefined = StrictUndefined


@app.route('/vendors')
def flip():
    vendors = Vendor.query.all()
    return render_template('flip.html', vendors=vendors)


############################# HOMEPAGE ROUTES ##################################

@app.route('/')
def homepage():
    """ Displays Homepage html && determines day of week and displays
         appropriate markets on homepage"""

    days_dict = {6: "Sunday", 0: "Monday", 1: "Tuesday", 2: "Wednesday",
                 3: "Thursday", 4: "Friday", 5: "Saturday"}

    # Takes current time in UTC, aware of TZ
    now_utc = datetime.now(timezone('UTC'))

    # Determines current day of the week in PST and determines the string
    #  value from days_dict
    day = days_dict[now_utc.astimezone(timezone('US/Pacific')).weekday()]

    #  Searches db for markets on current day
    results = Market.query.filter(Market.market_day == day)

    return render_template("homepage.html", markets=results)


@app.route('/search', methods=['GET', 'POST'])
def search_results():
    """ Displays results of a search"""
    search_by = request.form.get("search_by")
    keyword = request.form.get("keyword")
    days = request.form.getlist("day")

    if search_by == "vendor":  # if vendor seach box was selected
        results = Vendor.query.filter(
            Vendor.vendor_name.ilike('%' + keyword + '%'))

    elif search_by == "market":  # if market search box was selected
        if days:  # if days were specified, select only markets on those days
            results = Market.query.filter(Market.market_day.in_(days)).filter(
                Market.market_name.ilike('%' + keyword + '%'))
        else:
            results = Market.query.filter(
                Market.market_name.ilike('%' + keyword + '%'))

    elif search_by == "address":  # if market address search was selected
        if days:  # if days were specified, select only markets on those days
            results = Market.query.filter(Market.market_day.in_(days)).filter(
                Market.market_address.ilike('%' + keyword + '%'))
        else:
            results = Market.query.filter(
                Market.market_address.ilike('%' + keyword + '%'))

    elif search_by == "commodity":  # if vendor commodity was selected
        results = Vendor.query.filter(
            Vendor.vendor_commodity.ilike('%' + keyword + '%'))

    else:  # if search was not completed correctlty return home
        return render_template('homepage.html')

    return render_template("results.html",
                           search=search_by, results=results.all())


############################### MARKET ROUTES###################################

@app.route('/markets')
def display_markets():
    """ Display all markets in database """

    markets = Market.query.all()
    api_key = os.environ['GOOGLE_MAPS_API_KEY']

    return render_template("markets.html", markets=markets, api_key=api_key)


@app.route('/markets.json')
def market_info_json():
    """ Creates JSON information about all markets for later use in API's"""
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


@app.route('/markets/<market_id>', methods=['GET'])
def market_profile(market_id):

    """ Displays info about specific market. """
    market = Market.query.get(market_id)
    vendors = market.vendors
    user_id = session.get("user_id")
    api_key = os.environ['GOOGLE_MAPS_API_KEY']

    # Checks to see if there is a user logged
    if user_id:
        # Queries for their favorites value of the market
        user_favorite = UserFavoriteMarket.query.filter_by(
            market_id=market_id, user_id=user_id).first()

    else:
        user_favorite = None

    return render_template(

        "market_profile.html", market=market, vendors=vendors,
        favorite=user_favorite, user_id=user_id, api_key=api_key)


@app.route('/markets/<market_id>.json')
def market_json(market_id):
    """ Creates JSON information for a specific market for use in APIs """
    market = Market.query.get(market_id)

    market_info = {
        'address': market.market_address,
        'name': market.market_name
    }
    return jsonify(market_info)


@app.route('/markets/<market_id>/weather')
def get_market_weather(market_id):
    """ Creates a weather icon for specific market """
    market = Market.query.get(market_id)
    city = market.market_city
    api_key = os.environ['WEATHER_API_KEY']

    r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=' +
                     city + ',us&units=imperial&mode=html&appid=' + api_key)
    html = r.content.decode('utf-8')

    return html


@app.route('/markets/<market_id>', methods=['POST'])
def market_added_favorites(market_id):
    """Add a market to user's favorites."""

    # Get form variables
    favorite_market = int(request.form["favorite"])

    user_id = session.get("user_id")
    if not user_id:
        flash("No User Logged In. Please Login!")
        return redirect("/login")

    # favorites = UserFavoriteMarkets.query.filter_by(user_id=user_id, market_id=market_id).first()

    else:
        favorite = UserFavoriteMarket(user_id=user_id, market_id=favorite_market)
        flash("Favorite added.")
        db.session.add(favorite)
        db.session.commit()

    return redirect('/markets/' + market_id)

############################## VENDOR ROUTES ###################################


# @app.route('/vendors')
def display_vendors():
    """ Display all vendors """

    vendors = Vendor.query.all()

    return render_template("vendors.html", vendors=vendors)


@app.route('/vendors/<vendor_id>')
def vendor_profile(vendor_id):

    """ Show info about Vendor according to vendor_id. """

    api_key = os.environ['GOOGLE_MAPS_API_KEY']
    vendor = Vendor.query.get(vendor_id)
    commodity_list = vendor.vendor_commodity.split("|")
    return render_template(

        "vendor_profile.html", vendor=vendor, api_key=api_key, commodities=commodity_list)


@app.route('/vendors/<vendor_id>', methods=['POST'])
def vendor_added_favorites(vendor_id):
    """Add a vendor to user's favorites."""

    # Get form variables
    favorite_vendor = int(request.form["favorite"])

    user_id = session.get("user_id")
    if not user_id:
        flash("No User Logged In. Please Login!")
    else:
        favorite = UserFavoriteVendor(user_id=user_id,
                                      vendor_id=favorite_vendor)
        flash("Favorite added.")
        db.session.add(favorite)
        db.session.commit()

    return redirect('/vendors/' + vendor_id)


@app.route('/vendors/<vendor_id>/json')
def vendor_info_json(vendor_id):
    """JSON information about specific vendors markets for use in APIs"""
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

########################## USER SPECIFIC ROUTES ################################


@app.route('/register', methods=['GET'])
def register_form():
    """Show form for user signup."""

    return render_template("registration.html")


@app.route('/register', methods=['POST'])
def register_process():
    """Process new user registration."""

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

    # If the user does not exist, it will send them to register
    if not user:
        flash("No such user")
        return redirect("/register")

    # Checks the user's password entry to the encrypted password in db
    if sha256_crypt.verify(password, user.password):
        flash("Incorrect password")
        return redirect("/")

    # Stores user in session for later use
    session["user_id"] = user.user_id

    flash("Logged in")
    return redirect('/')


@app.route('/logout')
def logout():
    """Log out."""

    # deletes the current user in session
    del session["user_id"]

    # flash("Logged Out.")
    return redirect("/")


@app.route('/favorites/<user_id>')
def display_user_favorites(user_id):
    """ Displays user's favorites """
    user_id = session.get("user_id")
    user = User.query.get(user_id)

    markets = user.favorite_markets
    vendors = user.favorite_vendors

    return render_template("user_favorites.html", user=user,
                           fav_vendors=vendors, fav_markets=markets)


if __name__ == "__main__":

    app.debug = True

    # make sure templates, etc. are not cached in debug mode

    app.jinja_env.auto_reload = app.debug

    connect_to_db(app)

    app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

    # Use the DebugToolbar

    DebugToolbarExtension(app)

    app.run(port=5000, host='0.0.0.0')
