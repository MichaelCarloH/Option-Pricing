Black-Scholes Option Pricing
=============================

This module contains functions for calculating the Black-Scholes price for European call and put options, 
as well as a function for calibrating implied volatility by minimizing the sum of squared differences between 
Black-Scholes prices and market prices.

Functions
---------

.. function:: black_scholes_price(S, K, T, r, q, sigma, option_type)

   Computes the Black-Scholes price for European call and put options with dividends.

   **Parameters:**
   
   - **S** (*float*): Current stock price.
   - **K** (*float*): Strike price.
   - **T** (*float*): Time to maturity (years).
   - **r** (*float*): Risk-free interest rate.
   - **sigma** (*float*): Volatility of the underlying asset.
   - **option_type** (*int*): 0 for call option, 1 for put option.
   - **q** (*float*): Dividend yield (default is 0, no dividend).

   **Returns:**
   
   - (*float*): Option price.

   **Example:**
   
   .. code-block:: python

      price = black_scholes_price(S=100, K=95, T=1, r=0.05, q=0, sigma=0.2, option_type=0)
