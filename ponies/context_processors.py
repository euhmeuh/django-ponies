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

import ponies.settings

def settings(request):
    return {
        'STATIC_URL': ponies.settings.STATIC_URL,
        'SITE_DESCRIPTION': '',
        'SITE_KEYWORDS': '',
        'SITE_AUTHOR': ''
    }
