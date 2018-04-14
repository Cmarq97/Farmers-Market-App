""" In order to properly run this file for testing, run the following:
    createdb testdb && python model.py && psql testdb < testdata.sql
    && python test.py"""

from unittest import TestCase
from model import connect_to_db, db, example_data
from server import app


class FlaskTestsDatabase(TestCase):
    """Flask tests that use the database."""

    def setUp(self):
        """Stuff to do before every test."""

        # Get the Flask test client
        self.client = app.test_client()
        app.config['TESTING'] = True

        # Connect to test database
        connect_to_db(app, "postgresql:///testdb")

        # Create tables and add sample data
        db.create_all()
        example_data()

    def tearDown(self):
        """Do at end of every test."""

        db.session.close()
        db.drop_all()

    def test_search(self):
        result = self.client.post("/search",
                                  data={"search_by": "address",
                                        "keyword": "oakland",
                                        "days": ['Friday']},
                                  follow_redirects=True)
        self.assertIn("Old Oakland", result.data)


class FlaskTestsRoutes(TestCase):
    """ Flask tests routes & html """

    def setUp(self):
        """Stuff to do before every test."""

        self.client = app.test_client()
        app.config['TESTING'] = True
        connect_to_db(app)

    def test_homepage_route(self):
        """ Homepage html test """
        result = self.client.get("/")
        self.assertEqual(result.status_code, 200)
        self.assertIn('Welcome to your local', result.data)

    def test_markets_route(self):
        """ Markets html test """
        result = self.client.get("/markets")
        self.assertEqual(result.status_code, 200)
        self.assertIn('all Markets in our database', result.data)

    def test_vendors_route(self):
        """ Vendors html test """
        result = self.client.get("/vendors")
        self.assertEqual(result.status_code, 200)
        self.assertIn('all vendors in our database', result.data)

    def test_vendor_profile_route(self):
        """ Vendors profile html test """
        result = self.client.get("/vendors/1/")
        self.assertEqual(result.status_code, 200)
        self.assertIn('Commodities', result.data)

    def test_market_profile_route(self):
        """ Market profile html test """
        result = self.client.get("/markets/1/")
        self.assertEqual(result.status_code, 200)
        self.assertIn('Market Name', result.data)

    def test_search_homepage_redirect_route(self):
        """ Search results redirect to homepage html test """
        result = self.client.get("/search")
        self.assertEqual(result.status_code, 200)
        self.assertIn('keyword', result.data)

if __name__ == "__main__":
    import unittest

    unittest.main()
