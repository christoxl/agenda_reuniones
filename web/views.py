# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from web.models import Entidad, Enlace, Sesion
from web.forms import SesionForm
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.http import JsonResponse


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


class EntidadDelete(DeleteView):
    model = Entidad
    success_url = reverse_lazy('entidad')


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


class EnlaceDelete(DeleteView):
    model = Enlace
    success_url = reverse_lazy('enlace')


class SesionList(ListView):
    model = Sesion


class SesionDetail(DetailView):
    model = Sesion


class SesionCreate(CreateView):
    form_class = SesionForm
    model = Sesion
    success_url = reverse_lazy('sesion')


class SesionUpdate(UpdateView):
    form_class = SesionForm
    model = Sesion
    success_url = reverse_lazy('sesion')


class SesionDelete(DeleteView):
    model = Sesion
    success_url = reverse_lazy('sesion')


def json_calendar(request):
    start = request.GET.get('start')
    end = request.GET.get('end')

    if start is None or end is None:
        json_data = [{"request": "bad_request"}]
    else:
        sesions = Sesion.objects.filter(fecha_prox__range=(start, end))
        json_data = [{"title": sesion.nombre, "start": sesion.fecha_prox, "url": "/sesion/1/"} 
                     for sesion in sesions]
    return JsonResponse(json_data, safe=False)
