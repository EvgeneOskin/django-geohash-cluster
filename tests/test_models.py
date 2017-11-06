#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from model_mommy import mommy

import geohash
from .models import Place


@pytest.mark.django_db
def test_annotate_geohash():
    place = mommy.make(Place)
    qs = Place.objects.cluster_points(precision=12)
    x, y = place.point
    assert qs[0]['point_geohash'] == geohash.encode(y, x, 12)


@pytest.mark.django_db
def test_group():
    mommy.make(Place, _quantity=100)
    qs = Place.objects.cluster_points(1)
    assert qs.count() <= 26 * 2  # group by a last char in geohash
