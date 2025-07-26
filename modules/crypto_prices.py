import requests

def get_crypto_price(coin="bitcoin", vs_currency="usd"):
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": coin,
        "vs_currencies": vs_currency
    }
    try:
        response = requests.get(url, params=params)
        return response.json()
    except Exception as e:
        return {"error": str(e)}
