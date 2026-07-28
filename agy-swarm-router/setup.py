from setuptools import setup, find_packages

setup(
    name="agy-swarm-router",
    version="1.0.0",
    description="Dynamic heterogeneous model routing for AGY swarms.",
    author="OpenAgentic Consortium",
    packages=find_packages(),
    install_requires=[],
    extras_require={
        "dev": ["pytest", "black", "flake8"]
    }
)
