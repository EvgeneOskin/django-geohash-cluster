# -*- coding: utf-8 -*-
"""Module provides Django Rest Framework Serializer and Filter for Clusters."""
from django.contrib.gis.geos import Point

from rest_framework.serializers import CharField, IntegerField
from rest_framework.filters import BaseFilterBackend
from rest_framework_gis.serializers import (
    GeoFeatureModelSerializer,
    GeometrySerializerMethodField,
)

import geohash
from .models import Pointed


class ClusterSerializer(GeoFeatureModelSerializer):
    """A class to serialize locations as GeoJSON compatible data."""

    point = GeometrySerializerMethodField()
    point_geohash = CharField()
    cluster_count = IntegerField()

    class Meta:  # noqa
        model = Pointed
        id_field = False
        geo_field = "point"
        fields = ['point', 'point_geohash', 'cluster_count']

    def get_point(self, obj):
        """Parse a geohashed point to Geometry."""
        y, x = geohash.decode(obj['point_geohash'])
        return Point(x, y)


class ClusterFilter(BaseFilterBackend):
    """Class is a DRF filter that cluster the queryset by geohash."""

    zoomToGeoHashPrecision = {
        0: 1,
        1: 2,
        2: 2,
        3: 2,
        4: 3,
        5: 3,
        6: 4,
        7: 4,
        8: 4,
        9: 5,
        10: 5,
        11: 6,
        12: 6,
        13: 6,
        14: 7,
        15: 7,
        16: 7,
        17: 7,
        18: 7,
        19: 7,
        20: 7,
        21: 7
    }

    def filter_queryset(self, request, queryset, view):
        """Filter queryset by zoom level."""
        zoom_level = float(request.query_params.get('zoom') or 0)
        precision = self._zoom_level_to_geohash_precision(zoom_level)
        return queryset.cluster_points(int(precision))

    def _zoom_level_to_geohash_precision(self, zoom_level):
        return self.zoomToGeoHashPrecision.get(int(zoom_level), 7)
