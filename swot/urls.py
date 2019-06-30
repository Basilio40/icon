from swot import views
from django.urls import path

app_name = 'swot'

urlpatterns = [
    path('questionario/<user>/', views.questionario, name='questionario'),
    path('analise_swot/<user>/', views.analise_swot, name='analise_swot'),
    path('questionario/<user>/salvar/', views.salvar_resposta_questionario, name='salvar_resposta_questionario'),
    path('concorrencia/<user>/', views.swot_concorrencia, name='swot_concorrencia'),
    path('concorrencia/<user>/salvar/', views.salvar_analise_concorrencia, name='salvar_analise_concorrencia'),
    path('concorrencia/<user>/salvar/concorrente/', views.salvar_concorrente, name='salvar_concorrente'),
    path('concorrencia/<user>/salvar_nome/', views.alterar_nome_concorrente, name='salvar_nome_concorrente'),
    path('clientes/<user>/', views.swot_clientes, name='swot_clientes' ),
    path('clientes/<user>/salvar/', views.salvar_analise_clientes, name='salvar_analise_clientes' ),
    path('clientes/<user>/salvar/clientes/', views.salvar_clientes, name='salvar_clientes' ),
    path('clientes/<user>/salvar_nome/', views.alterar_nome_cliente, name='salvar_nome_cliente'),
    path('fornecedores/<user>/', views.swot_fornecedores, name='swot_fornecedores' ),
    path('fornecedores/<user>/salvar/', views.salvar_analise_fornecedores, name='salvar_analise_fornecedores' ),
    path('fornecedores/<user>/salvar/fornecedores/', views.salvar_fornecedores, name='salvar_fornecedores' ),
    path('fornecedores/<user>/salvar_nome/', views.alterar_nome_fornecedor, name='salvar_nome_fornecedor'),
    path('macro/<user>/', views.swot_macro, name='swot_macro' ),
    path('macro/<user>/salvar/', views.salvar_analise_macro, name='salvar_analise_macro' ),
    path('macro/<user>/salvar/fornecedores/', views.salvar_macro, name='salvar_macro' ),
]
