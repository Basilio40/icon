from graficos import views
from django.urls import path

app_name = 'graficos'

urlpatterns = [
    path('dre/<user>/', views.grafico_dre, name='grafico_dre'),
    path('inicial/<user>/', views.ped_inicial, name='ped_inicial'),
    path('gestao/<user>/', views.ped_gestao, name='ped_gestao'),
    path('desempenho/<user>/', views.ped_desempenho, name='ped_desempenho'),
    path('diagnostico/<user>/', views.ped_diagnostico, name='ped_diagnostico'),
    path('diagnostico/externo/<user>/', views.diagnostico_amb_ext, name='diagnostico_amb_ext'),
    path('diagnostico/interno/<user>/', views.diagnostico_amb_int, name='diagnostico_amb_int')
]
