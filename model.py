"""Models and database functions for Farmer's Market project."""

from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class User(db.Model):

    """User of website."""

    __tablename__ = "users"
    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)

    email = db.Column(db.String(64), nullable=True)

    password = db.Column(db.String(64), nullable=True)

    def __repr__(self):

        """Provide helpful representation when printed."""

        return "<User user_id={} email={}>".format(self.user_id,

                                                   self.email)


class Market(db.Model):

    """Markets from Farmer's Market website."""

    __tablename__ = "markets"

    market_id = db.Column(db.Integer, autoincrement=True, primary_key=True)

    address_id = db.Column(db.Integer,

                           db.ForeignKey('addresses.address_id'))

    market_name = db.Column(db.String(64), nullable=False)

    market_day = db.Column(db.String(32), nullable=False)

    market_start = db.Column(db.Time)

    market_end = db.Column(db.Time)

    address = db.relationship("Address")

    def __repr__(self):

        """Represent market info when printed."""

        return "<Market market_id={} market_name={} market_day={}>".format(

            self.market_id, self.market_name, self.market_day)


class Address(db.Model):

    """Addresses for Markets from Farmer's Market website."""

    __tablename__ = "addresses"

    address_id = db.Column(db.Integer, autoincrement=True, primary_key=True)

    address_street = db.Column(db.String(64), nullable=False)

    address_city = db.Column(db.String(32), nullable=False)

    address_state = db.Column(db.String(32), server_default='CA')

    address_zip = db.Column(db.String(32))

    def __repr__(self):

        """Represent market address info when printed."""

        return "<Address market_id={} address_id={} address_street={}, address_city={}, addresses_zip={}>".format(

            self.market_id, self.address_id, self.address_street, self.address_city, self.addresses_zip)


class Vendor(db.Model):

    """Vendors from Farmer's Market website."""

    __tablename__ = "vendors"

    vendor_id = db.Column(db.Integer, autoincrement=True, primary_key=True)

    vendor_name = db.Column(db.String(64), nullable=False)

    vendor_website = db.Column(db.String(250))

    vendor_commodity = db.Column(db.String(250), nullable=False)

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

######################### HELPER FCNS ###################################


def connect_to_db(app):

    """Connect the database to our Flask app."""
    # Configure to use our PstgreSQL database

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///project'

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = app

    db.init_app(app)


if __name__ == "__main__":

    from server import app

    connect_to_db(app)

    print "Connected to DB."
    db.create_all()
