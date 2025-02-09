from setuptools import setup, find_packages

setup(
    name="araria-sdk",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests>=2.25.0",
        "pydantic>=2.0.0",
    ],
    author="Araria",
    author_email="contact@araria.com",
    description="Python SDK for Araria API",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/araria/araria-python-sdk",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
) 