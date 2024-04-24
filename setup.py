"""Codeseus setup file."""

from __future__ import annotations

from setuptools import find_packages, setup  # type: ignore


VERSION = "0.0.1"

setup(
    name="codeseus",
    version=VERSION,
    packages=find_packages(include=["codeseus", "codeseus.*"]),
    install_requires=["prompt_toolkit", "jaclang"],
    package_data={
        "": ["*.ini"],
    },
    entry_points={
        "console_scripts": [
            "codeseus = codeseus.cli:main",
        ],
    },
    author="Chandra & Kugeshan",
    author_email="irugalbandara@ascii.ai",
    url="https://github.com/chandralegend/codeseus",
)
