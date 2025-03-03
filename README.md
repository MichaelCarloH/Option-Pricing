# Option Pricing

This repository contains various models and techniques for pricing financial options. The focus is on implementing the Black-Scholes model, visualizing implied volatility surfaces, and utilizing Monte Carlo simulations for exotic option pricing.

## Folder Structure:

### `Black_Scholes_Pricing`
   - This folder contains notebooks related to the Black-Scholes option pricing model.
   - **`black_scholes_calibration.ipynb`**: Calibrates the Black-Scholes model to find the optimal volatility.
   - **`implied_vol_surface.ipynb`**: Finds and visualizes the implied volatility surface based on market data.
   - **`exotic_montecarlo_pricing.ipynb`**: Implements Monte Carlo simulations for pricing Asian and Barrier options.

## Requirements:
- Python 3.x
- Necessary libraries: `numpy`, `pandas`, `matplotlib`, `scipy`, `ipython`, etc.

## Setup:
To get started, make sure all dependencies are installed. You can install the necessary Python packages using:

```bash
pip install -r requirements.txt
