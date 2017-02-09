#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name="superleague",
    description="SuperLeague Pro Football League Manager",
    author="Neilen Marais",
    author_email="nmarais@gmail.com",
    packages=find_packages(),
    license="BSD",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: End Users/Desktop",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2",
    ],
    entry_points={'console_scripts': [
        'superleague = superleague.main:main']},
    platforms=["OS Independent"],
    keywords="soccer football league",
    zip_safe=False,
    test_suite="superleague.tests",
)
