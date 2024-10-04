import yfinance as yf
import pandas as pd

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

if __name__ == "__main__":
    # Example usage
    ticker = 'SPY'
    start_date = '2023-01-01'
    end_date = '2023-01-02'
    spy_data = fetch_historical_data(ticker, start_date, end_date, interval='1m')
    
    print(spy_data.head())
