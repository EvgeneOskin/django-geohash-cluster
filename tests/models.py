from geohash_cluster.models import Pointed, ClusterableQuerySet


class Place(Pointed):

    objects = ClusterableQuerySet.as_manager()

    class Meta:
        app_label = 'tests'
