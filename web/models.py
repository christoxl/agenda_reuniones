# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Entidad(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

    def __unicode__(self):
        return self.nombre


class Enlace(models.Model):
    nombre = models.CharField(max_length=200)
    apellido_pat = models.CharField(max_length=200)
    apellido_mat = models.CharField(max_length=200)
    cargo = models.CharField(max_length=200)

    def __str__(self):
        return (self.nombre + self.apellido_pat)

    def __unicode__(self):
        return (self.nombre + self.apellido_pat)


class Sesion(models.Model):
    nombre = models.CharField(max_length=200)
    fecha = models.DateTimeField()
    acuerdo = models.TextField(null=True)
    fecha_prox = models.DateTimeField()
    entidad = models.ForeignKey(Entidad)
    enlaces = models.ManyToManyField(Enlace)

    def __str__(self):
        return (str(self.entidad) + ' - ' + self.nombre)

    def __unicode__(self):
        return (str(self.entidad) + ' - ' + self.nombre)
