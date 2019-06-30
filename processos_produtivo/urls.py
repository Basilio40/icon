from django.urls import path
from . import views

app_name = 'processos_produtivo'

urlpatterns = [
    path('processos_produtivos/<user>/', views.analise_desemp_processos_produtivos, name='analise_desemp_processos_produtivos'),
    path('processos_produtivos/<user>/salvar/', views.salvar_objetivo_de_processos, name='salvar_objetivo_de_processos'),
    path('painel_desempenho_processos_produtivos/<user>',views.painel_desempenho_processos_produtivos, name='painel_desempenho_processos_produtivos'),
    path('dashboard_processos/<user>/', views.dashboard_processos, name='dashboard_processos'),
    path('objetivos/produtividade/<user>/', views.produtividade, name='produtividade'),
    path('objetivos/qualidade/<user>/', views.qualidade, name='qualidade'),
    path('objetivos/prazos_estoques/<user>/', views.prazos_estoques, name='prazos_estoques'),

]
