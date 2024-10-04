import pandas as pd

def clean_data(data):
    """
    Clean the historical stock data.
    
    Parameters:
    - data: DataFrame containing the stock data

    Returns:
    - Cleaned DataFrame
    """
    # Interpolate missing values for 'Close' and 'Volume'
    data['Close'] = data['Close'].interpolate(method='time')
    data['Volume'] = data['Volume'].interpolate(method='time')
    
    # Drop any rows that are still missing after interpolation
    cleaned_data = data.dropna()
    
    return cleaned_data

if __name__ == "__main__":
    # Example usage
    sample_data = pd.DataFrame({
        'Close': [100, 101, None, 102],
        'Volume': [1000, 1500, 2000, None]
    }, index=pd.date_range(start='2024-01-01', periods=4, freq='D'))

    cleaned_data = clean_data(sample_data)
    print(cleaned_data)
