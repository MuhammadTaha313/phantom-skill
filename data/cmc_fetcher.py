import os
import requests
from dotenv import load_dotenv

load_dotenv()

CMC_API_KEY = os.getenv("CMC_API_KEY")
BASE_URL = "https://pro-api.coinmarketcap.com/v1"

HEADERS = {
    "X-CMC_PRO_API_KEY": CMC_API_KEY,
    "Accept": "application/json"
}

def get_listings(limit=100):
    """Get latest crypto listings with market data"""
    url = f"{BASE_URL}/cryptocurrency/listings/latest"
    params = {
        "limit": limit,
        "convert": "USD",
        "sort": "volume_24h",
        "sort_dir": "desc"
    }
    try:
        r = requests.get(url, headers=HEADERS, params=params)
        r.raise_for_status()
        return r.json().get("data", [])
    except Exception as e:
        print(f"[CMC] listings error: {e}")
        return []

def get_fear_and_greed():
    """Get Fear & Greed index from CMC"""
    url = f"{BASE_URL}/global-metrics/quotes/latest"
    try:
        r = requests.get(url, headers=HEADERS)
        r.raise_for_status()
        data = r.json().get("data", {})
        return {
            "btc_dominance": data.get("btc_dominance", 0),
            "total_market_cap": data.get("quote", {}).get("USD", {}).get("total_market_cap", 0),
            "total_volume_24h": data.get("quote", {}).get("USD", {}).get("total_volume_24h", 0),
            "total_market_cap_yesterday_percentage_change": data.get("quote", {}).get("USD", {}).get("total_market_cap_yesterday_percentage_change", 0),
        }
    except Exception as e:
        print(f"[CMC] global metrics error: {e}")
        return {}

def get_token_info(symbol="BNB"):
    """Get specific token data"""
    url = f"{BASE_URL}/cryptocurrency/quotes/latest"
    params = {"symbol": symbol, "convert": "USD"}
    try:
        r = requests.get(url, headers=HEADERS, params=params)
        r.raise_for_status()
        data = r.json().get("data", {})
        token = data.get(symbol, [{}])
        if isinstance(token, list):
            token = token[0]
        quote = token.get("quote", {}).get("USD", {})
        return {
            "symbol": symbol,
            "price": quote.get("price", 0),
            "volume_24h": quote.get("volume_24h", 0),
            "percent_change_1h": quote.get("percent_change_1h", 0),
            "percent_change_24h": quote.get("percent_change_24h", 0),
            "percent_change_7d": quote.get("percent_change_7d", 0),
            "market_cap": quote.get("market_cap", 0),
            "volume_change_24h": quote.get("volume_change_24h", 0),
        }
    except Exception as e:
        print(f"[CMC] token info error: {e}")
        return {}

def get_trending_tokens():
    """Get trending/gainers on BSC ecosystem"""
    url = f"{BASE_URL}/cryptocurrency/trending/gainers-losers"
    params = {"time_period": "24h", "limit": 20, "convert": "USD"}
    try:
        r = requests.get(url, headers=HEADERS, params=params)
        r.raise_for_status()
        return r.json().get("data", {})
    except Exception as e:
        print(f"[CMC] trending error: {e}")
        return {}
