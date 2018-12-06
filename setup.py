import os
from setuptools import setup, find_packages

# Utility function to read the README file.
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name = "monerolib",
    version = "0.0.1",
    description = "An all-in-one python toolbox for Monero cryptocurrency.",
    long_description=read('README.md'),
    url = "https://github.com/cryptochangements34/monerolib-python",
    keywords = "monero",
    packages=find_packages(),
    install_requires=requirements,
    license = "MIT"
)
