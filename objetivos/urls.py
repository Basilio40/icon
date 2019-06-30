from django.urls import path
from . import views

app_name = 'objetivos'

urlpatterns = [
    path('receitas/<user>/', views.definir_objetivo_de_receitas, name='objetivo_de_receitas'),
    path('receitas/<user>/salvar/', views.salvar_objetivo_de_receitas, name='salvar_objetivo_de_receitas'),
    path('rentabilidade/<user>/', views.definir_objetivo_de_rentabilidade, name='objetivo_de_rentabilidade'),
    path('rentabilidade/<user>/salvar/', views.salvar_objetivo_de_rentabilidade, name='salvar_objetivo_de_rentabilidade'),
    path('endividamento/<user>/', views.definir_objetivo_de_endividamento, name='objetivo_de_endividamento'),
    path('endividamento/<user>/salvar/', views.salvar_objetivo_de_endividamento, name='salvar_objetivo_de_endividamento'),
    path('analise/<user>/', views.analise_desempenho_financeiro, name='analise_desempenho_financeiro'),
    path('analise/<user>/salvar/', views.salvar_analise_desempenho_financeiro, name='salvar_analise_desempenho_financeiro'),
    path('custos/<user>/', views.definir_objetivo_de_custos, name='objetivo_de_custos'),
    path('custos/<user>/salvar/', views.salvar_objetivo_de_custos, name='salvar_objetivo_de_custos'),
    path('orcamento/<user>/', views.definir_orcamento_mensal, name='definir_orcamento_mensal'),
    path('orcamento/<user>/salvar/', views.salvar_orcamento_mensal, name='salvar_orcamento_mensal'),
]
