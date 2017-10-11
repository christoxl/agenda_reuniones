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

    url(r'^entidad$', views.EntidadList.as_view(), name='entidad'),
    url(r'^entidad/agregar/$', views.EntidadCreate.as_view(), name='add_entidad'),
    url(r'^entidad/editar/(?P<slug>[\w\-]+)/$', views.EntidadUpdate.as_view(), name='update_entidad'),
    url(r'^entidad/borrar/(?P<slug>[\w\-]+)$', views.EntidadDelete.as_view(), name='delete_entidad'),

    url(r'^enlace$', views.EnlaceList.as_view(), name='enlace'),
    url(r'^enlace/agregar/$', views.EnlaceCreate.as_view(), name='add_enlace'),
    url(r'^enlace/editar/(?P<pk>\d+)/$', views.EnlaceUpdate.as_view(), name='update_enlace'),
    url(r'^enlace/borrar/(?P<pk>\d+)/$', views.EnlaceDelete.as_view(), name='delete_enlace'), 

    url(r'^sesion$', views.SesionList.as_view(), name='sesion'),
    url(r'^sesion/agregar/$', views.SesionCreate.as_view(), name='add_sesion'),
    url(r'^sesion/editar/(?P<pk>\d+)/$', views.SesionUpdate.as_view(), name='update_sesion'),
    url(r'^sesion/borrar/(?P<pk>\d+)/$', views.SesionDelete.as_view(), name='delete_sesion'),

    url(r'^admin/', admin.site.urls),
]
