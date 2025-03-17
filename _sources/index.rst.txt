tiny_pricing_utils Documentation
================================

Overview
--------
`tiny_pricing_utils` is a Python package for option pricing and financial modeling. It includes implementations of the Black-Scholes and Heston models, Monte Carlo simulations, and characteristic functions for Fourier-based pricing.\

Working examples can be found at: https://github.com/MichaelCarloH/Option-Pricing/tree/main/Option%20pricing

Key Features:
- **Black-Scholes Model**: European option pricing.
- **Heston Model**: Class-based implementation with FFT pricing methods.
- **Monte Carlo Simulations**: Simulates stock price paths under different models.
- **Characteristic Functions**: Fourier-based characteristic functions for pricing using BS and Heston.

**Aknowledgements**: Part of the Theory and code snippets are based on the course "Financial Engineering" by Peter Leon and Wim Schoutens and course collaborators at KU Leuven.

Installation
------------
To install the required dependencies, use:

.. code-block:: bash

   pip install numpy scipy

Modules
-------
.. toctree::
   :maxdepth: 2
   :caption: Contents:

   HestonModel
   montecarlo_pricing
   stock_paths
   characteristic_function
   black_scholes

API Reference
-------------
.. automodule:: tiny_pricing_utils
   :members:
   :undoc-members:
   :show-inheritance:

.. automodule:: HestonModel
   :members:
   :undoc-members:
   :show-inheritance:

.. automodule:: montecarlo_pricing
   :members:
   :undoc-members:
   :show-inheritance:

.. automodule:: stock_paths
   :members:
   :undoc-members:
   :show-inheritance:

.. automodule:: characteristic_function
   :members:
   :undoc-members:
   :show-inheritance:

.. automodule:: black_scholes
   :members:
   :undoc-members:
   :show-inheritance:
