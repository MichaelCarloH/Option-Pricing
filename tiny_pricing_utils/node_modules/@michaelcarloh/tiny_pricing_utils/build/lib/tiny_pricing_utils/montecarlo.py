import numpy as np

def simulate_stock_paths(S0, r, q, sigma, T, N, M):
    """
    Simulates stock price paths using the geometric Brownian motion model.

    Parameters:
        S0 (float): Initial stock price
        r (float): Risk-free interest rate
        q (float): Dividend yield
        sigma (float): Volatility
        T (float): Time to maturity
        N (int): Number of time steps
        M (int): Number of Monte Carlo paths

    Returns:
        numpy.ndarray: Simulated stock price paths of shape (M, N+1)
    """
    dt = T / N  # Time step size
    stock_paths = np.zeros((M, N + 1))  # Store stock prices for all paths
    stock_paths[:, 0] = S0  # Set initial stock price

    Z = np.random.randn(M, N)  # Generate standard normal random numbers

    for i in range(1, N + 1):
        stock_paths[:, i] = stock_paths[:, i-1] * np.exp((r - q - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * Z[:, i-1])

    return stock_paths

def price_asian_call(S0, K, r, q, sigma, T, N, M):
    """
    Prices an Asian call option using Monte Carlo simulation.

    Parameters:
        S0, K, r, q, sigma, T (float): Option parameters
        N (int): Number of time steps
        M (int): Number of Monte Carlo simulations

    Returns:
        float: Estimated Asian call option price
    """
    stock_paths = simulate_stock_paths(S0, r, q, sigma, T, N, M)
    average_prices = np.mean(stock_paths[:, 1:], axis=1)  # Average price across time steps
    payoffs = np.maximum(average_prices - K, 0)  # Compute call payoffs
    return np.exp(-r * T) * np.mean(payoffs)  # Discounted expected payoff

def price_up_and_in_put(S0, K, H, r, q, sigma, T, N, M):
    """
    Prices an up-and-in put option using Monte Carlo simulation.

    Parameters:
        S0, K, H, r, q, sigma, T (float): Option parameters
        N (int): Number of time steps
        M (int): Number of Monte Carlo simulations

    Returns:
        float: Estimated up-and-in put option price
    """
    stock_paths = simulate_stock_paths(S0, r, q, sigma, T, N, M)
    barrier_hit = np.any(stock_paths[:, 1:] >= H, axis=1)  # Check if barrier is crossed
    payoffs = np.maximum(K - stock_paths[:, -1], 0) * barrier_hit  # Compute put payoffs
    return np.exp(-r * T) * np.mean(payoffs)

def price_up_and_out_put(S0, K, H, r, q, sigma, T, N, M):
    """
    Prices an up-and-out put option using Monte Carlo simulation.

    Parameters:
        S0, K, H, r, q, sigma, T (float): Option parameters
        N (int): Number of time steps
        M (int): Number of Monte Carlo simulations

    Returns:
        float: Estimated up-and-out put option price
    """
    stock_paths = simulate_stock_paths(S0, r, q, sigma, T, N, M)
    barrier_hit = np.any(stock_paths[:, 1:] >= H, axis=1)  # Check if barrier is crossed
    payoffs = np.maximum(K - stock_paths[:, -1], 0) * (1 - barrier_hit)  # Compute put payoffs
    return np.exp(-r * T) * np.mean(payoffs)