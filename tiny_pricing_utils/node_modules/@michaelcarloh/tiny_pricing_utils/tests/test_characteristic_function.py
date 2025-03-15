import pytest
from tiny_pricing_utils.characteristic_function import *
import numpy as np

def test_characteristic_function():
    # Given data
    N = 4096
    alpha = 1.5
    eta = 0.25
    S0 = 100
    T = 1
    r = 0.05
    q = 0
    sigma = 0.2
    u = 1

    # Call characteristic function with the provided values
    phi_BS = cf_BlackScholes(u, S0, r, q, sigma, T)

    # Round real and imaginary parts to match expected output
    phi_BS = complex(round(phi_BS.real, 4), round(phi_BS.imag, 4))

    # Expected value from manual calculation or external source
    expected_value = complex(-0.0756, -0.9773)

    # Test if the computed value is close enough to the expected value
    assert np.allclose([phi_BS.real, phi_BS.imag], [expected_value.real, expected_value.imag], atol=1e-4)
