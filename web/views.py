# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from web.models import Entidad, Enlace, Sesion
from web.forms import SesionForm
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.core.urlresolvers import reverse_lazy


def index(request):
    context_dict = {}
    return render(request, 'web/index.html', context_dict)


class EntidadList(ListView):
    model = Entidad


class EntidadCreate(CreateView):
    model = Entidad
    success_url = reverse_lazy('entidad')
    fields = ['nombre']


class EntidadUpdate(UpdateView):
    model = Entidad
    success_url = reverse_lazy('entidad')
    fields = ['nombre']


class EnlaceList(ListView):
    model = Enlace


class EnlaceCreate(CreateView):
    model = Enlace
    success_url = reverse_lazy('enlace')
    fields = ['nombre', 'apellido_pat', 'apellido_mat', 'cargo']


class EnlaceUpdate(UpdateView):
    model = Enlace
    success_url = reverse_lazy('enlace')
    fields = ['nombre', 'apellido_pat', 'apellido_mat', 'cargo']


class SesionList(ListView):
    model = Sesion


class SesionCreate(CreateView):
    form_class = SesionForm
    model = Sesion
    success_url = reverse_lazy('sesion')

class SesionUpdate(UpdateView):
    form_class = SesionForm
    model = Sesion
    success_url = reverse_lazy('sesion')
