from setuptools import setup, find_packages
import os
import sys
sys.path.insert(0, os.path.abspath('../tiny_pricing_utils'))

setup(
    name="tiny_pricing_utils",
    version="1.0.0",
    packages=find_packages(),
    description="A set of utility functions for my project",
    repository="https://github.com/MichaelCarloH/Option-Pricing",
    long_description_content_type="text/markdown",
    test_suite='tests',
    author="Michael Carlo",
    author_email="michael.carlo@outlook.it",
    license="MIT",
    long_description=open('README.md').read(),
    url="https://github.com/MichaelCarloH/Option-Pricing/tree/main/tiny_pricing_utils",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
     install_requires=[
        'numpy',  
        'scipy',  #
        'matplotlib',  #
    ],
    python_requires='>=3.6',
)
