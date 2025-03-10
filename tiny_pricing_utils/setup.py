from setuptools import setup, find_packages
from setuptools.command.install import install
import os
import subprocess

class CustomInstallCommand(install):
    """Custom command to run Sphinx after installation."""
    def run(self):
        install.run(self)  # Run the standard install
        # Now, generate the documentation using Sphinx
        subprocess.check_call(['sphinx-build', '-b', 'html', 'docs/source', 'docs/_build/html'])

setup(
    name="tiny_pricing_utils",  # Package name
    version="0.4",  # Version of the package
    packages=find_packages(),  # This automatically finds your package
    description="A set of utility functions for my project",
    repository="https://github.com/MichaelCarloH/Option-Pricing",
    long_description=open('README.md').read(),  # Read your README file
    long_description_content_type="text/markdown",  # The format of your README
    author="Your Name",
    author_email="michael.carlo@outlook.it",
    license="MIT",  # License type
    classifiers=[  # Useful for PyPI classification
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[  # Add sphinx to dependencies
        'sphinx',  # Add Sphinx to your dependencies for building docs
    ],
    cmdclass={
        'install': CustomInstallCommand,  # Use custom install to run sphinx-build
    },
)
