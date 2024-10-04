from src.data_fetcher import fetch_historical_data
from src.data_cleaner import clean_data
from datetime import datetime, timedelta

def main():
    # Set date range to the last week
    end_date = datetime.now().date()  # Today
    start_date = end_date - timedelta(days=7)  # One week ago
    
    ticker = 'SPY'
    
    # Fetch historical data
    data = fetch_historical_data(ticker, start_date, end_date, interval='1m')
    print(f"Fetched data shape: {data.shape}")  # Check how much data was fetched
    
    # Clean the data
    cleaned_data = clean_data(data)
    print("Data cleaned successfully!")

    # Display the cleaned data
    print(cleaned_data)

if __name__ == "__main__":
    main()
