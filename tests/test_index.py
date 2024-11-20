import unittest
from app import app

class CurrencyConverterTestCase(unittest.TestCase):

    def setUp(self):
        # Set up the test client
        self.app = app.test_client()
        # Propagate the exceptions to the test client
        self.app.testing = True

    def test_home_page(self):
        # Test that the home page loads correctly
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
