from flask import Flask, request, jsonify, render_template
import requests
# from secret_api_key import API_KEY
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from.env file

API_KEY = os.getenv("API_KEY")

app = Flask(__name__)
app.app_context().push()


@app.route('/')
def index():
    """Serve the index.html page."""
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert_currency():
    """Endpoint to perform currency conversion."""
    data = request.get_json()

    from_currency = data.get('from_currency')
    to_currency = data.get('to_currency')
    amount = float(data.get('amount'))

    # If from_currency and to_currency are the same, return a response with an empty list for 'result'
    if from_currency == to_currency:
        return jsonify({'result': []}), 200

    try:
        response = requests.get(
            'http://api.exchangerate.host/live',
            params={
                'access_key': API_KEY,  # Include your API key in the request parameters.
                'source': from_currency,
                'currencies': to_currency
                
            }
        )
        response.raise_for_status()  # This will raise an HTTPError if the HTTP request returned an unsuccessful status code

        response_data = response.json()
        quotes = response_data.get('quotes')
        if quotes:
            exchange_quote = next(iter(quotes.values()))
            if exchange_quote:
                # Multiply the exchange rate by the amount the user wants to convert
                converted_amount = amount * exchange_quote
                return jsonify({'result': converted_amount})
            else:
                return jsonify({'error': 'Exchange rate not found.'}), 400
        else:
            return jsonify({'error': 'No quotes found in the response.'}), 400 


    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

