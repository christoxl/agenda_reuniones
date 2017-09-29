# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from web.models import Entidad, Enlace, Sesion
from web.forms import EntidadForm, EnlaceForm, SesionForm


def index(request):
    context_dict = {}
    return render(request, 'web/index.html', context_dict)


def entidad(request):
    entidad_list = Entidad.objects.all()
    context_dict = {'entidades': entidad_list}

    return render(request, 'web/entidad.html', context_dict)


def enlace(request):
    enlace_list = Enlace.objects.all()
    context_dict = {'enlaces': enlace_list}

    return render(request, 'web/enlace.html', context_dict)


def sesion(request):
    sesion_list = Sesion.objects.all()
    context_dict = {'sesiones': sesion_list}

    return render(request, 'web/sesion.html', context_dict)


def add_entidad(request):
    form = EntidadForm()

    if request.method == 'POST':
        form = EntidadForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return entidad(request)
        else:
            print(form.errors)

    return render(request, 'web/add_entidad.html', {'form': form})


def add_enlace(request):
    form = EnlaceForm()

    if request.method == 'POST':
        form = EnlaceForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return enlace(request)
        else:
            print(form.errors)

    return render(request, 'web/add_enlace.html', {'form': form})


def add_sesion(request):
    form = SesionForm()

    if request.method == 'POST':
        form = SesionForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return sesion(request)
        else:
            print(form.errors)

    return render(request, 'web/add_sesion.html', {'form': form})
