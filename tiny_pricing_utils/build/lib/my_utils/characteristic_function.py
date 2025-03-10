import numpy as np

def cf_BlackScholes(u, S0, r, q, sigma, T):
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


def cf_Heston(u, S0, r, q, V0, kappa, eta, theta, rho, T):
    """
    Computes the characteristic function of the log-stock price under the Heston model.
    
    The Heston model allows for stochastic volatility, where volatility follows a mean-reverting process.

    Parameters:
        u (complex or float): Fourier transform variable. This is the variable for which the characteristic function is computed.
        S0 (float): Initial stock price at time t = 0.
        r (float): Risk-free rate. This is the rate of return on a risk-free asset.
        q (float): Dividend yield. This is the annual dividend yield of the stock.
        V0 (float): Initial variance. This is the starting value for the volatility.
        kappa (float): Rate of mean reversion. This is the speed at which volatility reverts to its long-term mean (eta).
        eta (float): Long-term mean of volatility. This is the value to which volatility reverts over time.
        theta (float): Volatility of volatility. This determines how much volatility fluctuates over time.
        rho (float): Correlation between the stock price and its volatility. A value between -1 and 1.
        T (float): Time to maturity. This is the time in years until the option expires.

    Returns:
        complex: Characteristic function value at u. This value is used in the Fourier inversion to price the option.
    """
    
    i = complex(0, 1)
    d = np.sqrt((rho * theta * u * i - kappa)**2 - (theta**2) * (-i * u - u**2))
    g = (kappa - rho * theta * u * i - d) / (kappa - rho * theta * u * i + d)
    
    term1 = i * u * (np.log(S0) + (r - q) * T)
    term2 = (eta * kappa / theta**2) * ((kappa - rho * theta * u * i - d) * T - 2 * np.log((1 - g * np.exp(-d * T)) / (1 - g)))
    term3 = (V0 / theta**2) * (kappa - rho * theta * u * i - d) * (1 - np.exp(-d * T)) / (1 - g * np.exp(-d * T))
    
    return np.exp(term1 + term2 + term3)