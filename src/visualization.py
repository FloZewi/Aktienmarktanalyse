import matplotlib.pyplot as plt


def plot_predictions(actual, predicted, title):
    """Visualisiert tatsächliche und vorhergesagte Werte."""
    plt.figure(figsize=(10, 6))
    plt.plot(actual, label='Actual Prices')
    plt.plot(predicted, label='Predicted Prices')
    plt.title(title)
    plt.legend()
    plt.show()
