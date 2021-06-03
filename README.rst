Interactive py2neo console (ipy2neo)
====================================
.. image:: https://img.shields.io/github/v/release/technige/ipy2neo?sort=semver
   :target: https://github.com/technige/ipy2neo
   :alt: GitHub release

.. image:: https://img.shields.io/github/license/technige/ipy2neo.svg
   :target: https://www.apache.org/licenses/LICENSE-2.0
   :alt: License

.. image:: https://img.shields.io/github/workflow/status/technige/ipy2neo/Run%20tests%20(Ubuntu%2018.04)
   :target: https://github.com/technige/ipy2neo/actions?query=workflow%3A"Run%20tests%20(Ubuntu%2018.04)"
   :alt: GitHub Workflow Status

.. image:: https://coveralls.io/repos/github/technige/ipy2neo/badge.svg?branch=master
   :target: https://coveralls.io/github/technige/ipy2neo?branch=master
   :alt: Coverage Status


**IPy2neo** is a an interactive command line console for working with `Neo4j <https://neo4j.com/>`_ built on top of the `py2neo <https://py2neo.org>`_ library.


Quick Example
-------------

To run a query against a local database is straightforward::

    >>> from py2neo import Graph
    >>> graph = Graph("bolt://localhost:7687", auth=("neo4j", "password"))
    >>> graph.run("UNWIND range(1, 3) AS n RETURN n, n * n as n_sq")
       n | n_sq
    -----|------
       1 |    1
       2 |    4
       3 |    9


Releases & Versioning
---------------------

IPy2neo releases adhere to `Calendar Versioning <https://calver.org/>`_, using a scheme of ``YYYY.N.M``.
Here, ``N`` is an incrementing zero-based number for each year, and ``M`` is a revision within that version (also zero-based).

No compatibility guarantees are given between versions, but as a general rule, a change in ``M`` should require little-to-no work within client applications,
whereas a change in ``N`` may require some work. A change to the year is likely to require a more significant amount of work to upgrade.


Installation
------------
.. image:: https://img.shields.io/pypi/v/ipy2neo.svg
   :target: https://pypi.python.org/pypi/ipy2neo
   :alt: PyPI version

.. image:: https://img.shields.io/pypi/dm/ipy2neo
   :target: https://pypi.python.org/pypi/ipy2neo
   :alt: PyPI Downloads

To install the latest release of ipy2neo, simply use:

.. code-block::

    $ pip install --upgrade ipy2neo

To install the latest stable code from the GitHub master branch, use:

.. code-block::

    $ pip install git+https://github.com/technige/ipy2neo.git@master#egg=ipy2neo


Requirements
------------
.. image:: https://img.shields.io/pypi/pyversions/ipy2neo.svg
   :target: https://www.python.org/
   :alt: Python versions

.. image:: https://img.shields.io/badge/neo4j-3.4%20%7C%203.5%20%7C%204.0%20%7C%204.1%20%7C%204.2%20%7C%204.3-blue.svg
   :target: https://neo4j.com/
   :alt: Neo4j versions

The following versions of Python and Neo4j (all editions) are supported:

- Python 2.7 / 3.4 / 3.5 / 3.6 / 3.7 / 3.8 / 3.9
- Neo4j 3.4 / 3.5 / 4.0 / 4.1 / 4.2 / 4.3 (the latest point release of each version is recommended)

Note also that IPy2neo is developed and tested under **Linux** using standard CPython distributions.
While other operating systems and Python distributions may work, support for these is not available.


More
----

For more information, read the `handbook <https://py2neo.org/i>`_.
