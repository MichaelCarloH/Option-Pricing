Black-Scholes Model
===================

The Black-Scholes model is a mathematical model used for pricing options, particularly European-style options. It provides a theoretical estimate of the price of options based on certain assumptions and market conditions.

Key Assumptions
----------------
1. The price of the underlying asset follows a geometric Brownian motion.
2. There are no dividends paid during the life of the option.
3. The markets are frictionless (no transaction costs or taxes).
4. There is no arbitrage opportunity.
5. The risk-free interest rate is constant.

Black-Scholes Formula
----------------------
The price of a European call option under the Black-Scholes model is given by the following formula:

.. math::

   C = S_0 N(d_1) - X e^{-rT} N(d_2)

Where:
- :math:`C` = Price of the call option
- :math:`S_0` = Current stock price
- :math:`X` = Strike price of the option
- :math:`r` = Risk-free interest rate
- :math:`T` = Time to maturity
- :math:`N(d_1)` and :math:`N(d_2)` = Cumulative distribution functions of the standard normal distribution
- :math:`d_1` and :math:`d_2` are calculated as:

.. math::

   d_1 = \frac{\ln(S_0 / X) + (r + \frac{\sigma^2}{2}) T}{\sigma \sqrt{T}}
   d_2 = d_1 - \sigma \sqrt{T}

Where:
- :math:`\sigma` = Volatility of the underlying asset

Applications
------------
The Black-Scholes model is widely used in the finance industry for option pricing and risk management. It has been fundamental to the development of modern financial derivatives markets.

However, the model assumes constant volatility and no dividends, which may not hold in real market conditions. In practice, traders often use modifications such as the Black-Scholes-Merton model or volatility surface adjustments to handle these shortcomings.
