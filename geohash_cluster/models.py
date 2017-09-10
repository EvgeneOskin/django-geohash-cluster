# -*- coding: utf-8 -*-

from django.contrib.gis.db import models
from django.contrib.gis.db.models.functions import GeoHash

from .settings import settings
import geohash


class ClusterableQuerySet(models.QuerySet):

    def cluster(self, precision):
        field = self.model.GEOCLUSTER_FIELD

        return self.annotate(geohash=GeoHash(field, precision))

    def filter_cluster(self, geohash):
        return qs.filter(geohash__endswith=geohash)


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
        super(GeoHashAndPoint, self).save(*args, **kwargs)


def get_geohash(point):
    assert point.srid is not None, 'You must set srid for the point!'

    x_coord, y_coord = point.transform(4326, clone=True)  # WGS84
    return geohash.encode(y_coord, x_coord, settings.GEOHASH_LENGTH)
