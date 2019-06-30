from django.urls import path
from . import views

app_name = 'mapa'

urlpatterns = [
    path('mapa_estrategico/<user>/', views.mapa_estrategico, name='mapa_estrategico'),
    
]
