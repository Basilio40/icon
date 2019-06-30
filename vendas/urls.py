from django.urls import path
from . import views

app_name = 'vendas'

urlpatterns = [
    path('objetivo_vendas/<user>/', views.definir_objetivo_de_vendas, name='analise_desempenho_vendas'),
    path('objetivo_vendas/<user>/salvar/', views.salvar_objetivo_de_vendas, name='salvar_desempenho_vendas'),
    path('desempenho_vendas/<user>/', views.painel_desempenho_vendas, name='painel_desempenho_vendas'),
    path('dashboard_vendas/<user>/', views.dashboard_vendas, name='dashboard_vendas' ),
    path('vendas/<user>/<ano>/', views.detail_vendas, name='vendas_detail' ),
    path('objetivos/mkt_relacionamento/<user>/', views.mkt_relacionamento, name='mkt_relacionamento'),
    path('objetivos/metas_vendas/<user>/', views.metas_vendas, name='metas_vendas'),
    path('objetivos/satisfacao_clientes/<user>/', views.satisfacao_clientes, name='satisfacao_clientes'),

]
