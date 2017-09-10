from django.contrib.gis.db import models

from geohash_cluster.models import (
    GeoHashed, GeoHashAndPoint,
    ClusterableQuerySet,
)


class Place(GeoHashAndPoint):

    objects = ClusterableQuerySet.as_manager()

    class Meta:
        app_label = 'tests'


class Pointed(models.Model):

    point = models.PointField()
    objects = ClusterableQuerySet.as_manager()
    GEOCLUSTER_FIELD = 'point'

    class Meta:
        app_label = 'tests'
