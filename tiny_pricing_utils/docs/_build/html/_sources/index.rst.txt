Welcome to the Option Pricing Utils Documentation!
===================================================

This library contains utilities for option pricing, including Black-Scholes, Monte Carlo simulations, and characteristic functions. Below is the overview of the main modules and their functionality.

Contents:
----------
.. toctree::
   :maxdepth: 2
   :caption: Modules:

   black_scholes
   characteristic_function
   montecarlo

black_scholes.py
================

The `black_scholes.py` module provides the implementation of the Black-Scholes pricing model with dividends.

Functions:
----------
1. `black_scholes_price(S, K, T, r, q, sigma, option_type)`: Computes the price of European call and put options under the Black-Scholes model.
2. `sum_squared_diff(sigma, S0, K, T, r, q, market_prices, option_type)`: Calculates the sum of squared differences between model prices and market prices for calibration.

characteristic_function.py
==========================

The `characteristic_function.py` module contains functions for computing characteristic functions under the Black-Scholes and Heston models.

Functions:
----------
1. `cf_BlackScholes(u, S0, r, q, sigma, T)`: Computes the characteristic function for the Black-Scholes model.
2. `cf_Heston(u, S0, r, q, V0, kappa, eta, theta, rho, T)`: Computes the characteristic function for the Heston model, incorporating stochastic volatility.

montecarlo.py
=============

The `montecarlo.py` module includes Monte Carlo simulations for pricing different types of options.

Functions:
----------
1. `simulate_stock_paths(S0, r, q, sigma, T, N, M)`: Simulates stock price paths using the geometric Brownian motion model.
2. `price_asian_call(S0, K, r, q, sigma, T, N, M)`: Prices an Asian call option using Monte Carlo simulation.
3. `price_up_and_in_put(S0, K, H, r, q, sigma, T, N, M)`: Prices an up-and-in put option using Monte Carlo simulation.
4. `price_up_and_out_put(S0, K, H, r, q, sigma, T, N, M)`: Prices an up-and-out put option using Monte Carlo simulation.

Installation
============
To install the package, run:

.. code-block:: bash

   pip install option-pricing-utils

Usage
=====
To use the module, import the functions as follows:

.. code-block:: python

   from black_scholes import black_scholes_price
   from montecarlo import price_asian_call
