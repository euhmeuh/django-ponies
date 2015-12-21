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

"""api URL Configuration
"""

from django.conf.urls import include, url
from tastypie.api import Api

from .api import PonyResource

v1_api = Api(api_name='v1')
v1_api.register(PonyResource())

urlpatterns = [
    url(r'', include(v1_api.urls)),
]
