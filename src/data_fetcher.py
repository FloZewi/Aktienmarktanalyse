import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta


def fetch_stock_data(ticker, start_date, end_date):
    """Holt historische Aktienkurse von Yahoo Finance."""
    data = yf.download(ticker, start=start_date, end=end_date)
    if not data.empty:
        data.reset_index(inplace=True)
        return data
    else:
        raise ValueError(f"Keine Daten für {ticker} verfügbar.")


def fetch_multiple_stocks(tickers, start_date, end_date):
    """Holt Daten für mehrere Aktien."""
    all_data = {}
    for ticker in tickers:
        try:
            all_data[ticker] = fetch_stock_data(ticker, start_date, end_date)
        except ValueError as e:
            print(e)
    return all_data


if __name__ == "__main__":
    tickers = ["AAPL", "GOOGL", "MSFT", "AMZN"]
    start_date = (datetime.now() - timedelta(days=365)).strftime('%Y-%m-%d')
    end_date = datetime.now().strftime('%Y-%m-%d')

    stock_data = fetch_multiple_stocks(tickers, start_date, end_date)
    for ticker, data in stock_data.items():
        data.to_csv(f"../data/{ticker}_data.csv", index=False)
