import os
from setuptools import setup


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="fpdf-parser",
    version="0.0.1",
    author="Fred Vollmer",
    author_email="fredric.vollmer@gmail.com",
    description="A simp[le utility to parse Freematics Parsed Data Format files",
    license="BSD",
    keywords="parser fpdf freematics",
    url="http://packages.python.org/an_example_pypi_project",
    packages=['fpdfparser', 'tests'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
    install_requires=[
        'geopy',
    ]
)
