from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    install_requires=[
        "boto3==1.10.32",
        "botocore==1.13.32",
        "docutils==0.15.2",
        "jmespath==0.9.4",
        "python-dateutil==2.8.0; python_version >= '2.7'",
        "s3transfer==0.2.1",
        "six==1.13.0",
        "urllib3==1.25.7; python_version >= '3.4'",
    ],
    name="aws-utils",  # Replace with your own username
    version="0.1.0",
    author="Gabriel Chamon Araujo",
    author_email="gabrielchamon@lett.digital",
    description="Contain aws utilities to be shared between projects",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gchamon/aws-utils",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
