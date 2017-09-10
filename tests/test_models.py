#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from model_mommy import mommy

from geohash_cluster import models
from .models import Place, Pointed


@pytest.mark.parametrize('model', [
    models.GeoHashAndPoint,
    models.GeoHashed,
])
def test_clusterable_is_abstract(model):
    assert model.Meta.abstract


@pytest.mark.django_db
def test_has_geohash():
    model = mommy.make(Place)
    assert model.geohash.length != 0
