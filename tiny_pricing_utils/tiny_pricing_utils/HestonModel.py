import numpy as np
from scipy.interpolate import interp1d
from tiny_pricing_utils.characteristic_function import cf_Heston

class HestonModel:
    def __init__(self, 
                 S0, 
                 r, 
                 q, 
                 V0=0.05, 
                 kappa=0.5, 
                 eta=0.05, 
                 theta=0.2, 
                 rho=-0.75, 
                 T=1, 
                 alpha=1.5, 
                 N=4096, 
                 eta_cm=0.25, 
                 b=None, 
                 strikes=None):
        """
        Initialize the Heston model with given or default parameters.

        Parameters:
            S0 (float): Initial stock price.
            r (float): Risk-free rate.
            q (float): Dividend yield.
            V0 (float): Initial variance (default = 0.05).
            kappa (float): Rate of mean reversion (default = 0.5).
            eta (float): Long-term mean of volatility (default = 0.05).
            theta (float): Volatility of volatility (default = 0.2).
            rho (float): Correlation between stock price and volatility (default = -0.75).
            T (float): Time to maturity (default = 1).
            alpha (float): Fourier transform parameter (default = 1.5).
            N (int): Number of grid points (default = 4096).
            eta_cm (float): Fourier grid spacing (default = 0.25).
            b (float): Upper limit for Fourier transform integration (default calculated if None).
            strikes (array-like): Specific strike prices for interpolation (default = None).
        """
        # Store model parameters
        self.S0 = S0
        self.r = r
        self.q = q
        self.V0 = V0
        self.kappa = kappa
        self.eta = eta
        self.theta = theta
        self.rho = rho
        self.T = T
        self.alpha = alpha
        self.N = N
        self.eta_cm = eta_cm
        self.strikes = strikes
        
        # Calculate lambda_ and b if not provided
        self.lambda_ = (2 * np.pi) / (N * eta_cm)
        self.b = b if b is not None else (N * self.lambda_) / 2
        
        # Calculate auxiliary variables (log strikes, v, u, rho_cm)
        self.calculate_auxiliary_variables()

    def calculate_auxiliary_variables(self):
        """Calculate log_strikes, v, u, and rho_cm based on model parameters."""
        # Define finer grid for log strikes
        self.log_strikes = np.arange(-self.b, self.b, self.lambda_)
        
        # Grid for the Fourier transform variable v
        self.v = np.arange(0, self.N * self.eta_cm, self.eta_cm)
        
        # Define u for Fourier transform
        self.u = self.v - (self.alpha + 1) * 1j
        
        # Define rho_cm using the characteristic function
        self.rho_cm = np.exp(-self.r * self.T) * cf_Heston(self.u, self.S0, self.r, self.q, 
                                                             self.V0, self.kappa, self.eta, 
                                                             self.theta, self.rho, self.T) / \
                      (self.alpha**2 + self.alpha - self.v**2 + 1j * (2 * self.alpha + 1) * self.v)

    def compute_fft(self, rule="rectangular", simpson_weights=None):
        """Compute the FFT based on the specified integration rule."""
        if rule == "rectangular":
            return self.compute_fft_rectangular()
        elif rule == "simpson":
            return self.compute_fft_simpson(simpson_weights)
        else:
            raise ValueError(f"Unsupported rule: {rule}")

    def compute_fft_rectangular(self):
        """Computes option prices using FFT with the rectangular rule."""
        fft_result_rectangular = np.fft.fft(np.exp(1j * self.v * self.b) * self.rho_cm * self.eta_cm)
        
        # Extract real part
        a_rectangular = np.real(fft_result_rectangular)
        
        # Compute call option prices
        self.calls_rectangular = (1 / np.pi) * np.exp(-self.alpha * self.log_strikes) * a_rectangular

    def compute_fft_simpson(self, simpson_weights):
        """Computes option prices using FFT with Simpson's rule."""
        # Apply Simpson's Rule correction in the FFT computation
        simpson_int = simpson_weights
        
        # Perform FFT with the Simpson's Rule weights
        fft_result_simpson = np.fft.fft(np.exp(1j * self.v * self.b) * self.rho_cm * self.eta_cm * simpson_int)
        
        # Extract real part
        a_simpson = np.real(fft_result_simpson)
        
        # Compute call option prices
        self.calls_simpson = (1 / np.pi) * np.exp(-self.alpha * self.log_strikes) * a_simpson

    def interpolate_prices(self):
        """Interpolate option prices for specific strikes."""
        # Choose interpolation method based on available data
        if hasattr(self, 'calls_rectangular'):
            calls_to_use = self.calls_rectangular
        elif hasattr(self, 'calls_simpson'):
            calls_to_use = self.calls_simpson
        else:
            raise ValueError("No option prices computed. Run compute_fft first.")
        
        # Interpolation for the specific strikes
        spline = interp1d(np.exp(self.log_strikes), calls_to_use, kind='cubic', fill_value="extrapolate")
        return spline(self.strikes)

    def price_options(self, rule="rectangular", simpson_weights=None):
        """Price options based on selected integration rule."""
        self.compute_fft(rule, simpson_weights)
        return self.interpolate_prices()
    # Getter and Setter Functions
    def get_S0(self):
        return self.S0

    def set_S0(self, value):
        self.S0 = value
    
    def get_r(self):
        return self.r

    def set_r(self, value):
        self.r = value
    
    def get_q(self):
        return self.q

    def set_q(self, value):
        self.q = value
    
    def get_V0(self):
        return self.V0

    def set_V0(self, value):
        self.V0 = value
    
    def get_kappa(self):
        return self.kappa

    def set_kappa(self, value):
        self.kappa = value
    
    def get_eta(self):
        return self.eta

    def set_eta(self, value):
        self.eta = value
    
    def get_theta(self):
        return self.theta

    def set_theta(self, value):
        self.theta = value
    
    def get_rho(self):
        return self.rho

    def set_rho(self, value):
        self.rho = value
    
    def get_T(self):
        return self.T

    def set_T(self, value):
        self.T = value
    
    def get_alpha(self):
        return self.alpha

    def set_alpha(self, value):
        self.alpha = value
    
    def get_N(self):
        return self.N

    def set_N(self, value):
        self.N = value
    
    def get_b(self):
        return self.b

    def set_b(self, value):
        self.b = value
    
    def get_eta_cm(self):
        return self.eta_cm

    def set_eta_cm(self, value):
        self.eta_cm = value
    
    def get_specific_strikes(self):
        return self.specific_strikes

    def set_specific_strikes(self, value):
        self.specific_strikes = value