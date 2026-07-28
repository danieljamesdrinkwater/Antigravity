from setuptools import setup, find_packages

setup(
    name="agy-chroma-memory",
    version="1.0.0",
    description="Persistent architectural knowledge graphs using ChromaDB.",
    author="OpenAgentic Consortium",
    packages=find_packages(),
    install_requires=[
        # Mock dependency
        "chromadb>=0.4.0",
    ],
    extras_require={
        "dev": ["pytest", "black", "flake8"]
    }
)
