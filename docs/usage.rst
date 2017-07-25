=====
Usage
=====

To use django geohash cluster in a project, add it to your `INSTALLED_APPS`:

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
