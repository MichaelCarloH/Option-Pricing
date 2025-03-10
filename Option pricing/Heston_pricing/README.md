# Heston Model Call Price Calculation using Carr-Madan Formula  

## Overview  
This script calculates call option prices using the **Heston model** and applies numerical integration techniques—**Rectangular Rule** and **Simpson’s Rule**—within the **Carr-Madan formula** for option pricing. The results are then visualized in a graph comparing the two approximation methods.  

![image](https://github.com/user-attachments/assets/6bc2a600-f915-4623-aa79-5b2ae00faf10)

## Methodology  
### Heston Model  
The Heston model assumes that volatility follows a stochastic process:  
This sentence uses `$` delimiters to show math inline: $\sqrt{3x-1}+(1+x)^2$

$\frac{dS_t}{S_t} = (r − q)dt + \sqrt{v_t} dW_t , \quad S_0 \geq 0$

$dv_t = \kappa(\eta − v_t)dt + \theta \sqrt{v_t} d\tilde{W}_t , \quad v_0 = \sigma^2_0 \geq 0$

where \(W_t\) and \(\tilde{W}_t\) are correlated Brownian motions (correlation \(\rho\)).

Parameters:
- **$\kappa$ (kappa):** Speed of mean reversion ($\kappa > 0$)  
- **$\eta$ (eta):** Long-run variance level ($\eta > 0$)  
- **$\theta$ (theta):** Volatility of volatility ($\theta > 0$)  
- **$v_0$:** Initial variance ($v_0 > 0$)  
- **$\rho$ (rho):** Correlation between volatility and stock price ($-1 < \rho < 1$) 

### Carr-Madan Formula  
The call price is computed using the Fourier transform approach:  

$$ C(K) = e^{- \alpha K} \mathcal{F}^{-1} [\phi(u)] $$  

where $\phi(u)$ is the characteristic function of the log-price under the risk-neutral measure.  

### Numerical Integration  
- **Rectangular Rule:** A simple integration method using uniform partitioning.  
- **Simpson’s Rule:** A higher-order numerical integration method for better accuracy.  

## Theory provided by KUL
