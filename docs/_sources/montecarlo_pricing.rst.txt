Option Pricing Functions
========================

This module provides various functions for pricing options using different models for stock paths. The functions use Monte Carlo simulations to estimate the option prices.

Functions
---------

.. function:: price_european_call(S0, K, r, q, sigma, T, N, M)

   Prices a European call option using Monte Carlo simulation based on the Geometric Brownian Motion model.

   **Parameters:**
   - **S0** (*float*): Initial stock price.
   - **K** (*float*): Strike price.
   - **r** (*float*): Risk-free rate.
   - **q** (*float*): Dividend yield.
   - **sigma** (*float*): Volatility.
   - **T** (*float*): Time to maturity.
   - **N** (*int*): Number of time steps.
   - **M** (*int*): Number of simulations.

   **Returns:**
   - (*float*): The price of the European call option.

.. function:: price_european_put(S0, K, r, q, sigma, T, N, M)

   Prices a European put option using Monte Carlo simulation based on the Geometric Brownian Motion model.

   **Parameters:**
   - **S0** (*float*): Initial stock price.
   - **K** (*float*): Strike price.
   - **r** (*float*): Risk-free rate.
   - **q** (*float*): Dividend yield.
   - **sigma** (*float*): Volatility.
   - **T** (*float*): Time to maturity.
   - **N** (*int*): Number of time steps.
   - **M** (*int*): Number of simulations.

   **Returns:**
   - (*float*): The price of the European put option.

.. function:: price_heston_euler_call(S0, K, r, q, v0, kappa, eta, theta, rho, T, N, M)

   Prices a European call option using Monte Carlo simulation based on the Heston model with Euler discretization.

   **Parameters:**
   - **S0** (*float*): Initial stock price.
   - **K** (*float*): Strike price.
   - **r** (*float*): Risk-free rate.
   - **q** (*float*): Dividend yield.
   - **v0** (*float*): Initial variance.
   - **kappa** (*float*): Rate of mean reversion.
   - **eta** (*float*): Volatility of volatility.
   - **theta** (*float*): Long-term variance.
   - **rho** (*float*): Correlation between stock and variance.
   - **T** (*float*): Time to maturity.
   - **N** (*int*): Number of time steps.
   - **M** (*int*): Number of simulations.

   **Returns:**
   - (*float*): The price of the European call option under the Heston model.

.. function:: price_heston_euler_put(S0, K, r, q, v0, kappa, eta, theta, rho, T, N, M)

   Prices a European put option using Monte Carlo simulation based on the Heston model with Euler discretization.

   **Parameters:**
   - **S0** (*float*): Initial stock price.
   - **K** (*float*): Strike price.
   - **r** (*float*): Risk-free rate.
   - **q** (*float*): Dividend yield.
   - **v0** (*float*): Initial variance.
   - **kappa** (*float*): Rate of mean reversion.
   - **eta** (*float*): Volatility of volatility.
   - **theta** (*float*): Long-term variance.
   - **rho** (*float*): Correlation between stock and variance.
   - **T** (*float*): Time to maturity.
   - **N** (*int*): Number of time steps.
   - **M** (*int*): Number of simulations.

   **Returns:**
   - (*float*): The price of the European put option under the Heston model.

.. function:: price_heston_milstein_call(S0, K, r, q, v0, kappa, eta, theta, rho, T, N, M)

   Prices a European call option using Monte Carlo simulation based on the Heston model with Milstein discretization.

   **Parameters:**
   - **S0** (*float*): Initial stock price.
   - **K** (*float*): Strike price.
   - **r** (*float*): Risk-free rate.
   - **q** (*float*): Dividend yield.
   - **v0** (*float*): Initial variance.
   - **kappa** (*float*): Rate of mean reversion.
   - **eta** (*float*): Volatility of volatility.
   - **theta** (*float*): Long-term variance.
   - **rho** (*float*): Correlation between stock and variance.
   - **T** (*float*): Time to maturity.
   - **N** (*int*): Number of time steps.
   - **M** (*int*): Number of simulations.

   **Returns:**
   - (*float*): The price of the European call option under the Heston model with Milstein discretization.

.. function:: price_heston_milstein_put(S0, K, r, q, v0, kappa, eta, theta, rho, T, N, M)

   Prices a European put option using Monte Carlo simulation based on the Heston model with Milstein discretization.

   **Parameters:**
   - **S0** (*float*): Initial stock price.
   - **K** (*float*): Strike price.
   - **r** (*float*): Risk-free rate.
   - **q** (*float*): Dividend yield.
   - **v0** (*float*): Initial variance.
   - **kappa** (*float*): Rate of mean reversion.
   - **eta** (*float*): Volatility of volatility.
   - **theta** (*float*): Long-term variance.
   - **rho** (*float*): Correlation between stock and variance.
   - **T** (*float*): Time to maturity.
   - **N** (*int*): Number of time steps.
   - **M** (*int*): Number of simulations.

   **Returns:**
   - (*float*): The price of the European put option under the Heston model with Milstein discretization.

.. function:: price_asian_call(S0, K, r, q, sigma, T, N, M)

   Prices an Asian call option using Monte Carlo simulation based on the Geometric Brownian Motion model.

   **Parameters:**
   - **S0** (*float*): Initial stock price.
   - **K** (*float*): Strike price.
   - **r** (*float*): Risk-free rate.
   - **q** (*float*): Dividend yield.
   - **sigma** (*float*): Volatility.
   - **T** (*float*): Time to maturity.
   - **N** (*int*): Number of time steps.
   - **M** (*int*): Number of simulations.

   **Returns:**
   - (*float*): The price of the Asian call option.

.. function:: price_up_and_in_put(S0, K, H, r, q, sigma, T, N, M)

   Prices an up-and-in put option using Monte Carlo simulation based on the Geometric Brownian Motion model. The option becomes active when the stock price hits the barrier.

   **Parameters:**
   - **S0** (*float*): Initial stock price.
   - **K** (*float*): Strike price.
   - **H** (*float*): Barrier level.
   - **r** (*float*): Risk-free rate.
   - **q** (*float*): Dividend yield.
   - **sigma** (*float*): Volatility.
   - **T** (*float*): Time to maturity.
   - **N** (*int*): Number of time steps.
   - **M** (*int*): Number of simulations.

   **Returns:**
   - (*float*): The price of the up-and-in put option.

.. function:: price_up_and_out_put(S0, K, H, r, q, sigma, T, N, M)

   Prices an up-and-out put option using Monte Carlo simulation based on the Geometric Brownian Motion model. The option becomes inactive if the stock price hits the barrier.

   **Parameters:**
   - **S0** (*float*): Initial stock price.
   - **K** (*float*): Strike price.
   - **H** (*float*): Barrier level.
   - **r** (*float*): Risk-free rate.
   - **q** (*float*): Dividend yield.
   - **sigma** (*float*): Volatility.
   - **T** (*float*): Time to maturity.
   - **N** (*int*): Number of time steps.
   - **M** (*int*): Number of simulations.

   **Returns:**
   - (*float*): The price of the up-and-out put option.
