# Copyright 2018 SAP SE.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http: //www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied. See the License for the specific
# language governing permissions and limitations under the License.

from os.path import dirname, join
import os
import re
from setuptools import setup, find_packages
import subprocess

source_location = os.path.abspath(os.path.dirname(__file__))


NAME = 'python-pyodata'
HERE = os.path.abspath(os.path.dirname(__file__))
def _read(name):
    with open(os.path.join(HERE, name), 'r', encoding='utf-8') as f:
        return f.read()

setup(
    name="pyodata",
    version=_read('VERSION').strip(),
    license="Apache License Version 2.0",
    url="https://github.com/SAP/python-pyodata",
    author="Jakub Filak, Michal Nezerka, Patrik Petrik, Lubos Mjachky",
    author_email="jakub.filak@sap.com, michal.nezerka@sap.com, patrik.petrik@sap.com, lubos.mjachky@sap.com",
    description="Enterprise ready Python OData client",
    long_description=_read('README.md'),
    long_description_content_type="text/markdown",
    packages=find_packages(exclude=("tests")),
    zip_safe=False,
    install_requires=[
        "enum34>=1.0.4",
        "lxml>=3.7.3",
    ],
    extras_require={
    },
    tests_require=[
        "setuptools>=38.2.4",
        "setuptools-scm>=1.15.6",
        "funcsigs>=1.0.2",
        "requests==2.20.0",
        "responses>=0.8.1",
        "pytest>=2.7.0",
    ],
    classifiers=[ # cf. http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    entry_points = {
    },
)
