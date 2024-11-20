import unittest
from app import app

class CurrencyConverterTestCase(unittest.TestCase):

    def setUp(self):
        # Set up the test client
        self.app = app.test_client()
        # Propagate the exceptions to the test client
        self.app.testing = True

    def test_conversion_same_currency(self):
        # Test that converting from USD to USD returns the correct response
        response = self.app.post('/convert', json={
            'from_currency': 'USD',
            'to_currency': 'USD',
            'amount': 1
        })
        
        # Parse the response data
        data = response.get_json()
        
         # Check that the 'result' key exists in the response data
        self.assertIn('result', data, "The key 'result' is not in the response.")
        
        # Now check that the value of 'result' is an empty list
        self.assertEqual(data['result'], [], "The result should be an empty list for the same currency conversion.")

    # Add more tests to cover different scenarios and edge cases.

if __name__ == '__main__':
    unittest.main()
