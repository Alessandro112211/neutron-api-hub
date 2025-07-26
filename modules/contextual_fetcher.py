import requests
import os
from fastapi import APIRouter

router = APIRouter()

@router.get("/news/contextual")
def get_contextual_news(q: str = "bitcoin"):
    API_KEY = os.getenv("CONTEXTUALWEB_API_KEY", "9c3f8eb1-2fc6-4bfb-83f5-28514d9e8f29")
    url = f"https://contextualwebsearch-websearch-v1.p.rapidapi.com/api/Search/NewsSearchAPI"
    headers = {
        "X-RapidAPI-Key": API_KEY,
        "X-RapidAPI-Host": "contextualwebsearch-websearch-v1.p.rapidapi.com"
    }
    params = {"q": q, "pageNumber": 1, "pageSize": 10, "autoCorrect": True}
    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    return {"news": data.get("value", [])}
