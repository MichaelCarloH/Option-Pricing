from src.data_fetcher import fetch_historical_data
from src.data_cleaner import clean_data  # If you have specific cleaning logic
from src.analysis import plot_price_data, calculate_log_returns, calculate_volatility
from datetime import datetime, timedelta

def main():
    # Set date range to the last week
    end_date = datetime.now().date()
    start_date = end_date - timedelta(days=7)
    
    ticker = 'SPY'
    
    # Fetch historical data
    data = fetch_historical_data(ticker, start_date, end_date, interval='1m')
    print(f"Fetched data shape: {data.shape}")
    
    # Clean the data
    cleaned_data = clean_data(data)
    print("Data cleaned successfully!")

    # Calculate log returns
    cleaned_data = calculate_log_returns(cleaned_data)
    
    # Calculate volatility
    cleaned_data = calculate_volatility(cleaned_data)
    
    # Plot price data
    plot_price_data(cleaned_data)

    # Display the cleaned data
    print(cleaned_data.head())

if __name__ == "__main__":
    main()
