=====
Usage
=====

To use django geohash cluster in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'geohash_cluster',
        ...
    )

Add `Pointed` model and `ClusteraleQuerySet` to your `models.py`:

.. code-block:: python

    from geohash_cluster.models import Pointed, ClusterableQuerySet


    class Place(Pointed):

        objects = ClusterableQuerySet.as_manager()

        class Meta:
            app_label = 'example'


---
DRF
---

Geohash Cluster provides a shortcuts for
:Django Rest Framework:`http://www.django-rest-framework.org/`.

Sample:

.. code-block:: python

    # views.py
    from rest_framework.viewsets import ReadOnlyModelViewSet

    from rest_framework_gis.filters import InBBoxFilter
    from geohash_cluster.rest_framework import ClusterSerializer, ClusterFilter

    from .models import Place


    class PlaceClusterSerializer(ClusterSerializer):

        class Meta:
            model = Place
            id_field = False
            geo_field = "point"
            fields = ['point', 'point_geohash', 'cluster_count']


    class Cluster(ReadOnlyModelViewSet):
        queryset = Place.objects
        bbox_filter_field = 'point'
        filter_backends = (InBBoxFilter, ClusterFilter)
        serializer_class = PlaceClusterSerializer

.. code-block:: python

    # urls.py

    from django.conf.urls import url, include
    from rest_framework.routers import DefaultRouter

    from .views import Cluster


    router = DefaultRouter()
    router.register('cluster', Cluster)

    urlpatterns = [
        url(r'^', include(router.urls)),
    ]


Usage

.. code-block:: bash

    $ curl 'http://localhost:8000/cluster/?zoom=0&in_bbox=0,0,10,10'

.. code-block:: json

    {
      "type": "FeatureCollection",
      "features": [
        {
          "type": "Feature",
          "geometry": {
            "type": "Point",
            "coordinates": [
              -157.5,
              -22.5
            ]
          },
          "properties": {
            "point_geohash": "2",
            "cluster_count": 344
          }
        },
        {
          "type": "Feature",
          "geometry": {
            "type": "Point",
            "coordinates": [
              67.5,
              22.5
            ]
          },
          "properties": {
            "point_geohash": "t",
            "cluster_count": 320
          }
        }
      ]
    }
