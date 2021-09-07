from setuptools import setup

setup(
    name='Astro',
    version='0.1',
    description='Multipuprose discord bot',
    packages=['Astro'],
    install_requires=['coloredlogs'],
    extras_require={  # Optional
        'dev': ['discord.py']
    },
)
