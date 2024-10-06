import matplotlib.pyplot as plt
import pandas as pd

def plot_volume_over_time(data, use_log_scale=True, smooth_window=10):
    """
    Plot volume over time with optional log scale and smoothing.
    
    Parameters:
    - data: DataFrame containing the stock data with 'Volume' and 'Datetime' as the index
    - use_log_scale: If True, use a logarithmic scale for the volume axis
    - smooth_window: Window size for rolling average smoothing (default is 10)
    """
    plt.figure(figsize=(10, 6))
    
    # Apply smoothing (rolling average) to the volume data
    smoothed_volume = data['Volume'].rolling(window=smooth_window).mean()
    
    # Plot original volume data with transparency for comparison
    plt.plot(data.index, data['Volume'], label='Original Volume', color='blue', alpha=0.3)
    
    # Plot smoothed volume data
    plt.plot(data.index, smoothed_volume, label=f'Smoothed Volume (window={smooth_window})', color='red')
    
    # Use a logarithmic scale if specified
    if use_log_scale:
        plt.yscale('log')
    
    plt.xlabel('Time')
    plt.ylabel('Volume')
    plt.title('Volume over Time (Smoothed)')
    
    # Rotate x-axis labels for better readability
    plt.xticks(rotation=45)
    
    plt.legend()
    plt.tight_layout()  # Ensures everything fits without overlapping
    plt.show()

# Example usage
if __name__ == "__main__":
    # Assuming `cleaned_data` is your DataFrame with 'Datetime' as the index and 'Volume' as a column
    plot_volume_over_time(cleaned_data)
