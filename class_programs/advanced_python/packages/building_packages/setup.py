from setuptools import setup, find_packages

setup(
    name="my_package",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'requests',  # An example dependency
    ],
    # Additional metadata like author, description, etc.
)
