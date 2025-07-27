# core/feed_router.py

from fastapi import APIRouter
import requests

router = APIRouter()

@router.get("/feed")
def unified_feed():
    try:
        btc_data = requests.get("https://neutron-api-hub.onrender.com/crypto").json()
        # Puoi aggiungere altre chiamate API interne: eth, forex, news, ecc.
        return {
            "btc_usd": btc_data.get("bitcoin", {}).get("usd"),
            "source": "neutron-api-hub"
        }
    except Exception as e:
        return {"error": str(e)}
