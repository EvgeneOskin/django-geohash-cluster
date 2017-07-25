# -*- coding: utf-8 -*-

from django.db import models


class Clusterable(models.Model):

    class Meta:
        abstract = True
