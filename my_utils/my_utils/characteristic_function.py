import numpy as np

def characteristic_function(u, S0, r, q, sigma, T):
    """
    Computes the characteristic function of the log-stock price under the Black-Scholes model.

    Parameters:
        u (complex or float): Fourier transform variable
        S0 (float): Initial stock price
        r (float): Risk-free rate
        q (float): Dividend yield
        sigma (float): Volatility
        T (float): Time to maturity

    Returns:
        complex: Characteristic function value at u
    """
    return np.exp(1j * u * (np.log(S0) + (r - q - 0.5 * sigma**2) * T) - 0.5 * u**2 * sigma**2 * T)
