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


from os import getenv


def _parse_letter_version(letter, number):

    if letter:
        # We consider there to be an implicit 0 in a pre-release if there is
        # not a numeral associated with it.
        if number is None:
            number = 0

        # We normalize any letters to their lower case form
        letter = letter.lower()

        # We consider some words to be alternate spellings of other words and
        # in those cases we want to normalize the spellings to our preferred
        # spelling.
        if letter == "alpha":
            letter = "a"
        elif letter == "beta":
            letter = "b"
        elif letter in ["c", "pre", "preview"]:
            letter = "rc"
        elif letter in ["rev", "r"]:
            letter = "post"

        return letter, int(number)
    if not letter and number:
        # We assume if we are given a number, but we are not given a letter
        # then this is using the implicit post release syntax (e.g. 1.0-1)
        letter = "post"

        return letter, int(number)

    return None


def parse_version_string(version_string):
    import re

    version_pattern_str = r"""
        v?
        (?:
            (?:(?P<epoch>[0-9]+)!)?                           # epoch
            (?P<release>[0-9]+(?:\.[0-9]+)*)                  # release segment
            (?P<pre>                                          # pre-release
                [-_\.]?
                (?P<pre_l>(a|b|c|rc|alpha|beta|pre|preview))
                [-_\.]?
                (?P<pre_n>[0-9]+)?
            )?
            (?P<post>                                         # post release
                (?:-(?P<post_n1>[0-9]+))
                |
                (?:
                    [-_\.]?
                    (?P<post_l>post|rev|r)
                    [-_\.]?
                    (?P<post_n2>[0-9]+)?
                )
            )?
            (?P<dev>                                          # dev release
                [-_\.]?
                (?P<dev_l>dev)
                [-_\.]?
                (?P<dev_n>[0-9]+)?
            )?
        )
    """

    version_pattern = re.compile(
        r"^\s*" + version_pattern_str + r"\s*$",
        re.VERBOSE | re.IGNORECASE,
    )

    match = version_pattern.search(version_string)
    if not match:
        raise ValueError("Invalid version: {}".format(version_string))

    return {
        "string": version_string,
        "epoch": int(match.group("epoch")) if match.group("epoch") else 0,
        "release": tuple(int(i) for i in match.group("release").split(".")),
        "pre": _parse_letter_version(match.group("pre_l"), match.group("pre_n")),
        "post": _parse_letter_version(
            match.group("post_l"), match.group("post_n1") or match.group("post_n2")
        ),
        "dev": _parse_letter_version(match.group("dev_l"), match.group("dev_n")),
    }


def get_metadata():
    return {
        "name": "ipy2neo",
        "version": "2021.0.0",
        "description": "Interactive Neo4j console built on py2neo",
        "author": "Nigel Small",
        "author_email": "technige@py2neo.org",
        "url": "https://py2neo.org/ipy2neo",
        "project_urls": {
            "Bug Tracker": "https://github.com/py2neo-org/ipy2neo/issues",
            "Documentation": "https://py2neo.org/ipy2neo/",
            "Source Code": "https://github.com/py2neo-org/ipy2neo",
        },
        "license": "Apache License, Version 2.0",
        "keywords": [],
        "platforms": [],
        "classifiers": [
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
            "Topic :: Software Development :: Libraries",
        ],
    }
