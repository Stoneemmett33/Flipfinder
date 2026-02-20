from fastapi import FastAPI, Query
from app.pricing_engine import calculate_market_metrics
from app.profit_engine import calculate_profit
from app.scoring import score_deal

app = FastAPI()

@app.get("/")
def root():
    return {"status": "FlipFinder Running"}

@app.get("/analyze")
def analyze(purchase_price: float = Query(...)):
    sold_prices = [210, 205, 215, 220, 200, 208]

    metrics = calculate_market_metrics(sold_prices)

    profit_data = calculate_profit(
        resale_price=metrics["median_price"],
        purchase_price=purchase_price
    )

    sell_through = 0.75
    deal_score = score_deal(
        profit_data["roi_percent"],
        sell_through,
        metrics["volatility"]
    )

    return {
        "median_market_price": metrics["median_price"],
        "recommended_resale_price": metrics["median_price"],
        "profit": profit_data["profit"],
        "roi_percent": profit_data["roi_percent"],
        "deal_score": deal_score,
        "recommendation": "BUY" if deal_score > 70 else "PASS"
    }
