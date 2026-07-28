from setuptools import setup, find_packages

setup(
    name="agy-secure-sandbox",
    version="1.0.0",
    description="Containerized isolated environments for MCP servers with eBPF kernel monitoring.",
    author="OpenAgentic Consortium",
    packages=find_packages(),
    install_requires=[],
    extras_require={
        "dev": ["pytest", "black", "flake8"]
    }
)
