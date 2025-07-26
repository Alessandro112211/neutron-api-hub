import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("NEWSAPI_KEY")

def get_latest_news(query="crypto", language="en", sort_by="publishedAt"):
    url = "https://newsapi.org/v2/everything"
    params = {
        "q": query,
        "language": language,
        "sortBy": sort_by,
        "pageSize": 5,
        "apiKey": API_KEY
    }
    try:
        response = requests.get(url, params=params)
        data = response.json()
        articles = data.get("articles", [])
        return articles if articles else [{"message": "Nessun risultato trovato."}]
    except Exception as e:
        return {"error": str(e)}
