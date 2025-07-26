import requests
import os
from fastapi import APIRouter

router = APIRouter()

@router.get("/news/gnews")
def get_gnews_news(q: str = "crypto", lang: str = "en"):
    API_KEY = os.getenv("GNEWS_API_KEY", "7715dfd2b3f43218d71f489bba65d3ab")
    url = f"https://gnews.io/api/v4/search?q={q}&lang={lang}&token={API_KEY}"
    response = requests.get(url)
    data = response.json()
    return {"news": data.get("articles", [])}
