from fastapi import FastAPI
from modules.alpha_vantage_data import router as alpha_router
from modules.newsapi_data import router as news_router
from modules.crypto_data import router as crypto_router

app = FastAPI()

# Includi tutte le API attive
app.include_router(alpha_router)
app.include_router(news_router)
app.include_router(crypto_router)

# Rotta principale per test
@app.get("/")
def read_root():
    return {"message": "NEUTRON API HUB™ is live!"}
