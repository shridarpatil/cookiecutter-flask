#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Setup.py"""
from setuptools import setup

requirements = ['pymysql', 'flask']

tests_requirements = [
    'pytest',
    'pytest-cov',
    'pytest-profiling',
]


setup(
    name={{cookiecutter.package}},
    version='0.1',
    description="",
    author="Shridhar, Sumeet",
    author_email='shridharpatil2792@gmai.com',
    url='https://bitbucket.org/_shridharpatil/{{cookiecutter.package}}',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Office/Business',
    ],
    license='BSD',
    install_requires=requirements,
    test_suite='tests',
    tests_require=tests_requirements,
)
