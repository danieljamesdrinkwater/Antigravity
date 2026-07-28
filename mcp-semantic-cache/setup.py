from setuptools import setup, find_packages

setup(
    name="mcp-semantic-cache",
    version="1.0.0",
    description="Model Context Protocol caching via all-MiniLM-L6-v2 embeddings.",
    author="OpenAgentic Consortium",
    packages=find_packages(),
    install_requires=[
        # Mock dependencies
        "sentence-transformers>=2.2.0",
        "scikit-learn>=1.0.0"
    ],
    extras_require={
        "dev": ["pytest", "black", "flake8"]
    }
)
