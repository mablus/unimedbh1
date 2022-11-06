from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="python-pacotes-processamento-imagens",
    version="0.0.1",
    author="Jefferson",
    author_email="jeffersonknopf97@gmail.com",
    description="Test version - Image processing. This project belongs to Karina Tiemi Kato, Tech Lead, Machine Learning Engineer, Data Scientist Specialist at Take. This package is a demo for simulation of upload on the Test Pypi website, and it's from class of the Bootcamp Cognizant Cloud Data Engineer #2. E-mail:karinatkato@gmail.com.",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jeffersonk97/python-pacotes-processamento-imagens",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)