import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="stockx-api-client",
    version="0.0.1",
    author="Steven Athouel",
    author_email="sathouel@gmail.com",
    description="A simple api client for stockx plateform",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sathouel/stockx-api-client.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)