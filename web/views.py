# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from web.forms import EntidadForm, EnlaceForm, SesionForm


def index(request):
    context_dict = {}
    return render(request, 'web/index.html', context_dict)


def add_entidad(request):
    form = EntidadForm()

    if request.method == 'POST':
        form = EntidadForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print(form.errors)

    return render(request, 'web/add_entidad.html', {'form': form})


def add_enlace(request):
    form = EnlaceForm()

    if request.method == 'POST':
        form = EnlaceForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print(form.errors)

    return render(request, 'web/add_enlace.html', {'form': form})


def add_sesion(request):
    form = SesionForm()

    if request.method == 'POST':
        form = SesionForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print(form.errors)

    return render(request, 'web/add_sesion.html', {'form': form})
