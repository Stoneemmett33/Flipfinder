def calculate_profit(
    resale_price,
    purchase_price,
    shipping_cost=12,
    platform_fee=0.13,
    payment_fee=0.03,
    tax_buffer=0.02
):
    total_fees = resale_price * (platform_fee + payment_fee + tax_buffer)
    net_revenue = resale_price - total_fees - shipping_cost
    profit = net_revenue - purchase_price
    roi = (profit / purchase_price) * 100 if purchase_price > 0 else 0

    return {
        "net_revenue": round(net_revenue, 2),
        "profit": round(profit, 2),
        "roi_percent": round(roi, 2)
    }
