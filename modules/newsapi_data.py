# modules/newsapi_data.py

from fastapi import APIRouter
import requests
import os
from dotenv import load_dotenv

load_dotenv()

router = APIRouter()

NEWSAPI_KEY = os.getenv("NEWSAPI_KEY")

@router.get("/news")
def get_latest_news():
    url = "https://newsapi.org/v2/top-headlines"
    params = {
        "language": "en",
        "pageSize": 5,
        "apiKey": NEWSAPI_KEY
    }

    response = requests.get(url, params=params)
    data = response.json()

    if data.get("status") != "ok":
        return {"news": [{"message": "Nessun risultato trovato."}]}

    articles = data.get("articles", [])
    simplified_news = [
        {
            "title": article.get("title"),
            "url": article.get("url"),
            "source": article.get("source", {}).get("name")
        }
        for article in articles
    ]

    return {"news": simplified_news}
