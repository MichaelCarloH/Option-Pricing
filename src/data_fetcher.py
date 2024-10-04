import yfinance as yf
import pandas as pd
import os
from datetime import datetime, timedelta

DATA_DIR = 'data'  # Define the directory to store data

def fetch_historical_data(ticker, start_date, end_date, interval='1m'):
    """
    Fetch historical stock data from Yahoo Finance.
    
    Parameters:
    - ticker: Stock ticker symbol (e.g., 'AAPL', 'SPY')
    - start_date: Start date for the historical data
    - end_date: End date for the historical data
    - interval: Data interval (default is '1m')

    Returns:
    - DataFrame containing the historical stock data
    """
    data = yf.download(ticker, start=start_date, end=end_date, interval=interval)
    return data

def save_data_to_csv(data, ticker):
    """
    Save the DataFrame to a CSV file.
    
    Parameters:
    - data: DataFrame containing the stock data
    - ticker: Stock ticker symbol for naming the file
    """
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)  # Create the data directory if it doesn't exist

    filename = os.path.join(DATA_DIR, f"{ticker}_data.csv")
    data.to_csv(filename)
    print(f"Data saved to {filename}")

def load_data_from_csv(ticker):
    """
    Load historical stock data from a CSV file.
    
    Parameters:
    - ticker: Stock ticker symbol for identifying the file

    Returns:
    - DataFrame containing the stock data or None if file doesn't exist
    """
    filename = os.path.join(DATA_DIR, f"{ticker}_data.csv")
    if os.path.exists(filename):
        return pd.read_csv(filename, index_col=0, parse_dates=True)
    else:
        return None

if __name__ == "__main__":
    # Example usage
    end_date = datetime.now().date()
    start_date = end_date - timedelta(days=7)  # Fetch the last week of data
    ticker = 'SPY'
    
    # Try loading data from CSV
    local_data = load_data_from_csv(ticker)
    if local_data is not None:
        print("Loaded data from local CSV.")
        spy_data = local_data
    else:
        # Fetch historical data if not found locally
        spy_data = fetch_historical_data(ticker, start_date, end_date, interval='1m')
        save_data_to_csv(spy_data, ticker)  # Save data for future use
    
    print(spy_data.head())
