import requests

def get_bitcoin_price():
    """Fetch the current price of Bitcoin."""
    url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
    response = requests.get(url)
    data = response.json()
    return data['bpi']['USD']['rate']

# Fetch and print the current price of Bitcoin
bitcoin_price = get_bitcoin_price()
print(f"The current price of Bitcoin is: ${bitcoin_price}")
