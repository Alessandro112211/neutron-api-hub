from fastapi import FastAPI
from modules.alpha_vantage_data import router as alpha_router
from modules.newsapi_data import router as news_router  # Se hai già anche il modulo newsapi
from modules.crypto_data import router as crypto_router  # Se hai già anche il modulo crypto

app = FastAPI()

# Includi tutte le API attive
app.include_router(alpha_router)
app.include_router(news_router)
app.include_router(crypto_router)
