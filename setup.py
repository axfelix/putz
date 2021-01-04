#!/usr/bin/env python

from setuptools import setup
import sys

with open("readme.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

install_requires = ["setuptools", "docopt", "pypi_search"]

if sys.version_info < (3, 5):
    sys.exit("This module requires Python 3.5+")

setup(
    name="putz",
    python_requires=">3.5.0",
    version="1.0.1",
    description="A module for putzing around with Python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    author="Alex Garnett",
    author_email="axfelix@gmail.com",
    url="https://github.com/axfelix/putz",
    packages=[
        "putz",
        "putz.cli",
    ],
    install_requires=install_requires,
    zip_safe=False,
    entry_points="""
        [console_scripts]
        putz=putz.cli.main:main
        """,
)
