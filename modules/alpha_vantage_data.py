from fastapi import APIRouter, Query
import requests
import os

router = APIRouter()

API_KEY = os.getenv("ALPHA_VANTAGE_KEY")
BASE_URL = "https://www.alphavantage.co/query"


@router.get("/alpha/rsi")
def get_rsi(symbol: str):
    url = f"{BASE_URL}?function=RSI&symbol={symbol}&interval=daily&time_period=14&series_type=close&apikey={API_KEY}"
    response = requests.get(url)
    data = response.json()
    return data


@router.get("/alpha/forex")
def get_forex_rate(from_: str = Query(..., alias="from"), to: str = Query(..., alias="to")):
    url = f"{BASE_URL}?function=CURRENCY_EXCHANGE_RATE&from_currency={from_}&to_currency={to}&apikey={API_KEY}"
    response = requests.get(url)
    data = response.json()
    return data


@router.get("/alpha/stock")
def get_stock_price(symbol: str):
    url = f"{BASE_URL}?function=GLOBAL_QUOTE&symbol={symbol}&apikey={API_KEY}"
    response = requests.get(url)
    data = response.json()
    return data
