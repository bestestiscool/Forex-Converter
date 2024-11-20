async function convertCurrency() {
    const fromCurrency = document.getElementById('from').value.toUpperCase().trim();
    const toCurrency = document.getElementById('to').value.toUpperCase().trim();
    const amount = document.getElementById('amount').value;

    // Clear previous results
    const resultElement = document.getElementById('result');
    resultElement.textContent = '';
    resultElement.style.display = 'none';

    // Check if the currencies are valid (e.g., not empty and are three letters long)
    if (!fromCurrency || fromCurrency.length !== 3) {
        resultElement.textContent = 'Please enter a valid "From" currency code.';
        resultElement.style.display = 'block';
        return;
    }
    if (!toCurrency || toCurrency.length !== 3) {
        resultElement.textContent = 'Please enter a valid "To" currency code.';
        resultElement.style.display = 'block';
        return;
    }

    // Check if the amount is valid (greater than 0)
    if (isNaN(amount) || amount <= 0) {
        resultElement.textContent = 'Please enter an amount greater than 0.';
        resultElement.style.display = 'block';
        return;
    }

    try {
        // POST to the Flask `/convert` route which handles the conversion server-side
        const response = await axios.post('/convert', {
            from_currency: fromCurrency,
            to_currency: toCurrency,
            amount: amount
        });
        
        // Handle the response from your Flask app
        if (response.data.result) {
            resultElement.textContent = `Converted: ${response.data.result}`;
            resultElement.style.display = 'block';
        } else {
            resultElement.textContent = 'Conversion failed. Please try again.';
            resultElement.style.display = 'block';
        }
    } catch (error) {
        // Log the error and show it on the webpage
        console.error('Error during the conversion:', error);
        resultElement.textContent = 'An error occurred during conversion. ' + (error.response ? error.response.data.error : error.message);
        resultElement.style.display = 'block';
    }
}

document.addEventListener('DOMContentLoaded', function() {
    const convertButton = document.getElementById('convert-button');
    if (convertButton) {
        convertButton.addEventListener('click', convertCurrency);
    }
});

// Basic idea of conversion