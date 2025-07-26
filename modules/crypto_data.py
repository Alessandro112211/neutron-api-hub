# modules/crypto_data.py

from fastapi import APIRouter
import requests

router = APIRouter()

@router.get("/crypto")
def get_bitcoin_price():
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": "bitcoin",
        "vs_currencies": "usd"
    }

    response = requests.get(url, params=params)
    if response.status_code != 200:
        return {"error": "API request failed"}

    data = response.json()
    return {"bitcoin": data.get("bitcoin", {})}
