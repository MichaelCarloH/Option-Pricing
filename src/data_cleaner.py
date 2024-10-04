import pandas as pd

def clean_data(data):
    """
    Clean the historical stock data.
    
    Parameters:
    - data: DataFrame containing the stock data

    Returns:
    - Cleaned DataFrame
    """
    # Drop any rows with missing values
    cleaned_data = data.dropna()
    
    return cleaned_data

if __name__ == "__main__":
    # Example usage
    # Replace this with actual data fetching if needed
    sample_data = pd.DataFrame({
        'Close': [100, 101, None, 102],
        'Volume': [1000, 1500, 2000, None]
    })

    cleaned_data = clean_data(sample_data)
    print(cleaned_data)
