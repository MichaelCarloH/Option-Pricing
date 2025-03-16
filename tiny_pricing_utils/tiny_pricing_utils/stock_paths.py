import numpy as np

def geometric_brownian_motion(S0, r, q, sigma, T, N, M):
    dt = T / N
    stock_paths = np.zeros((M, N + 1))
    stock_paths[:, 0] = S0
    Z = np.random.randn(M, N)
    for i in range(1, N + 1):
        stock_paths[:, i] = stock_paths[:, i-1] * np.exp((r - q - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * Z[:, i-1])
    return stock_paths

def heston_euler(S0, r, q, v0, kappa, eta, theta, rho, T, N, M):
    dt = T / N
    stock_paths = np.zeros((M, N + 1))
    v = np.zeros((M, N + 1))
    stock_paths[:, 0] = S0
    v[:, 0] = v0
    epsilon1 = np.random.randn(M, N)
    epsilon2 = rho * epsilon1 + np.sqrt(1 - rho ** 2) * np.random.randn(M, N)
    for i in range(1, N + 1):
        v[:, i] = np.maximum(0, v[:, i-1] + kappa * (eta - v[:, i-1]) * dt + theta * np.sqrt(np.maximum(0, v[:, i-1]) * dt) * epsilon2[:, i-1])
        stock_paths[:, i] = stock_paths[:, i-1] * np.exp((r - q - 0.5 * v[:, i-1]) * dt + np.sqrt(v[:, i-1] * dt) * epsilon1[:, i-1])
    return stock_paths

def heston_milstein(S0, r, q, v0, kappa, eta, theta, rho, T, N, M):
    dt = T / N
    stock_paths = np.zeros((M, N + 1))
    v = np.zeros((M, N + 1))
    stock_paths[:, 0] = S0
    v[:, 0] = v0
    epsilon1 = np.random.randn(M, N)
    epsilon2 = rho * epsilon1 + np.sqrt(1 - rho ** 2) * np.random.randn(M, N)
    for i in range(1, N + 1):
        v_t = np.maximum(0, v[:, i-1])
        v[:, i] = v[:, i-1] + kappa * (eta - v[:, i-1]) * dt + theta * np.sqrt(v_t * dt) * epsilon2[:, i-1] + 0.25 * theta**2 * dt * (epsilon2[:, i-1]**2 - 1)
        v[:, i] = np.maximum(0, v[:, i])  # Ensure variance is non-negative
        stock_paths[:, i] = stock_paths[:, i-1] * np.exp((r - q - 0.5 * v[:, i-1]) * dt + np.sqrt(v[:, i-1] * dt) * epsilon1[:, i-1])
    return stock_paths
