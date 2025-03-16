import numpy as np
from .stock_paths import *

def price_european_call(S0, K, r, q, sigma, T, N, M):
    stock_paths = geometric_brownian_motion(S0, r, q, sigma, T, N, M)
    payoffs = np.maximum(stock_paths[:, -1] - K, 0)
    return np.exp(-r * T) * np.mean(payoffs)

def price_european_put(S0, K, r, q, sigma, T, N, M):
    stock_paths = geometric_brownian_motion(S0, r, q, sigma, T, N, M)
    payoffs = np.maximum(K - stock_paths[:, -1], 0)
    return np.exp(-r * T) * np.mean(payoffs)

def price_heston_euler_call(S0, K, r, q, v0, kappa, eta, theta, rho, T, N, M):
    stock_paths = heston_euler(S0, r, q, v0, kappa, eta, theta, rho, T, N, M)
    payoffs = np.maximum(stock_paths[:, -1] - K, 0)
    return np.exp(-r * T) * np.mean(payoffs)

def price_heston_euler_put(S0, K, r, q, v0, kappa, eta, theta, rho, T, N, M):
    stock_paths = heston_euler(S0, r, q, v0, kappa, eta, theta, rho, T, N, M)
    payoffs = np.maximum(K - stock_paths[:, -1], 0)
    return np.exp(-r * T) * np.mean(payoffs)

def price_heston_milstein_call(S0, K, r, q, v0, kappa, eta, theta, rho, T, N, M):
    stock_paths = heston_milstein(S0, r, q, v0, kappa, eta, theta, rho, T, N, M)
    payoffs = np.maximum(stock_paths[:, -1] - K, 0)
    return np.exp(-r * T) * np.mean(payoffs)

def price_heston_milstein_put(S0, K, r, q, v0, kappa, eta, theta, rho, T, N, M):
    stock_paths = heston_milstein(S0, r, q, v0, kappa, eta, theta, rho, T, N, M)
    payoffs = np.maximum(K - stock_paths[:, -1], 0)
    return np.exp(-r * T) * np.mean(payoffs)

def price_asian_call(S0, K, r, q, sigma, T, N, M):
    stock_paths = geometric_brownian_motion(S0, r, q, sigma, T, N, M)
    avg_price = np.mean(stock_paths[:, 1:], axis=1)
    payoffs = np.maximum(avg_price - K, 0)
    return np.exp(-r * T) * np.mean(payoffs)

def price_up_and_in_put(S0, K, H, r, q, sigma, T, N, M):
    stock_paths = geometric_brownian_motion(S0, r, q, sigma, T, N, M)
    barrier_hit = np.any(stock_paths[:, 1:] >= H, axis=1)
    payoffs = np.maximum(K - stock_paths[:, -1], 0) * barrier_hit
    return np.exp(-r * T) * np.mean(payoffs)

def price_up_and_out_put(S0, K, H, r, q, sigma, T, N, M):
    stock_paths = geometric_brownian_motion(S0, r, q, sigma, T, N, M)
    barrier_hit = np.any(stock_paths[:, 1:] >= H, axis=1)
    payoffs = np.maximum(K - stock_paths[:, -1], 0) * (1 - barrier_hit)
    return np.exp(-r * T) * np.mean(payoffs)
