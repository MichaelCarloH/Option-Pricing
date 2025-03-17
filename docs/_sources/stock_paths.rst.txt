Stock Path Simulation Functions
===============================

This module provides functions for simulating stock paths using various stochastic models. The functions are based on the Geometric Brownian Motion model and the Heston model with Euler and Milstein discretizations.

Functions
---------

.. function:: geometric_brownian_motion(S0, r, q, sigma, T, N, M)

   Simulates stock paths using the Geometric Brownian Motion model.

   **Parameters:**
   - **S0** (*float*): Initial stock price.
   - **r** (*float*): Risk-free rate.
   - **q** (*float*): Dividend yield.
   - **sigma** (*float*): Volatility.
   - **T** (*float*): Time to maturity.
   - **N** (*int*): Number of time steps.
   - **M** (*int*): Number of simulations.

   **Returns:**
   - (*ndarray*): Simulated stock paths with shape `(M, N + 1)`.

.. function:: heston_euler(S0, r, q, v0, kappa, eta, theta, rho, T, N, M)

   Simulates stock paths using the Heston model with Euler discretization. The volatility follows a mean-reverting process with stochastic volatility.

   **Parameters:**
   - **S0** (*float*): Initial stock price.
   - **r** (*float*): Risk-free rate.
   - **q** (*float*): Dividend yield.
   - **v0** (*float*): Initial variance.
   - **kappa** (*float*): Rate of mean reversion.
   - **eta** (*float*): Volatility of volatility.
   - **theta** (*float*): Long-term variance.
   - **rho** (*float*): Correlation between the stock price and variance.
   - **T** (*float*): Time to maturity.
   - **N** (*int*): Number of time steps.
   - **M** (*int*): Number of simulations.

   **Returns:**
   - (*ndarray*): Simulated stock paths with shape `(M, N + 1)`.

.. function:: heston_milstein(S0, r, q, v0, kappa, eta, theta, rho, T, N, M)

   Simulates stock paths using the Heston model with Milstein discretization. This method adds a correction term to the volatility process to improve accuracy.

   **Parameters:**
   - **S0** (*float*): Initial stock price.
   - **r** (*float*): Risk-free rate.
   - **q** (*float*): Dividend yield.
   - **v0** (*float*): Initial variance.
   - **kappa** (*float*): Rate of mean reversion.
   - **eta** (*float*): Volatility of volatility.
   - **theta** (*float*): Long-term variance.
   - **rho** (*float*): Correlation between the stock price and variance.
   - **T** (*float*): Time to maturity.
   - **N** (*int*): Number of time steps.
   - **M** (*int*): Number of simulations.

   **Returns:**
   - (*ndarray*): Simulated stock paths with shape `(M, N + 1)`.
