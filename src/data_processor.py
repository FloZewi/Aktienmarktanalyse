import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler


def process_stock_data(file_path):
    """Bereitet Aktienkurse für das Modell vor."""
    df = pd.read_csv(file_path)
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)
    df = df[['Close']]

    scaler = MinMaxScaler()
    df['Close_scaled'] = scaler.fit_transform(df[['Close']])
    return df, scaler


def create_sequences(data, sequence_length):
    """Erstellt Sequenzen für das Modelltraining."""
    sequences = []
    labels = []
    for i in range(len(data) - sequence_length):
        seq = data[i:i+sequence_length]
        label = data[i+sequence_length]
        sequences.append(seq)
        labels.append(label)
    return np.array(sequences), np.array(labels)
