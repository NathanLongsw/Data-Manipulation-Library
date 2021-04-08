import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="OSC-SelectR",
    version="0.1.5",
    author="Bruce Meng, Nathan Longsworth",
    author_email="bmeng@osc.gov.on.ca, nlongsworth@osc.gov.on.ca",
    description="Python package to read and parse SelectR data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    #url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)