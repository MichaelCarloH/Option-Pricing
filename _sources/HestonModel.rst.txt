Heston Model
=============

The Heston model is used for option pricing by incorporating stochastic volatility into the Black-Scholes framework. This class provides methods for computing option prices using Fourier Transform methods.

Class: `HestonModel`
---------------------

The `HestonModel` class models the price of options under the Heston stochastic volatility model. 

**Constructor**
The constructor initializes the Heston model with the given parameters. The parameters are:

- **S0** (float): Initial stock price.
- **r** (float): Risk-free rate.
- **q** (float): Dividend yield.
- **V0** (float, default=0.05): Initial variance.
- **kappa** (float, default=0.5): Rate of mean reversion.
- **eta** (float, default=0.05): Long-term mean of volatility.
- **theta** (float, default=0.2): Volatility of volatility.
- **rho** (float, default=-0.75): Correlation between stock price and volatility.
- **T** (float, default=1): Time to maturity.
- **alpha** (float, default=1.5): Fourier transform parameter.
- **N** (int, default=4096): Number of grid points.
- **eta_cm** (float, default=0.25): Fourier grid spacing.
- **b** (float, optional): Upper limit for Fourier transform integration.
- **strikes** (array-like, optional): Specific strike prices for interpolation.

**Methods**

.. function:: calculate_auxiliary_variables()

   This method calculates the auxiliary variables required for the Fourier transform, such as log strikes, `v`, `u`, and `rho_cm`.

.. function:: compute_fft(rule, simpson_weights=None)

   Computes the FFT based on the specified integration rule. It can use either the rectangular rule or Simpson's rule.

   **Parameters:**
   - **rule** (str): The integration rule to use ("rectangular" or "simpson").
   - **simpson_weights** (array, optional): Weights to apply if using Simpson's rule.

.. function:: compute_fft_rectangular()

   Computes option prices using FFT with the rectangular rule. It calculates the real part of the FFT result to obtain the call option prices.

.. function:: compute_fft_simpson()

   Computes option prices using FFT with Simpson's rule. It applies Simpson's rule correction during the FFT computation.

.. function:: interpolate_prices()

   Interpolates the computed option prices for specific strikes using cubic interpolation.

.. function:: price_options(rule)

   Prices options based on the selected integration rule ("rectangular" or "simpson"). It computes the FFT and interpolates the option prices.

   **Parameters:**
   - **rule** (str): The integration rule to use ("rectangular" or "simpson").

   **Returns:**
   - (dict): A dictionary containing the computed option prices.

Example Usage

```python
from tiny_pricing_utils.HestonModel import HestonModel

# Initialize Heston model with parameters
heston_model = HestonModel(S0=100, r=0.05, q=0.01, V0=0.05, kappa=0.5, 
                           eta=0.05, theta=0.2, rho=-0.75, T=1, alpha=1.5, 
                           N=4096, eta_cm=0.25, strikes=[90, 100, 110])

# Compute option prices using rectangular rule
option_prices = heston_model.price_options(rule="rectangular")

# Print computed prices
print(option_prices)
