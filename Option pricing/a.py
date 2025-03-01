import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# Given Data
data = np.array([
    [30000,  15.0, 25.0, 139.68, -0.00027],
    [40000,  0.0, 40.0, np.nan, -0.00216],  # IV is NaN
    [45000,  35.0, 50.0, 101.45, -0.00367],
    [50000,  25.0, 70.0, 85.02, -0.00575],
    [55000,  50.0, 80.0, 79.61, -0.00862],
    [60000,  100.0, 115.0, 74.91, -0.01359],
    [65000,  145.0, 160.0, 67.21, -0.02067],
    [70000,  230.0, 235.0, 60.71, -0.03293],
    [75000,  380.0, 400.0, 54.80, -0.05569],
    [80000,  700.0, 720.0, 50.45, -0.09871],
    [85000,  1360.0, 1375.0, 47.53, -0.17731],
    [88000,  2020.0, 2050.0, 46.42, -0.24491],
    [90000,  2620.0, 2670.0, 46.09, -0.29844],
    [92000,  3350.0, 3400.0, 45.91, -0.35652],
    [94000,  4225.0, 4280.0, 45.95, -0.41741]
])

# Extract Data
strikes_given = data[:, 0]
iv_given = data[:, 3]

# Step 1: Linearly interpolate missing values
nan_mask = np.isnan(iv_given)  # Find NaNs
interp_linear = interp1d(strikes_given[~nan_mask], iv_given[~nan_mask], kind='linear', fill_value="extrapolate")
iv_given[nan_mask] = interp_linear(strikes_given[nan_mask])  # Replace NaNs with interpolated values

# Step 2: Generate 4096 new strike points
strikes_dense = np.linspace(min(strikes_given), max(strikes_given), 4096)

# Step 3: Use cubic spline interpolation for smooth IV curve
interp_cubic = interp1d(strikes_given, iv_given, kind='cubic')
iv_dense = interp_cubic(strikes_dense)

# Step 4: Plot Original, Linear Interpolated, and Dense Interpolated Data
plt.figure(figsize=(10, 5))

# Plot given data points (before interpolation)
plt.scatter(strikes_given, iv_given, color='red', label="Given Data (Linear Interpolated)", zorder=3)

# Plot smooth cubic spline interpolation
plt.plot(strikes_dense, iv_dense, 'b-', label="Cubic Spline (4096 points)", zorder=2)

# Formatting
plt.xlabel("Strike Price")
plt.ylabel("Implied Volatility")
plt.title("Implied Volatility vs. Strike Price (Linear & Cubic Interpolation)")
plt.legend()
plt.grid(True)

# Step 5: Show the plot
plt.show()
