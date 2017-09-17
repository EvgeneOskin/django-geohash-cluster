#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from model_mommy import mommy

from django.db.models import Count
from geohash_cluster import models
import geohash
from .models import Place, Pointed


@pytest.mark.django_db
def test_has_geohash():
    place = mommy.make(Place)
    assert len(place.geohash) != 0


@pytest.mark.django_db
def test_annotate_geohash():
    pointed = mommy.make(Pointed)
    qs = Pointed.objects.cluster_points(precision=12)
    x, y = pointed.point
    assert qs[0]['point_geohash'] == geohash.encode(y, x, 12)


@pytest.mark.django_db
def test_group():
    place = mommy.make(Place, _quantity=100)
    qs = Place.objects.cluster_geohash(0)
    assert qs.count() <= 26*2  # group by a last char in geohash
