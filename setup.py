from distutils.core import setup
from setuptools import find_packages

setup(
    name="math_quiz",
    version="1.0",
    author="Marlon Gravemeyer",
    author_email="marlon-gravemeyer@web.de",
    packages=find_packages(),
    install_requires=["random"],
    extras_require={
        "dev": ["unittest"]     # Additional packages for development
    }
)
