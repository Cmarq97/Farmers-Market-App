"""Models and database functions for Farmer's Market project."""

from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class User(db.Model):

    """User of website."""

    __tablename__ = "users"
    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String(64), nullable=False)
    password = db.Column(db.String(250), nullable=False)
    age = db.Column(db.Integer, nullable=True)
    zipcode = db.Column(db.String(15), nullable=True)

    favorite_vendors = db.relationship("Vendor", secondary="userfavoritevendors")
    favorite_markets = db.relationship("Market", secondary="userfavoritemarkets")

    def __repr__(self):

        """Provide helpful representation when printed."""

        return "<User user_id={} email={}>".format(self.user_id,
                                                   self.email)


class UserFavoriteVendor(db.Model):
    """ Shows which vendors are a users favorite """
    __tablename__ = "userfavoritevendors"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)

    user_id = db.Column(db.Integer,
                        db.ForeignKey('users.user_id'))

    vendor_id = db.Column(db.Integer,
                          db.ForeignKey('vendors.vendor_id'))


class UserFavoriteMarket(db.Model):
    """ Shows which markets are a users favorite """
    __tablename__ = "userfavoritemarkets"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)

    user_id = db.Column(db.Integer,
                        db.ForeignKey('users.user_id'))

    market_id = db.Column(db.Integer,

                          db.ForeignKey('markets.market_id'))
    markets = db.relationship("Market")


class Market(db.Model):

    """Markets from Farmer's Market website."""

    __tablename__ = "markets"

    market_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    market_name = db.Column(db.String(64), nullable=False)
    market_day = db.Column(db.String(32), nullable=False)
    market_start = db.Column(db.Time(timezone=True))
    market_end = db.Column(db.Time)
    market_address = db.Column(db.String(250), nullable=False)
    market_city = db.Column(db.String(64), nullable=False)

    def __repr__(self):

        """Represent market info when printed."""

        return "<Market market_id={} market_name={} market_day={} market_address={}>".format(

            self.market_id, self.market_name, self.market_day, self.market_address)


class Vendor(db.Model):

    """Vendors from Farmer's Market website."""

    __tablename__ = "vendors"

    vendor_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    vendor_name = db.Column(db.String(64), nullable=False)
    vendor_website = db.Column(db.String(250))
    vendor_commodity = db.Column(db.String(250), nullable=False)
    map_icon = db.Column(db.String(250), nullable=True)
    organic = db.Column(db.Boolean, nullable=True)
    credit = db.Column(db.Boolean, nullable=True)
    markets = db.relationship("Market", backref='vendors', secondary="marketvendors", uselist=True)

    def __repr__(self):

        """Represent market info when printed."""

        return "<Vendor vendor_id={} vendor_name={} vendor_commodity={}>".format(

            self.vendor_id, self.vendor_name, self.vendor_commodity)


class MarketVendor(db.Model):
    """ Shows which vendors go to which markets """
    __tablename__ = "marketvendors"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)

    market_id = db.Column(db.Integer,

                          db.ForeignKey('markets.market_id'))

    vendor_id = db.Column(db.Integer,

                          db.ForeignKey('vendors.vendor_id'))


def example_data():
    """Create some sample data."""

    # In case this is run more than once, empty out existing data
    Vendor.query.delete()
    Market.query.delete()
    MarketVendor.query.delete()

    mry = Market(market_name="Monterey Farmer's Market", market_day='Tuesday', market_start='16:00',
                 market_end='20:00', market_address='Alvarado St Monterey CA 93940')

    pls = Market(market_name="Pleasonton Farmer's Market", market_day='Saturday', market_start='09:00',
                 market_end='13:00', market_address='424 Main St. Pleasonton CA')

    dan = Market(market_name="Danville Farmer's Market", market_day='Saturday', market_start='09:00',
                 market_end='13:00', market_address='205 Railroad Ave. Danville CA')

    sun = Vendor(vendor_name='Sunrise Nursery', vendor_website='',
                 vendor_commodity='Cut Flowers|Eggs', map_icon='/static/img/sunflower.png',
                 markets=[pls, dan, mry])

    oak = Vendor(vendor_name='Lone Oak Ranch', vendor_website='ThefarmerandtheDale.com',
                 vendor_commodity='Fruit|Vegetables', map_icon='/static/img/vegetables.png',
                 markets=[pls, dan])

    vie = Vendor(vendor_name='La Vie', vendor_website='DrinkLaVie.com',
                 vendor_commodity='Fresh Juice', map_icon='/static/img/healthy-food.png',
                 markets=[pls, dan])

    db.session.add_all([mry, pls, dan, sun, vie, oak])
    db.session.commit()


######################### HELPER FCNS ###################################


def connect_to_db(app, db_uri="postgresql:///project"):
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


if __name__ == '__main__':
    from server import app
    connect_to_db(app)
    db.create_all()
    print "Data Tables Created"
    print "Connected to DB."
