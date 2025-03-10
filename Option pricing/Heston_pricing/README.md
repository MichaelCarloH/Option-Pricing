# Heston Model Call Price Calculation using Carr-Madan Formula  

## Overview  
This script calculates call option prices using the **Heston model** and applies numerical integration techniques—**Rectangular Rule** and **Simpson’s Rule**—within the **Carr-Madan formula** for option pricing. The results are then visualized in a graph comparing the two approximation methods.  

## Methodology  
### Heston Model  
The Heston model assumes that volatility follows a stochastic process:  

$$ dV_t = \kappa (\theta - V_t) dt + \eta \sqrt{V_t} dW_t^2 $$  

where:  
- \( V_t \) is the variance process  
- \( \kappa \) is the rate of mean reversion  
- \( \theta \) is the long-term variance  
- \( \eta \) is the volatility of variance  
- \( W_t^2 \) is a Wiener process  

### Carr-Madan Formula  
The call price is computed using the Fourier transform approach:  

$$ C(K) = e^{- \alpha K} \mathcal{F}^{-1} [\phi(u)] $$  

where \( \phi(u) \) is the characteristic function of the log-price under the risk-neutral measure.  

### Numerical Integration  
- **Rectangular Rule:** A simple integration method using uniform partitioning.  
- **Simpson’s Rule:** A higher-order numerical integration method for better accuracy.  

## How to Use  
- Run the script in a Python environment with `numpy` and `matplotlib` installed.  
- The output graph compares call option prices for different strike prices:  

$$ K = [90, 95, 100, 105, 110] $$  

using both numerical methods.  

## Dependencies  
- `numpy`  
- `matplotlib`  

## Example Output  
The graph generated shows the call option prices obtained using both approximation methods, helping to visualize their differences.  
