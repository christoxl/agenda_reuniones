"""project_agenda_reuniones URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from web import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^agregar-entidad/$', views.add_entidad, name='add_entidad'),
    url(r'^agregar-enlace/$', views.add_enlace, name='add_enlace'),
    url(r'^agregar-sesion/$', views.add_sesion, name='add_sesion'),
    url(r'^admin/', admin.site.urls),
]
