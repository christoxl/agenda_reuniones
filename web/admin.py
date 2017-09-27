# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from web.models import Entidad, Enlace, Sesion

admin.site.register(Entidad)
admin.site.register(Enlace)
admin.site.register(Sesion)
