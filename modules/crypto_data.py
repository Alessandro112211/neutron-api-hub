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

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        return {"bitcoin": data.get("bitcoin", {})}
    except Exception as e:
        return {"error": f"API request failed: {str(e)}"}
