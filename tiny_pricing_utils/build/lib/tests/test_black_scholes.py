import pytest
import numpy as np
from tiny_pricing_utils.black_scholes import black_scholes_price  # Correct import

def test_black_scholes():
    # Given data
    S0 = 100
    q = 0.01
    r = 0.05
    sigma = 0.25
    K = [90, 95, 100, 105, 110]
    T = 3 / 12  # Time to expiration (3 months)

    # Expected call prices calculated manually or from an external source
    expected_prices = np.array([12.0002, 8.3561, 5.4584, 3.3385, 1.9129])

    # List to store the computed call prices from black_scholes_price function
    computed_prices = []
    for strike in K:
        call_price = black_scholes_price(S0, strike, T, r, q, sigma, 0)
        computed_prices.append(round(call_price, 4))  # Round to match the expected precision

    computed_prices_array = np.array(computed_prices)

    # Test if the computed prices are close enough to the expected prices
    np.testing.assert_allclose(computed_prices_array, expected_prices, rtol=1e-4, atol=1e-4)
