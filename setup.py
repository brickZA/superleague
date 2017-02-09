#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name="superleague",
    description="SuperLeague Pro Football League Manager",
    author="Neilen Marais",
    author_email="nmarais@gmail.com",
    packages=find_packages(),
    scripts=[
        "scripts/superleague.py",
    ],
    license="BSD",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: End Users/Desktop",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2",
    ],
    platforms=["OS Independent"],
    keywords="soccer football league",
    # run tests and install these requirements with python setup.py nosetests
    tests_require=["mock"],
    zip_safe=False,
    test_suite="superleague.tests",
)
