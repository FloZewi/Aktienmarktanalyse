# Aktienmarktanalyse

# Aktienmarktanalyse mit TensorFlow

Dieses Projekt analysiert Aktienmarktdaten mithilfe von **Machine Learning** und erstellt Investitionsempfehlungen basierend auf Vorhersagen der zukünftigen Kursentwicklungen. Es verwendet **TensorFlow** für die Modellierung und **Python** für die Datenverarbeitung und Visualisierung.

---

## 🚀 Features
- **Datenbeschaffung**: Automatisches Laden historischer Aktienmarktdaten von Yahoo Finance.
- **Datenverarbeitung**: Vorbereitung und Skalierung der Daten für die Modellierung.
- **Modellierung**: Einsatz eines LSTM-Modells (Long Short-Term Memory), um Kursentwicklungen vorherzusagen.
- **Investitionsempfehlungen**: Generierung einer Liste von Aktien, in die investiert werden könnte.
- **Visualisierung**: Darstellung der Vorhersagen und tatsächlichen Kurse in Diagrammen.

---

## 🛠️ Technologien und Bibliotheken
- **Programmiersprache**: Python
- **Bibliotheken**:
  - [TensorFlow](https://www.tensorflow.org/)
  - [Pandas](https://pandas.pydata.org/)
  - [NumPy](https://numpy.org/)
  - [Matplotlib](https://matplotlib.org/)
  - [scikit-learn](https://scikit-learn.org/)
  - [yfinance](https://pypi.org/project/yfinance/)

---

## 📂 Projektstruktur

```plaintext
Aktienmarktanalyse/
│
├── data/                       # Datenspeicher (z. B. historische Kursdaten)
│   ├── stock_data.csv          # Beispiel: Rohdaten
│   ├── processed_data.csv      # Beispiel: Verarbeitete Daten
│
├── src/                        # Source-Code-Verzeichnis
│   ├── data_fetcher.py         # Modul für Datenbeschaffung
│   ├── data_processor.py       # Modul für Datenverarbeitung
│   ├── model.py                # Modul für das LSTM-Modell
│   ├── recommender.py          # Modul für Empfehlungen
│   ├── visualization.py        # Modul für die Visualisierung
│
├── main.py                     # Hauptskript
├── requirements.txt            # Liste der Abhängigkeiten
└── README.md                   # Beschreibung des Projekts
