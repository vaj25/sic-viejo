"""sic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""

from django.conf.urls import include, url
from django.contrib import admin
from contable.views import ingresar ,inicio ,transaccion ,planillaEmpleados ,eliminar_emp ,comprobacion ,resultado ,capital ,general ,libroDiario ,ajustes ,acercaDe ,cerrarPeriodo ,costos ,peranteriores ,iniciarPeriodo ,ingresarUsuario ,ingresar_empleado

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)) ,
    url(r'^index/', inicio) ,
    url(r'^ingresar/$',ingresar) ,
    url(r'^cerrar/$', 'contable.views.cerrar'),
    url(r'^empleado/', ingresar_empleado),
    url(r'^cuenta/', 'contable.views.ingresar_cuenta'),
    url(r'^planilla/empleados', planillaEmpleados) ,
    url(r'^catalogo/cuentas', 'contable.views.catalogoCuentas') ,
    url(r'^$',ingresar),
    url(r'^transaccion', transaccion) ,
    url(r'^eliminar', eliminar_emp) ,
    url(r'^comprobacion', comprobacion) ,
    url(r'^resultado', resultado) ,
    url(r'^capital', capital) ,
    url(r'^general', general) ,
    url(r'^libroDiario', libroDiario) ,
    url(r'^ajustes', ajustes) ,
    url(r'^acercaDe', acercaDe) ,
    url(r'^cerrarPeriodo', cerrarPeriodo) ,
    url(r'^costos', costos) ,
    url(r'^perant', peranteriores) ,
    url(r'^iniciarPeriodo', iniciarPeriodo) ,
    url(r'^ingresarUsuario', ingresarUsuario) ,
]
