from setuptools import setup, find_packages

setup(
    name="agy-perf-toolkit",
    version="1.0.0",
    description="Native AGY KV cache optimization and dynamic context-pruning.",
    author="OpenAgentic Consortium",
    packages=find_packages(),
    install_requires=[
        "numpy>=1.24.0",
    ],
    extras_require={
        "dev": ["pytest", "black", "flake8"]
    }
)
