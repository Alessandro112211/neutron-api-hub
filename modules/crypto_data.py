# modules/crypto_data.py

from fastapi import APIRouter
import requests

router = APIRouter()

@router.get("/crypto")
def get_bitcoin_price():
    # Prima fonte: CoinGecko
    url_coingecko = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": "bitcoin",
        "vs_currencies": "usd"
    }

    try:
        response = requests.get(url_coingecko, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        return {"bitcoin": data.get("bitcoin", {})}
    except Exception as e:
        # Fallback: CoinMarketCap
        url_cmc = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"
        headers = {
            "X-CMC_PRO_API_KEY": "00f92556-744f-45bc-968b-1fcce9398035"
        }
        params_cmc = {
            "symbol": "BTC",
            "convert": "USD"
        }

        try:
            response = requests.get(url_cmc, headers=headers, params=params_cmc, timeout=10)
            response.raise_for_status()
            data = response.json()
            price = data["data"]["BTC"]["quote"]["USD"]["price"]
            return {"bitcoin": {"usd": round(price, 2)}}
        except Exception as ex:
            return {"error": f"Fallback API request failed: {str(ex)}"}
