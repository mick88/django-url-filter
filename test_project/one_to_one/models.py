# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals

import six
from django.db import models


@six.python_2_unicode_compatible
class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

    def __str__(self):
        return "%s the place" % self.name


@six.python_2_unicode_compatible
class Restaurant(models.Model):
    place = models.OneToOneField(Place, primary_key=True)
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)

    def __str__(self):
        return "%s the restaurant" % self.place.name


@six.python_2_unicode_compatible
class Waiter(models.Model):
    restaurant = models.ForeignKey(Restaurant, null=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return "%s the waiter at %s" % (self.name, self.restaurant)
