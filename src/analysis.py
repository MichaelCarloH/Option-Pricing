# src/analysis.py

import matplotlib.pyplot as plt
import numpy as np

def plot_price_data(data):
    plt.figure(figsize=(12, 6))
    plt.plot(data.index, data['Close'], label='Close Price', color='blue')
    plt.title('SPY Close Price Over Time')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid()
    plt.show()

def calculate_log_returns(data):
    data['Log Return'] = np.log(data['Close'] / data['Close'].shift(1))
    return data

def calculate_volatility(data, window=10):
    data['Volatility'] = data['Log Return'].rolling(window=window).std() * np.sqrt(252)  # Annualized volatility
    return data
