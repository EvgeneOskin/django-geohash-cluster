# -*- coding: utf-8
from __future__ import unicode_literals, absolute_import

import django
import dj_database_url
from mommy_spatial_generators import MOMMY_SPATIAL_FIELDS

DEBUG = True
USE_TZ = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww"

DATABASES = {}
DATABASES['default'] = dj_database_url.config(
    default=('postgis://geohash:test@localhost:5432/geohash')
)

ROOT_URLCONF = "tests.urls"

INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sites",
    "geohash_cluster",
    "django.contrib.gis",
    "tests"
]

SITE_ID = 1

if django.VERSION >= (1, 10):
    MIDDLEWARE = ()
else:
    MIDDLEWARE_CLASSES = ()


MOMMY_CUSTOM_FIELDS_GEN = MOMMY_SPATIAL_FIELDS
