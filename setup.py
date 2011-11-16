#!/usr/bin/env python

from setuptools import setup


setup(
    name="djtokeninput",
    version="0.1",
    license="MIT",

    install_requires = [
        "django"
    ],

    package_dir={"": "lib"},
    packages=["djtokeninput"],
    include_package_data=True,

    author="Adam Mckaig",
    author_email="adam.mckaig@gmail.com",

    description="jQuery Tokeninput for Django forms",
    url="http://github.com/adammck/djtokeninput"
)
