import numpy as np
import matplotlib.pyplot as plt

def plot_fourier_transform(data, column='Volume', sampling_rate=1):
    """
    Perform Fourier Transform on a given column of data (default is 'Volume').
    
    Parameters:
    - data: DataFrame containing the stock data with 'Datetime' as the index
    - column: The column to perform the Fourier Transform on (default is 'Volume')
    - sampling_rate: Time interval between data points in minutes (default is 1 minute)
    
    Returns:
    - frequencies: Frequencies identified from the Fourier Transform
    - power_spectrum: Power of each frequency
    """
    # Remove NaN values from the data (if any)
    data = data.dropna(subset=[column])
    
    # Apply FFT to the volume data
    volume_data = data[column].values
    n = len(volume_data)  # Number of samples
    fft_result = np.fft.fft(volume_data)  # FFT result (complex numbers)
    power_spectrum = np.abs(fft_result)  # Power spectrum (magnitude of FFT)
    
    # Create frequency axis
    frequencies = np.fft.fftfreq(n, d=sampling_rate)  # Sampling rate (d is 1 minute by default)

    # Plot the Fourier Transform (Frequency vs Power)
    plt.figure(figsize=(10, 6))
    plt.plot(frequencies[:n // 2], power_spectrum[:n // 2], color='blue')  # Only plot the positive frequencies
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Power')
    plt.title(f'Fourier Transform of {column}')
    plt.grid(True)
    plt.show()

    return frequencies, power_spectrum

# Example usage
if __name__ == "__main__":
    # Assuming `cleaned_data` is your DataFrame with 'Datetime' as the index and 'Volume' as a column
    plot_fourier_transform(cleaned_data)
