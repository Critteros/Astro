"""
Setup script for setuptools and pip-tools
"""
from setuptools import setup

setup(
    # Application name
    name='Astro',
    # Application version
    version='0.1',
    # Application description
    description='Multipuprose discord bot',
    # Application core
    packages=['astro'],
    # Requirements
    install_requires=['coloredlogs'],
    extras_require={
        'dev': ['discord.py']
    },
)
