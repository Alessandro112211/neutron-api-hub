from fastapi import FastAPI
from modules.alpha_vantage_data import router as alpha_router
from modules.newsapi_data import router as news_router
from modules.crypto_data import router as crypto_router
from modules.feed_router import router as feed_router  # <--- nuovo
import requests

app = FastAPI()

# Includi tutte le API attive
app.include_router(alpha_router)
app.include_router(news_router)
app.include_router(crypto_router)
app.include_router(feed_router)  # <--- nuovo

# Rotta principale per test
@app.get("/")
def read_root():
    return {"message": "NEUTRON API HUB™ is live!"}

# Test di connessione al modulo crypto
@app.get("/testbtc")
def test_btc():
    try:
        r = requests.get("https://neutron-api-hub.onrender.com/crypto")
        prezzo = r.json()
        return {"BTC_price": prezzo}
    except:
        return {"error": "Nessuna risposta dal modulo crypto."}
