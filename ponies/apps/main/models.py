# -*- coding: utf-8 -*-
#
# django-ponies
# Sample Django project to get started
#
# Inspired by mibou
#
# Copyright (C) 2016 euhmeuh
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from django.db import models

from .choices import PONY_TYPE_CHOICES


class Faction(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Pony(models.Model):
    class Meta:
        verbose_name_plural = 'ponies'

    name = models.CharField(max_length=50)
    pony_type = models.CharField(max_length=1, choices=PONY_TYPE_CHOICES, null=True)
    short_desc = models.CharField(max_length=150, blank=True)
    long_desc = models.TextField(blank=True)
    faction = models.ForeignKey(Faction, blank=True, null=True)
    image_url = models.CharField(max_length=2048, blank=True, null=True)

    def __str__(self):
        return self.name

