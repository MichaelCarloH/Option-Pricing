import pytest
import numpy as np
from tiny_pricing_utils.montecarlo_pricing import price_heston_euler_call  # Import the Monte Carlo pricing function

# Define the test function for European call option pricing using Monte Carlo
def test_montecarlo_option_pricing():
    # Given data for European call option pricing
    S0 = 100  # Initial stock price
    r = 0.05  # Risk-free rate
    q = 0.01  # Dividend yield
    sigma = 0.2  # Volatility
    T = 1  # Time to expiration (in years)
    rho = -0.75
    kappa = 0.5
    theta = 0.2
    eta = 0.05
    v0 = 0.05
    N = 252  # Number of time steps
    M = 100000  # Number of Monte Carlo simulations
    K = [90, 100, 110]  # Strike prices

    # Expected prices for the given strikes (for example, from a trusted source)
    expected_prices = np.array([16.97, 10.67, 5.88])

    # Price options using Monte Carlo for different strike prices
    computed_prices = []
    for K_strike in K:
        price = price_heston_euler_call(S0, K_strike, r, q, v0, kappa, eta, theta, rho, T, N, M)
        computed_prices.append(price)

    # Convert computed prices to a numpy array for easier comparison
    computed_prices = np.array(computed_prices)

    # Assert that the computed prices are close to the expected prices
    np.testing.assert_allclose(computed_prices, expected_prices, rtol=1e-2, atol=1e-2)

    # Print results for visual confirmation
    print(f"Computed Option Prices using Monte Carlo: {computed_prices}")
    print(f"Expected Option Prices: {expected_prices}")


