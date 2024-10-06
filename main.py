from src.data_fetcher import fetch_historical_data, save_data_to_csv, load_data_from_csv
from src.data_cleaner import clean_data, filter_trading_hours
from src.analysis_price_time import plot_price_data, calculate_log_returns, calculate_volatility
from src.analysis_volume_time import plot_volume_over_time
from datetime import datetime, timedelta

def main():
    # Set date range to the last week
    end_date = datetime.now().date()
    start_date = end_date - timedelta(days=7)
    
    ticker = 'SPY'
    
    # Load data from CSV
    local_data = load_data_from_csv(ticker)
    if local_data is not None:
        print("Loaded data from local CSV.")
        data = local_data
    else:
        # Fetch historical data if not found locally
        data = fetch_historical_data(ticker, start_date, end_date, interval='1m')
        save_data_to_csv(data, ticker)  # Save data for future use
    
    print(f"Fetched data shape: {data.shape}")
    
    # Clean the data
    cleaned_data = clean_data(data)
    print("Data cleaned successfully!")
    
    # Filter for trading hours
    cleaned_data = filter_trading_hours(cleaned_data)
    
    # Calculate log returns
    cleaned_data = calculate_log_returns(cleaned_data)
    
    # Calculate volatility
    cleaned_data = calculate_volatility(cleaned_data)
    
    # Plot price data
    plot_price_data(cleaned_data)

    #Plot volume data
    plot_volume_over_time(cleaned_data)

    # Display the cleaned data
    print(cleaned_data.head())

if __name__ == "__main__":
    main()
