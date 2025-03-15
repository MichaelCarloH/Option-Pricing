import pytest
import numpy as np
from tiny_pricing_utils.heston_model import HestonModel  # Import the Heston model from your module
from tiny_pricing_utils.characteristic_function import cf_Heston
from scipy.interpolate import interp1d


def test_heston_model():
    # Given data for Heston model pricing
    eta_cm = 0.25
    N = 4096
    alpha = 1.5
    lambda_ = (2 * np.pi) / (N * eta_cm)
    b = (N * lambda_) / 2

    S0 = 100
    q = 0.01
    r = 0.05
    V0 = 0.05
    kappa = 0.5
    eta = 0.05
    theta = 0.2
    rho = -0.75
    T = 1  # Time to expiration (3 months)
    K = [90, 100, 110]  # Strike prices

    # Specific strikes for interpolation
    strikes = np.array([90, 100, 110])

    # Create an instance of the Heston model with the provided data
    heston = HestonModel(S0=S0, r=r, q=q, V0=V0, kappa=kappa, eta=eta, theta=theta, rho=rho, T=T, 
                         alpha=alpha, N=N, eta_cm=eta_cm, b=b, strikes=strikes)

    # Simpson's Rule coefficients for pricing
    simpson_1 = 1 / 3  # First coefficient
    simpson_weights = (3 + (-1) ** np.arange(2, N + 1)) / 3  # Alternating coefficients starting from index 2
    simpson_weights = np.concatenate(([simpson_1], simpson_weights))  # Combine with the first coefficient

    # Price options using Simpson's rule
    option_prices_simpson = heston.price_options(rule="simpson", simpson_weights=simpson_weights)

    # Updated expected prices (for example purposes, these should be trusted reference values)
    expected_prices_simpson = np.array([16.93747985, 10.6163149, 5.86707143])

    # Test if the computed prices are close enough to the expected prices for Simpson's rule
    np.testing.assert_allclose(option_prices_simpson, expected_prices_simpson, rtol=1e-4, atol=1e-4)

    # Print results for visual confirmation
    print(f"Interpolated Option Prices using Simpson's Rule: {option_prices_simpson}")


# To run the test, use the following command:
# pytest <name_of_test_file>.py
