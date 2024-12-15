def recommend_investments(predictions, tickers, threshold=0.05):
    """Gibt Aktien mit erwarteten Wachstumsraten über dem Schwellenwert zurück."""
    recommendations = {}
    for ticker, prediction in predictions.items():
        growth_rate = (prediction[-1] - prediction[0]) / prediction[0]
        if growth_rate > threshold:
            recommendations[ticker] = growth_rate
    return recommendations
