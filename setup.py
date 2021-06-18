#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# Copyright 2011-2021, Nigel Small
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from os import path

from setuptools import setup, find_packages

from ipy2neo import __version__


README_FILE = path.join(path.dirname(__file__), "README.rst")


def get_readme():
    with open(README_FILE) as f:
        return f.read()


setup(
    name="ipy2neo",
    version=__version__,
    description="Interactive Neo4j console built on py2neo",
    author="Nigel Small",
    author_email="technige@py2neo.org",
    url="https://py2neo.org/ipy2neo",
    project_urls={
        "Bug Tracker": "https://github.com/py2neo-org/ipy2neo/issues",
        "Documentation": "https://py2neo.org/ipy2neo/",
        "Source Code": "https://github.com/py2neo-org/ipy2neo",
    },
    license="Apache License, Version 2.0",
    keywords=[],
    platforms=[],
    classifiers=[
        "Development Status :: 6 - Mature",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Database",
        "Topic :: Database :: Database Engines/Servers",
        "Topic :: Scientific/Engineering",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries"],
    long_description=get_readme(),
    long_description_content_type="text/x-rst",
    entry_points={
        "console_scripts": [
            "ipy2neo = ipy2neo.__main__:main",
        ],
    },
    packages=find_packages(exclude=("docs", "test", "test.*")),
    py_modules=[],
    install_requires=[
        "pansi>=2020.7.3",
        "prompt_toolkit~=2.0.7; python_version < '3.6'",
        "prompt_toolkit>=2.0.7; python_version >= '3.6'",
        "py2neo",
        "pygments>=2.0.0",
    ]
)
