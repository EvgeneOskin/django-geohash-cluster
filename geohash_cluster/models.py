# -*- coding: utf-8 -*-

from django.contrib.gis.db import models
from .settings import settings


class ClusterableQuerySet(models.QuerySet):

    def cluster(self, precision):
        field = self.model.GEOCLUSTER_FIELD

        return self.annotate(geohash=models.GeoHash(field, precision))

    def filter_cluster(self, geohash):
        field = self.model.GEOCLUSTER_FIELD

        return qs.filter(**{field + '__endswith': geohash})


class GeoHashed(models.Model):

    geohash = models.CharField(max_length=settings.GEOHASH_LENGTH)
    GEOCLUSTER_FIELD = 'geohash'

    class Meta(object):
        abstract = True

    def set_geohash(self, point):
        self.geohash = get_geohash(point)


class GeoHashAndPoint(GeoHashed):

    point = models.PointField()

    def save(self, *args, **kwargs):
        if self.geohash is None:
            self.set_geohash(self.point)
        self.geohash = geohash.encode(self.point, settings.GEOHASH_LENGTH)


def get_geohash(point):
    assert point.srid is not None, 'You must set srid for the point!'

    x_coord, y_coord = point.transform(4326, clone=True)  # WGS84
    return geohash.encode(x_coord, y_coord, settings.GEOHASH_LENGTH)
