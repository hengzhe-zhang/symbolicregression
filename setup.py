#!/usr/bin/env python
# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.

from setuptools import setup, find_packages
import os

# Read the README file for long description
readme_path = os.path.join(os.path.dirname(__file__), "README.md")
long_description = ""
if os.path.exists(readme_path):
    with open(readme_path, "r", encoding="utf-8") as fh:
        long_description = fh.read()

setup(
    name="symbolicregression",
    version="0.1.0",
    author="Meta Platforms, Inc. and affiliates",
    description="End-to-end symbolic regression with transformers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/facebookresearch/symbolicregression",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.7",
    install_requires=[
        "numpy>=1.21.0",
        "torch>=1.11.0",
        "sympy>=1.10.0",
        "scikit-learn>=1.0.0",
        "pandas>=1.3.0",
        "matplotlib>=3.5.0",
        "scipy>=1.7.0",
        "tqdm>=4.64.0",
        "pyyaml>=6.0",
        "joblib>=1.1.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.1.0",
            "coverage>=6.3.0",
        ],
        "submitit": [
            "submitit",
        ],
    },
    entry_points={
        "console_scripts": [],
    },
)
