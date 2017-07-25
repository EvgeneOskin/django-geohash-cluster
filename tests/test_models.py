#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_django-geohash-cluster
------------

Tests for `django-geohash-cluster` models module.
"""

from geohash_cluster import models


def test_clusterable_is_abstract():
    assert models.Clusterable.Meta.abstract
