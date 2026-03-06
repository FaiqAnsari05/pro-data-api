from fastapi import FastAPI, Header, HTTPException
import random
import requests

# Vercel ke liye special configuration
app = FastAPI(docs_url="/api/docs", openapi_url="/api/openapi.json")

# RapidAPI Dashboard > Hub Listing > Security se mili Proxy Secret yahan likhein
# Abhi ke liye testing ke liye aap isse empty bhi chor sakte hain ya koi secret rakh dein
RAPIDAPI_SECRET = "YOUR_ACTUAL_PROXY_SECRET_HERE"

@app.get("/")
def home():
    return {"status": "Online", "message": "API is Secured. Please use RapidAPI Marketplace."}

@app.get("/news")
def get_news(x_rapidapi_proxy_secret: str = Header(None)):
    # Security Check
    if x_rapidapi_proxy_secret != RAPIDAPI_SECRET:
        raise HTTPException(status_code=403, detail="Direct access forbidden. Use RapidAPI.")
    
    headlines = [
        "Tech Giants announce new AI model.",
        "Global markets show recovery signs.",
        "New space mission scheduled for next month.",
        "Electric vehicle sales hit record high."
    ]
    return {"headline": random.choice(headlines), "category": "General"}

@app.get("/crypto")
def get_crypto(x_rapidapi_proxy_secret: str = Header(None)):
    # Security Check
    if x_rapidapi_proxy_secret != RAPIDAPI_SECRET:
        raise HTTPException(status_code=403, detail="Direct access forbidden. Use RapidAPI.")
    
    try:
        # Real-time Crypto Price
        url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd"
        response = requests.get(url).json()
        return response
    except Exception as e:
        return {"error": "Service temporarily unavailable"}