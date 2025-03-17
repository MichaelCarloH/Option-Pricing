# Option Pricing

This repository contains application of Heston and Black-scholes models and techniques for pricing financial options. The focus is on closely match market structure using the Black-Scholes model, visualizing implied volatility surfaces, and utilizing Monte Carlo simulations and FFT pricing for exotic option pricing using the Heston model.


## Folder Structure:
### `tiny_pricing_utils/` 
 - This folder is the source code for a python library to price derivatives using FFT and monetcarlo methods for BS and Heston.
 - Available at: https://pypi.org/project/tiny-pricing-utils/
 - Documentation: https://option-pricing-1ld1qd386-michael-carlos-projects.vercel.app/
   
### 'Option pricing/'

### `Black_Scholes_Pricing`
   - This folder contains notebooks related to the Black-Scholes option pricing model.
   - **`black_scholes_calibration.ipynb`**: Calibrates the Black-Scholes model to find the optimal volatility.
   - **`implied_vol_surface.ipynb`**: Finds and visualizes the implied volatility surface based on market data.
   - **`exotic_montecarlo_pricing.ipynb`**: Implements Monte Carlo simulations for pricing Asian and Barrier options.

### `Heston_Pricing`
   - This folder contains notebooks and scripts related to option pricing using the **Heston model** and numerical integration methods.
   - **`Heston_FFT_pricing.ipynb`**: Implements call option pricing using the Heston model.
   - **`Carr_Madan_formula.ipynb`**: Uses the Carr-Madan formula with **Rectangular Rule** and **Simpson's Rule** for pricing options under the Heston model.
   - **`BS_FFT_pricing.ipynb`**: Implements call option pricing using the Black-Scholes model.

### `Heston_calibration`
   - This folder contains notebooks and scripts related to option pricing using the **Heston model** using Montecarlo simulations.
   - **`Heston_calibration.ipynb`**: Implements call option pricing using the Heston model using Euler and Milstein Montecarlo methods.

## Requirements:
- Python 3.x
- Necessary libraries: `numpy`, `pandas`, `matplotlib`, `scipy`, `ipython`, etc.

## Setup:
To get started, make sure all dependencies are installed. You can install the necessary Python packages using:

```bash
pip install -r requirements.txt
