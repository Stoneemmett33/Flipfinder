def score_deal(roi, sell_through, volatility):
    score = 0

    if roi > 40:
        score += 40
    elif roi > 25:
        score += 30
    elif roi > 15:
        score += 20

    score += sell_through * 30

    if volatility > 0.25:
        score -= 15

    return max(min(round(score), 100), 0)
