from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    install_requires=[],
    name="aws-utils",
    version="1.0.1",
    author="Gabriel Chamon Araujo",
    author_email="gabrielchamon@lett.digital",
    description="Contains aws utilities to be shared between projects",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gchamon/aws-utils",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
