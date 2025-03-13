import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
}

def get_price(symbol: str):
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"

    responce = requests.get(url, headers=headers)
    data = responce.json()
    
    return float(data["price"])