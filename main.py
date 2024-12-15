from src.data_fetcher import fetch_stock_data
from src.data_processor import process_stock_data, create_sequences
from src.model import create_lstm_model
from src.recommender import recommend_investments
from src.visualization import plot_predictions

import numpy as np

if __name__ == "__main__":
    ticker = "AAPL"
    data, scaler = process_stock_data(f"data/{ticker}_data.csv")

    sequence_length = 60
    sequences, labels = create_sequences(data['Close_scaled'].values, sequence_length)

    X_train, y_train = sequences[:int(0.8 * len(sequences))], labels[:int(0.8 * len(labels))]
    X_test, y_test = sequences[int(0.8 * len(sequences)):], labels[int(0.8 * len(labels)):]

    model = create_lstm_model((X_train.shape[1], 1))
    model.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_test, y_test))

    predictions = model.predict(X_test)
    predictions = scaler.inverse_transform(predictions)
    actual_prices = scaler.inverse_transform(y_test.reshape(-1, 1))

    plot_predictions(actual_prices, predictions, f"Vorhersage für {ticker}")
