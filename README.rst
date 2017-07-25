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
        'geohash_cluster.apps.GeohashClusterConfig',
        ...
    )

Add django geohash cluster's URL patterns:

.. code-block:: python

    from geohash_cluster import urls as geohash_cluster_urls


    urlpatterns = [
        ...
        url(r'^', include(geohash_cluster_urls)),
        ...
    ]

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
