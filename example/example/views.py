from rest_framework.viewsets import ReadOnlyModelViewSet

from rest_framework_gis.filters import InBBoxFilter
from geohash_cluster.rest_framework import ClusterSerializer, ClusterFilter

from .models import Place


class Cluster(ReadOnlyModelViewSet):
    queryset = Place.objects
    bbox_filter_field = 'point'
    filter_backends = (InBBoxFilter, ClusterFilter)
    serializer_class = ClusterSerializer
