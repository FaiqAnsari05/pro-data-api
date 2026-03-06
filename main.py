from fastapi import FastAPI, Header, HTTPException
import random
import requests

app = FastAPI()

# RapidAPI Dashboard > Hub Listing > Security se mili Proxy Secret yahan likhein
RAPIDAPI_SECRET = "YOUR_ACTUAL_PROXY_SECRET_HERE"

@app.get("/")
def home():
    return {"status": "Online", "message": "API is Secured. Please use RapidAPI Marketplace."}

@app.get("/news")
def get_news(x_rapidapi_proxy_secret: str = Header(None)):
    if x_rapidapi_proxy_secret != RAPIDAPI_SECRET:
        raise HTTPException(status_code=403, detail="Direct access forbidden.")
    
    headlines = [
        "Tech Giants announce new AI model.",
        "Global markets show recovery signs.",
        "New space mission scheduled for next month.",
        "Electric vehicle sales hit record high."
    ]
    return {"headline": random.choice(headlines), "category": "General"}

@app.get("/crypto")
def get_crypto(x_rapidapi_proxy_secret: str = Header(None)):
    if x_rapidapi_proxy_secret != RAPIDAPI_SECRET:
        raise HTTPException(status_code=403, detail="Direct access forbidden.")
    
    try:
        url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd"
        response = requests.get(url).json()
        return response
    except:
        return {"error": "Service temporarily unavailable"}