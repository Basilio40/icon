from django.urls import path
from . import views

app_name = 'pessoa'

urlpatterns = [
    path('analise_desempenho_pessoas/<user>/', views.analise_desempenho_pessoas, name='analise_desempenho_pessoas'),
    path('analise_desempenho_pessoas/<user>/salvar/', views.salvar_objetivo_de_pessoas, name='salvar_objetivo_de_pessoas'),
    path('painel_desempenho_pessoas/<user>/', views.painel_desempenho_pessoas, name='painel_desempenho_pessoas'),
    path('multi_pessoas/<user>/', views.multi_pessoas, name='multi_pessoas'),
    path ('dashboard_pessoas/<user>/', views.dashboard_pessoas, name='dashboard_pessoas' ),
    path('objetivos/competencia/<user>/', views.competencia, name='competencia'),
    path('objetivos/engajamento/<user>/', views.engajamento, name='engajamento'),
    path('objetivos/retencao/<user>/', views.retencao, name='retencao'),

]
