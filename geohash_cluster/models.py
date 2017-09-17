# -*- coding: utf-8 -*-

from django.contrib.gis.db import models
from django.db.models.functions import Substr, Lower
from django.contrib.gis.db.models.functions import GeoHash

from .settings import settings


class ClusterableQuerySet(models.QuerySet):

    def cluster_points(self, precision):
        field = self.geohash_field()
        return self.annotate_geohash(precision).values(field).annotate(
            cluster_count=models.Count(field),
        )

    def filter_cluster(self, geohash):
        field = self.geohash_field()
        return self.annotate_geohash(len(geohash)).filter(**{field: geohash})

    def annotate_geohash(self, precision):
        field = self.geohash_field()
        point_field = self.model.GEOCLUSTER_FIELD
        return self.annotate(**{field: GeoHash(point_field, precision)})

    def geohash_field(self):
        field = self.model.GEOCLUSTER_FIELD
        return field + '_geohash'


class Pointed(models.Model):

    point = models.PointField()
    GEOCLUSTER_FIELD = 'point'

    class Meta:
        abstract = True
