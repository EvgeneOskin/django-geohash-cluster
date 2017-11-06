=============================
django geohash cluster
=============================

.. image:: https://badge.fury.io/py/django-geohash-cluster.svg
    :target: https://badge.fury.io/py/django-geohash-cluster

.. image:: https://travis-ci.org/EvgeneOskin/django-geohash-cluster.svg?branch=master
    :target: https://travis-ci.org/EvgeneOskin/django-geohash-cluster

.. image:: https://codecov.io/gh/EvgeneOskin/django-geohash-cluster/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/EvgeneOskin/django-geohash-cluster

High efficient clustering algorithm based on geohash of points

Documentation
-------------

The full documentation is at https://django-geohash-cluster.readthedocs.io.

Quickstart
----------

Install django geohash cluster::

    pip install django-geohash-cluster

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'geohash_cluster',
        ...
    )

To use with :django rest framework:https://django-geohash-cluster.readthedocs.io

.. code-block:: bash

    $ pip install geohash_cluster[rest]

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'rest_framework',
        'rest_framework_gis',
        ...
        'geohash_cluster',
        ...
    )


Features
--------

* A `Pointed` model with `PointField`.

Running Tests
-------------

Install dependencies:


.. code-block:: bash

   $ pipenv install --dev
   $ pip install .[rest]


Does the code actually work?

.. code-block:: bash

    $ source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
