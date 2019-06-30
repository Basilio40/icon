"""icon URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from core.views import home
from django.urls import path

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^conta/', include('accounts.urls', namespace='accounts')),
    # url(r'^reset/', include('password_reset.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^dre/', include('dre.urls', namespace='dre')),
    path('objetivos/', include('objetivos.urls')),
    path('swot/', include('swot.urls')),
    path('graficos/', include('graficos.urls')),
    path('vendas/', include('vendas.urls')),
    path('processos_produtivo/',include('processos_produtivo.urls')),
    path('pessoa/',include('pessoa.urls')),
    path('processos_produtivo/', include('processos_produtivo.urls')),
    path('pessoa/', include('pessoa.urls')),
    path('mapa/', include('mapa.urls')),
]
