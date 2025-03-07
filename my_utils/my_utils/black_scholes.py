import numpy as np
from scipy.stats import norm

def black_scholes_price(S, K, T, r, sigma, option_type):
    """
    Computes the Black-Scholes price for European call and put options.

    Parameters:
        S (float): Current stock price
        K (float): Strike price
        T (float): Time to maturity (years)
        r (float): Risk-free interest rate
        sigma (float): Volatility of the underlying asset
        option_type (int): 0 for call option, 1 for put option

    Returns:
        float: Option price
    """
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    if option_type == 0:  # Call option
        return S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    elif option_type == 1:  # Put option
        return K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    else:
        raise ValueError(f"Invalid option type: {option_type}")

def sum_squared_diff(sigma, S0, K, T, r, market_prices, option_type):
    """
    Computes the sum of squared differences between Black-Scholes prices and market prices.

    Parameters:
        sigma (float): Implied volatility to be calibrated
        S0 (float): Current stock price
        K (array-like): Strike prices
        T (array-like): Time to maturities
        r (array-like): Risk-free interest rates
        market_prices (array-like): Observed market option prices
        option_type (array-like): Option types (0 for call, 1 for put)

    Returns:
        float: Sum of squared differences
    """
    bs_prices = [black_scholes_price(S0, K[i], T[i], r[i], sigma, option_type[i]) for i in range(len(K))]
    return np.sum((np.array(bs_prices) - market_prices) ** 2)
