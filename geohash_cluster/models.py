# -*- coding: utf-8 -*-
"""Modules provides Django Model and Quetyset for clustering."""
from django.contrib.gis.db import models
from django.contrib.gis.db.models.functions import GeoHash


class ClusterableQuerySet(models.QuerySet):
    """Class is a Queryset that provides a clustering feature.

    * Call `cluster_points(geohash_precision)` to create a clusters.
    * Call `filter_clusters(geohash) to filter only places at this cluster.
    """

    def cluster_points(self, precision):
        """Cluster modeles by geohash value with provided `precision`."""
        field = self._geohash_field()
        return self._annotate_geohash(precision).values(field).annotate(
            cluster_count=models.Count(field),
        )

    def filter_cluster(self, geohash):
        """Filter points by the `geohash`."""
        field = self._geohash_field()
        return self._annotate_geohash(len(geohash)).filter(**{field: geohash})

    def _annotate_geohash(self, precision):
        field = self._geohash_field()
        point_field = self.model.GEOCLUSTER_FIELD
        return self.annotate(**{field: GeoHash(point_field, precision)})

    def _geohash_field(self):
        field = self.model.GEOCLUSTER_FIELD
        return field + '_geohash'


class Pointed(models.Model):
    """Module provides `point` field and `ClusterableQuerySet`-ready model."""

    point = models.PointField()
    GEOCLUSTER_FIELD = 'point'

    class Meta:  # noqa
        abstract = True
