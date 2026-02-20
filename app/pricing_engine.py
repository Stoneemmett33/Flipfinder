import statistics

def calculate_market_metrics(sold_prices):
    median_price = statistics.median(sold_prices)
    mean_price = statistics.mean(sold_prices)
    stdev = statistics.stdev(sold_prices) if len(sold_prices) > 1 else 0

    volatility = stdev / mean_price if mean_price > 0 else 0

    return {
        "median_price": round(median_price, 2),
        "mean_price": round(mean_price, 2),
        "volatility": round(volatility, 3)
    }
