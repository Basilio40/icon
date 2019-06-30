from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import *
from accounts.decorators import is_allowed
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .utils import calcula_competitividade

# Create your views here.
@login_required
@is_allowed
def questionario(request, user):
    # Objetos do banco de dados
    owner = get_object_or_404(User, username=user)
    questoes = Questao.objects.all()
    respostas = []
    for questao in questoes:
        resposta = Resposta.objects.get_or_create(questao=questao, user=owner)[0]
        respostas.append(resposta)

    questionario = zip(questoes, respostas)
    dicio_retorno = {'questionario': questionario}

    return render(request, 'swot/questionario.html', dicio_retorno)

@login_required
@is_allowed
def analise_swot(request, user):

    return render(request, 'swot/analise_swot.html')

@login_required
@csrf_exempt
@is_allowed
def salvar_resposta_questionario(request, user):
    if request.method == 'POST':
        owner = get_object_or_404(User, username=user)
        questao = Questao.objects.get(pk=request.POST['questao'])
        resposta_user = Resposta.objects.get(questao=questao, user=owner)
        resposta_user.resposta = request.POST['resposta']
        resposta_user.save()
    return HttpResponse('')

@login_required
@is_allowed
def swot_concorrencia(request, user):
    owner = get_object_or_404(User, username=user)
    concorrentes = Concorrente.objects.filter(user=owner)
    analise = AnaliseConcorrencia.objects.get_or_create(user=owner)[0]

    competitividade = {'preco': 0, 'qualidade': 0, 'entrega': 0, 'inovacao': 0, 'portifolio': 0}
    for concorrente in concorrentes:
        competitividade['preco'] += calcula_competitividade(concorrente.preco)
        competitividade['qualidade'] += calcula_competitividade(concorrente.qualidade)
        competitividade['entrega'] += calcula_competitividade(concorrente.entrega)
        competitividade['inovacao'] += calcula_competitividade(concorrente.inovacao)
        competitividade['portifolio'] += calcula_competitividade(concorrente.portifolio)
    competitividade_media = 0.0
    for i in competitividade:
        try:
            competitividade[i] = (competitividade[i] / (len(concorrentes)*2))*100
            competitividade_media += competitividade[i]
        except:
            pass
    competitividade['media'] = competitividade_media / 5

    choices = {
        'objetivo_1': ['Aumento de Receitas','Lançar Novos Produto/Serviços','Aumentar Fatia de Mercado','Soluções Customizadas','Gerar inovação na empresa','Oferecer novos produtos','Regularização da empresa','Melhorar Governança e Compliance','Customização de Produtos e Serviços','Segmentação de Clientes','Atender Público por faixa etária','Produtos customizados para idosos','Produtos customizados para jovens'],
        'objetivo_2': ['Aumento de Receitas','Lançar Novos Produto/Serviços','Aumentar Fatia de Mercado','Soluções Customizadas','Gerar inovação na empresa','Oferecer novos produtos','Regularização da empresa','Melhorar Governança e Compliance','Customização de Produtos e Serviços','Segmentação de Clientes','Atender Público por faixa etária','Produtos customizados para idosos','Produtos customizados para jovens'],
        'objetivo_3': ['Aumento de Receitas','Lançar Novos Produto/Serviços','Aumentar Fatia de Mercado','Soluções Customizadas','Gerar inovação na empresa','Oferecer novos produtos','Regularização da empresa','Melhorar Governança e Compliance','Customização de Produtos e Serviços','Segmentação de Clientes','Atender Público por faixa etária','Produtos customizados para idosos','Produtos customizados para jovens'],
        'objetivo_4': ['Aumento de Receitas','Lançar Novos Produto/Serviços','Aumentar Fatia de Mercado','Soluções Customizadas','Gerar inovação na empresa','Oferecer novos produtos','Regularização da empresa','Melhorar Governança e Compliance','Customização de Produtos e Serviços','Segmentação de Clientes','Atender Público por faixa etária','Produtos customizados para idosos','Produtos customizados para jovens'],
        'objetivo_5': ['Aumento de Receitas','Lançar Novos Produto/Serviços','Aumentar Fatia de Mercado','Soluções Customizadas','Gerar inovação na empresa','Oferecer novos produtos','Regularização da empresa','Melhorar Governança e Compliance','Customização de Produtos e Serviços','Segmentação de Clientes','Atender Público por faixa etária','Produtos customizados para idosos','Produtos customizados para jovens'],
        'ameaca_1': ['Necessidade de Investimentos','Aumento da Concorrencia','Aumento de Custos','Obsolecencia de Produtos/Serviços','Multas','Perda de Mercado','Perda de clientes','xyz','editar'],
        'ameaca_2': ['Necessidade de Investimentos','Aumento da Concorrencia','Aumento de Custos','Obsolecencia de Produtos/Serviços','Multas','Perda de Mercado','Perda de clientes','xyz','editar'],
        'ameaca_3': ['Necessidade de Investimentos','Aumento da Concorrencia','Aumento de Custos','Obsolecencia de Produtos/Serviços','Multas','Perda de Mercado','Perda de clientes','xyz','editar'],
        'ameaca_4': ['Necessidade de Investimentos','Aumento da Concorrencia','Aumento de Custos','Obsolecencia de Produtos/Serviços','Multas','Perda de Mercado','Perda de clientes','xyz','editar'],
        'ameaca_5': ['Necessidade de Investimentos','Aumento da Concorrencia','Aumento de Custos','Obsolecencia de Produtos/Serviços','Multas','Perda de Mercado','Perda de clientes','xyz','editar'],
    }

    dicio_retorno = {'concorrentes': concorrentes,
                     'opcoes_concorrentes': ['Sou melhor', 'Sou igual', 'Sou inferior'],
                     'competitividade': competitividade, 'analise': analise,
                     'choices': choices
                    }
    return render(request, 'swot/swot_concorrencia.html', dicio_retorno)

@login_required
@csrf_exempt
@is_allowed
def salvar_concorrente(request, user):
    if request.method == 'POST':
        try:
            owner = get_object_or_404(User, username=user)
            concorrente = Concorrente.objects.get(pk=int(request.POST['pk']),user=owner)
            concorrente.preco = request.POST['preco']
            concorrente.qualidade = request.POST['qualidade']
            concorrente.entrega = request.POST['entrega']
            concorrente.inovacao = request.POST['inovacao']
            concorrente.portifolio = request.POST['portifolio']
            concorrente.save()
        except:
            pass
    return HttpResponse('')

@login_required
@csrf_exempt
@is_allowed
def salvar_analise_concorrencia(request, user):
    if request.method == 'POST':
        owner = get_object_or_404(User, username=user)
        analise = AnaliseConcorrencia.objects.get(user=owner)
        analise.ameaca_1 = request.POST['ameaca_1']
        analise.ameaca_1_probabilidade = request.POST['ameaca_1_probabilidade']
        analise.ameaca_1_relevancia = request.POST['ameaca_1_relevancia']
        analise.ameaca_2 = request.POST['ameaca_2']
        analise.ameaca_2_probabilidade = request.POST['ameaca_2_probabilidade']
        analise.ameaca_2_relevancia = request.POST['ameaca_2_relevancia']
        analise.ameaca_3 = request.POST['ameaca_3']
        analise.ameaca_3_probabilidade = request.POST['ameaca_3_probabilidade']
        analise.ameaca_3_relevancia = request.POST['ameaca_3_relevancia']
        analise.ameaca_4 = request.POST['ameaca_4']
        analise.ameaca_4_probabilidade = request.POST['ameaca_4_probabilidade']
        analise.ameaca_4_relevancia = request.POST['ameaca_4_relevancia']
        analise.ameaca_5 = request.POST['ameaca_5']
        analise.ameaca_5_probabilidade = request.POST['ameaca_5_probabilidade']
        analise.ameaca_5_relevancia = request.POST['ameaca_5_relevancia']
        analise.objetivo_1 = request.POST['objetivo_1']
        analise.objetivo_1_atratividade = request.POST['objetivo_1_atratividade']
        analise.objetivo_1_probabilidade = request.POST['objetivo_1_probabilidade']
        analise.objetivo_2 = request.POST['objetivo_2']
        analise.objetivo_2_atratividade = request.POST['objetivo_2_atratividade']
        analise.objetivo_2_probabilidade = request.POST['objetivo_2_probabilidade']
        analise.objetivo_3 = request.POST['objetivo_3']
        analise.objetivo_3_atratividade = request.POST['objetivo_3_atratividade']
        analise.objetivo_3_probabilidade = request.POST['objetivo_3_probabilidade']
        analise.objetivo_4 = request.POST['objetivo_4']
        analise.objetivo_4_atratividade = request.POST['objetivo_4_atratividade']
        analise.objetivo_4_probabilidade = request.POST['objetivo_4_probabilidade']
        analise.objetivo_5 = request.POST['objetivo_5']
        analise.objetivo_5_atratividade = request.POST['objetivo_5_atratividade']
        analise.objetivo_5_probabilidade = request.POST['objetivo_5_probabilidade']
        analise.save()
    return HttpResponse('')

#CLIENTES#

def swot_clientes(request, user):
    owner = get_object_or_404(User, username=user)
    clientes = Cliente.objects.filter(user=owner)
    analise = AnaliseClientes.objects.get_or_create(user=owner)[0]

    competitividade = {'preco': 0, 'qualidade': 0, 'entrega': 0, 'inovacao': 0, 'portifolio': 0}
    for cliente in clientes:
        competitividade['preco'] += calcula_competitividade(cliente.preco)
        competitividade['qualidade'] += calcula_competitividade(cliente.qualidade)
        competitividade['entrega'] += calcula_competitividade(cliente.entrega)
        competitividade['inovacao'] += calcula_competitividade(cliente.inovacao)
        competitividade['portifolio'] += calcula_competitividade(cliente.portifolio)
    competitividade_media = 0.0
    for i in competitividade:
        try:
            competitividade[i] = (competitividade[i] / (len(clientes)*2))*100
            competitividade_media += competitividade[i]
        except:
            pass
    competitividade['media'] = competitividade_media / 5

    choices = {
        'objetivo_1': ['Aumento de Receitas','Lançar Novos Produto/Serviços','Aumentar Fatia de Mercado','Soluções Customizadas','Gerar inovação na empresa','Oferecer novos produtos','Regularização da empresa','Melhorar Governança e Compliance','Customização de Produtos e Serviços','Segmentação de Clientes','Atender Público por faixa etária','Produtos customizados para idosos','Produtos customizados para jovens'],
        'objetivo_2': ['Aumento de Receitas','Lançar Novos Produto/Serviços','Aumentar Fatia de Mercado','Soluções Customizadas','Gerar inovação na empresa','Oferecer novos produtos','Regularização da empresa','Melhorar Governança e Compliance','Customização de Produtos e Serviços','Segmentação de Clientes','Atender Público por faixa etária','Produtos customizados para idosos','Produtos customizados para jovens'],
        'objetivo_3': ['Aumento de Receitas','Lançar Novos Produto/Serviços','Aumentar Fatia de Mercado','Soluções Customizadas','Gerar inovação na empresa','Oferecer novos produtos','Regularização da empresa','Melhorar Governança e Compliance','Customização de Produtos e Serviços','Segmentação de Clientes','Atender Público por faixa etária','Produtos customizados para idosos','Produtos customizados para jovens'],
        'objetivo_4': ['Aumento de Receitas','Lançar Novos Produto/Serviços','Aumentar Fatia de Mercado','Soluções Customizadas','Gerar inovação na empresa','Oferecer novos produtos','Regularização da empresa','Melhorar Governança e Compliance','Customização de Produtos e Serviços','Segmentação de Clientes','Atender Público por faixa etária','Produtos customizados para idosos','Produtos customizados para jovens'],
        'objetivo_5': ['Aumento de Receitas','Lançar Novos Produto/Serviços','Aumentar Fatia de Mercado','Soluções Customizadas','Gerar inovação na empresa','Oferecer novos produtos','Regularização da empresa','Melhorar Governança e Compliance','Customização de Produtos e Serviços','Segmentação de Clientes','Atender Público por faixa etária','Produtos customizados para idosos','Produtos customizados para jovens'],
        'ameaca_1': ['Necessidade de Investimentos','Aumento da Concorrencia','Aumento de Custos','Obsolecencia de Produtos/Serviços','Multas','Perda de Mercado','Perda de clientes','xyz','editar'],
        'ameaca_2': ['Necessidade de Investimentos','Aumento da Concorrencia','Aumento de Custos','Obsolecencia de Produtos/Serviços','Multas','Perda de Mercado','Perda de clientes','xyz','editar'],
        'ameaca_3': ['Necessidade de Investimentos','Aumento da Concorrencia','Aumento de Custos','Obsolecencia de Produtos/Serviços','Multas','Perda de Mercado','Perda de clientes','xyz','editar'],
        'ameaca_4': ['Necessidade de Investimentos','Aumento da Concorrencia','Aumento de Custos','Obsolecencia de Produtos/Serviços','Multas','Perda de Mercado','Perda de clientes','xyz','editar'],
        'ameaca_5': ['Necessidade de Investimentos','Aumento da Concorrencia','Aumento de Custos','Obsolecencia de Produtos/Serviços','Multas','Perda de Mercado','Perda de clientes','xyz','editar'],
    }

    dicio_retorno = {'clientes': clientes,
                     'opcoes_clientes': ['Eu Encanto', 'Eu Atendo', 'Eu Decepciono'],
                     'competitividade': competitividade, 'analise': analise,
                     'choices': choices
                    }
    return render(request, 'swot/swot_clientes.html', dicio_retorno)

@login_required
@csrf_exempt
@is_allowed
def salvar_clientes(request, user):
    if request.method == 'POST':
        try:
            owner = get_object_or_404(User, username=user)
            cliente = Cliente.objects.get(pk=int(request.POST['pk']),user=owner)
            cliente.preco = request.POST['preco']
            cliente.qualidade = request.POST['qualidade']
            cliente.entrega = request.POST['entrega']
            cliente.inovacao = request.POST['inovacao']
            cliente.portifolio = request.POST['portifolio']
            cliente.save()
        except:
            pass
    return HttpResponse('')

@login_required
@csrf_exempt
@is_allowed
def alterar_nome_concorrente(request, user):
    if request.method == 'POST':
        try:
            owner = get_object_or_404(User, username=user)
            concorrente = Concorrente.objects.get(pk=int(request.POST['pk']),user=owner)
            concorrente.concorrente = request.POST['concorrente']
            concorrente.save()
        except:
            pass
    return HttpResponse('')

@login_required
@csrf_exempt
@is_allowed
def alterar_nome_cliente(request, user):
    if request.method == 'POST':
        try:
            owner = get_object_or_404(User, username=user)
            cliente = Cliente.objects.get(pk=int(request.POST['pk']),user=owner)
            cliente.clientes = request.POST['cliente']
            cliente.save()
        except:
            pass
    return HttpResponse('')

@login_required
@csrf_exempt
@is_allowed
def alterar_nome_fornecedor(request, user):
    if request.method == 'POST':
        try:
            owner = get_object_or_404(User, username=user)
            fornecedor = Fornecedor.objects.get(pk=int(request.POST['pk']),user=owner)
            fornecedor.fornecedor = request.POST['fornecedor']
            fornecedor.save()
        except:
            pass
    return HttpResponse('')


@login_required
@csrf_exempt
@is_allowed
def salvar_analise_clientes(request, user):
    if request.method == 'POST':
        owner = get_object_or_404(User, username=user)
        analise = AnaliseClientes.objects.get(user=owner)
        analise.ameaca_1 = request.POST['ameaca_1']
        analise.ameaca_1_probabilidade = request.POST['ameaca_1_probabilidade']
        analise.ameaca_1_relevancia = request.POST['ameaca_1_relevancia']
        analise.ameaca_2 = request.POST['ameaca_2']
        analise.ameaca_2_probabilidade = request.POST['ameaca_2_probabilidade']
        analise.ameaca_2_relevancia = request.POST['ameaca_2_relevancia']
        analise.ameaca_3 = request.POST['ameaca_3']
        analise.ameaca_3_probabilidade = request.POST['ameaca_3_probabilidade']
        analise.ameaca_3_relevancia = request.POST['ameaca_3_relevancia']
        analise.ameaca_4 = request.POST['ameaca_4']
        analise.ameaca_4_probabilidade = request.POST['ameaca_4_probabilidade']
        analise.ameaca_4_relevancia = request.POST['ameaca_4_relevancia']
        analise.ameaca_5 = request.POST['ameaca_5']
        analise.ameaca_5_probabilidade = request.POST['ameaca_5_probabilidade']
        analise.ameaca_5_relevancia = request.POST['ameaca_5_relevancia']
        analise.objetivo_1 = request.POST['objetivo_1']
        analise.objetivo_1_atratividade = request.POST['objetivo_1_atratividade']
        analise.objetivo_1_probabilidade = request.POST['objetivo_1_probabilidade']
        analise.objetivo_2 = request.POST['objetivo_2']
        analise.objetivo_2_atratividade = request.POST['objetivo_2_atratividade']
        analise.objetivo_2_probabilidade = request.POST['objetivo_2_probabilidade']
        analise.objetivo_3 = request.POST['objetivo_3']
        analise.objetivo_3_atratividade = request.POST['objetivo_3_atratividade']
        analise.objetivo_3_probabilidade = request.POST['objetivo_3_probabilidade']
        analise.objetivo_4 = request.POST['objetivo_4']
        analise.objetivo_4_atratividade = request.POST['objetivo_4_atratividade']
        analise.objetivo_4_probabilidade = request.POST['objetivo_4_probabilidade']
        analise.objetivo_5 = request.POST['objetivo_5']
        analise.objetivo_5_atratividade = request.POST['objetivo_5_atratividade']
        analise.objetivo_5_probabilidade = request.POST['objetivo_5_probabilidade']
        analise.save()
    return HttpResponse('')

#FORNECEDORES#

def swot_fornecedores(request, user):
    owner = get_object_or_404(User, username=user)
    fornecedores = Fornecedor.objects.filter(user=owner)
    analise = AnaliseFornecedores.objects.get_or_create(user=owner)[0]

    competitividade = {'preco': 0, 'qualidade': 0, 'entrega': 0, 'inovacao': 0, 'portifolio': 0}
    for fornecedor in fornecedores:
        competitividade['preco'] += calcula_competitividade(fornecedor.preco)
        competitividade['qualidade'] += calcula_competitividade(fornecedor.qualidade)
        competitividade['entrega'] += calcula_competitividade(fornecedor.entrega)
        competitividade['inovacao'] += calcula_competitividade(fornecedor.inovacao)
        competitividade['portifolio'] += calcula_competitividade(fornecedor.portifolio)
    competitividade_media = 0.0
    for i in competitividade:
        try:
            competitividade[i] = (competitividade[i] / (len(fornecedores)*2))*100
            competitividade_media += competitividade[i]
        except:
            pass
    competitividade['media'] = competitividade_media / 5

    choices = {
        'objetivo_1': ['Aumento de Receitas','Lançar Novos Produto/Serviços','Aumentar Fatia de Mercado','Soluções Customizadas','Gerar inovação na empresa','Oferecer novos produtos','Regularização da empresa','Melhorar Governança e Compliance','Customização de Produtos e Serviços','Segmentação de Clientes','Atender Público por faixa etária','Produtos customizados para idosos','Produtos customizados para jovens'],
        'objetivo_2': ['Aumento de Receitas','Lançar Novos Produto/Serviços','Aumentar Fatia de Mercado','Soluções Customizadas','Gerar inovação na empresa','Oferecer novos produtos','Regularização da empresa','Melhorar Governança e Compliance','Customização de Produtos e Serviços','Segmentação de Clientes','Atender Público por faixa etária','Produtos customizados para idosos','Produtos customizados para jovens'],
        'objetivo_3': ['Aumento de Receitas','Lançar Novos Produto/Serviços','Aumentar Fatia de Mercado','Soluções Customizadas','Gerar inovação na empresa','Oferecer novos produtos','Regularização da empresa','Melhorar Governança e Compliance','Customização de Produtos e Serviços','Segmentação de Clientes','Atender Público por faixa etária','Produtos customizados para idosos','Produtos customizados para jovens'],
        'objetivo_4': ['Aumento de Receitas','Lançar Novos Produto/Serviços','Aumentar Fatia de Mercado','Soluções Customizadas','Gerar inovação na empresa','Oferecer novos produtos','Regularização da empresa','Melhorar Governança e Compliance','Customização de Produtos e Serviços','Segmentação de Clientes','Atender Público por faixa etária','Produtos customizados para idosos','Produtos customizados para jovens'],
        'objetivo_5': ['Aumento de Receitas','Lançar Novos Produto/Serviços','Aumentar Fatia de Mercado','Soluções Customizadas','Gerar inovação na empresa','Oferecer novos produtos','Regularização da empresa','Melhorar Governança e Compliance','Customização de Produtos e Serviços','Segmentação de Clientes','Atender Público por faixa etária','Produtos customizados para idosos','Produtos customizados para jovens'],
        'ameaca_1': ['Necessidade de Investimentos','Aumento da Concorrencia','Aumento de Custos','Obsolecencia de Produtos/Serviços','Multas','Perda de Mercado','Perda de clientes','xyz','editar'],
        'ameaca_2': ['Necessidade de Investimentos','Aumento da Concorrencia','Aumento de Custos','Obsolecencia de Produtos/Serviços','Multas','Perda de Mercado','Perda de clientes','xyz','editar'],
        'ameaca_3': ['Necessidade de Investimentos','Aumento da Concorrencia','Aumento de Custos','Obsolecencia de Produtos/Serviços','Multas','Perda de Mercado','Perda de clientes','xyz','editar'],
        'ameaca_4': ['Necessidade de Investimentos','Aumento da Concorrencia','Aumento de Custos','Obsolecencia de Produtos/Serviços','Multas','Perda de Mercado','Perda de clientes','xyz','editar'],
        'ameaca_5': ['Necessidade de Investimentos','Aumento da Concorrencia','Aumento de Custos','Obsolecencia de Produtos/Serviços','Multas','Perda de Mercado','Perda de clientes','xyz','editar'],
    }

    dicio_retorno = {'fornecedores': fornecedores,
                     'opcoes_fornecedores': ['Me Encanta', 'Me Atende', 'Me Decepciona'],
                     'competitividade': competitividade, 'analise': analise,
                     'choices': choices
                    }
    return render(request, 'swot/swot_fornecedores.html', dicio_retorno)

@login_required
@csrf_exempt
@is_allowed
def salvar_fornecedores(request, user):
    if request.method == 'POST':
        try:
            owner = get_object_or_404(User, username=user)
            fornecedor = Fornecedor.objects.get(pk=int(request.POST['pk']),user=owner)
            fornecedor.preco = request.POST['preco']
            fornecedor.qualidade = request.POST['qualidade']
            fornecedor.entrega = request.POST['entrega']
            fornecedor.inovacao = request.POST['inovacao']
            fornecedor.portifolio = request.POST['portifolio']
            fornecedor.save()
        except:
            pass
    return HttpResponse('')

@login_required
@csrf_exempt
@is_allowed
def salvar_analise_fornecedores(request, user):
    if request.method == 'POST':
        owner = get_object_or_404(User, username=user)
        analise = AnaliseFornecedores.objects.get(user=owner)
        analise.ameaca_1 = request.POST['ameaca_1']
        analise.ameaca_1_probabilidade = request.POST['ameaca_1_probabilidade']
        analise.ameaca_1_relevancia = request.POST['ameaca_1_relevancia']
        analise.ameaca_2 = request.POST['ameaca_2']
        analise.ameaca_2_probabilidade = request.POST['ameaca_2_probabilidade']
        analise.ameaca_2_relevancia = request.POST['ameaca_2_relevancia']
        analise.ameaca_3 = request.POST['ameaca_3']
        analise.ameaca_3_probabilidade = request.POST['ameaca_3_probabilidade']
        analise.ameaca_3_relevancia = request.POST['ameaca_3_relevancia']
        analise.ameaca_4 = request.POST['ameaca_4']
        analise.ameaca_4_probabilidade = request.POST['ameaca_4_probabilidade']
        analise.ameaca_4_relevancia = request.POST['ameaca_4_relevancia']
        analise.ameaca_5 = request.POST['ameaca_5']
        analise.ameaca_5_probabilidade = request.POST['ameaca_5_probabilidade']
        analise.ameaca_5_relevancia = request.POST['ameaca_5_relevancia']
        analise.objetivo_1 = request.POST['objetivo_1']
        analise.objetivo_1_atratividade = request.POST['objetivo_1_atratividade']
        analise.objetivo_1_probabilidade = request.POST['objetivo_1_probabilidade']
        analise.objetivo_2 = request.POST['objetivo_2']
        analise.objetivo_2_atratividade = request.POST['objetivo_2_atratividade']
        analise.objetivo_2_probabilidade = request.POST['objetivo_2_probabilidade']
        analise.objetivo_3 = request.POST['objetivo_3']
        analise.objetivo_3_atratividade = request.POST['objetivo_3_atratividade']
        analise.objetivo_3_probabilidade = request.POST['objetivo_3_probabilidade']
        analise.objetivo_4 = request.POST['objetivo_4']
        analise.objetivo_4_atratividade = request.POST['objetivo_4_atratividade']
        analise.objetivo_4_probabilidade = request.POST['objetivo_4_probabilidade']
        analise.objetivo_5 = request.POST['objetivo_5']
        analise.objetivo_5_atratividade = request.POST['objetivo_5_atratividade']
        analise.objetivo_5_probabilidade = request.POST['objetivo_5_probabilidade']
        analise.save()
    return HttpResponse('')

#MACRO#

def swot_macro(request, user):
    owner = get_object_or_404(User, username=user)
    macros = Macro.objects.filter(user=owner)
    analise = AnalisesMacro.objects.get_or_create(user=owner)[0]

    competitividade = {'preco': 0, 'qualidade': 0, 'entrega': 0, 'inovacao': 0, 'portifolio': 0}
    for macro in macros:
        competitividade['preco'] += calcula_competitividade(macro.preco)
        competitividade['qualidade'] += calcula_competitividade(macro.qualidade)
        competitividade['entrega'] += calcula_competitividade(macro.entrega)
        competitividade['inovacao'] += calcula_competitividade(macro.inovacao)
        competitividade['portifolio'] += calcula_competitividade(macro.portifolio)
    competitividade_media = 0.0
    for i in competitividade:
        try:
            competitividade[i] = (competitividade[i] / (len(macros)*2))*100
            competitividade_media += competitividade[i]
        except:
            pass
    competitividade['media'] = competitividade_media / 5

    choices = {
        'objetivo_1': ['Aumento de Receitas','Lançar Novos Produto/Serviços','Aumentar Fatia de Mercado','Soluções Customizadas','Gerar inovação na empresa','Oferecer novos produtos','Regularização da empresa','Melhorar Governança e Compliance','Customização de Produtos e Serviços','Segmentação de Clientes','Atender Público por faixa etária','Produtos customizados para idosos','Produtos customizados para jovens'],
        'objetivo_2': ['Aumento de Receitas','Lançar Novos Produto/Serviços','Aumentar Fatia de Mercado','Soluções Customizadas','Gerar inovação na empresa','Oferecer novos produtos','Regularização da empresa','Melhorar Governança e Compliance','Customização de Produtos e Serviços','Segmentação de Clientes','Atender Público por faixa etária','Produtos customizados para idosos','Produtos customizados para jovens'],
        'objetivo_3': ['Aumento de Receitas','Lançar Novos Produto/Serviços','Aumentar Fatia de Mercado','Soluções Customizadas','Gerar inovação na empresa','Oferecer novos produtos','Regularização da empresa','Melhorar Governança e Compliance','Customização de Produtos e Serviços','Segmentação de Clientes','Atender Público por faixa etária','Produtos customizados para idosos','Produtos customizados para jovens'],
        'objetivo_4': ['Aumento de Receitas','Lançar Novos Produto/Serviços','Aumentar Fatia de Mercado','Soluções Customizadas','Gerar inovação na empresa','Oferecer novos produtos','Regularização da empresa','Melhorar Governança e Compliance','Customização de Produtos e Serviços','Segmentação de Clientes','Atender Público por faixa etária','Produtos customizados para idosos','Produtos customizados para jovens'],
        'objetivo_5': ['Aumento de Receitas','Lançar Novos Produto/Serviços','Aumentar Fatia de Mercado','Soluções Customizadas','Gerar inovação na empresa','Oferecer novos produtos','Regularização da empresa','Melhorar Governança e Compliance','Customização de Produtos e Serviços','Segmentação de Clientes','Atender Público por faixa etária','Produtos customizados para idosos','Produtos customizados para jovens'],
        'ameaca_1': ['Necessidade de Investimentos','Aumento da Concorrencia','Aumento de Custos','Obsolecencia de Produtos/Serviços','Multas','Perda de Mercado','Perda de clientes','xyz','editar'],
        'ameaca_2': ['Necessidade de Investimentos','Aumento da Concorrencia','Aumento de Custos','Obsolecencia de Produtos/Serviços','Multas','Perda de Mercado','Perda de clientes','xyz','editar'],
        'ameaca_3': ['Necessidade de Investimentos','Aumento da Concorrencia','Aumento de Custos','Obsolecencia de Produtos/Serviços','Multas','Perda de Mercado','Perda de clientes','xyz','editar'],
        'ameaca_4': ['Necessidade de Investimentos','Aumento da Concorrencia','Aumento de Custos','Obsolecencia de Produtos/Serviços','Multas','Perda de Mercado','Perda de clientes','xyz','editar'],
        'ameaca_5': ['Necessidade de Investimentos','Aumento da Concorrencia','Aumento de Custos','Obsolecencia de Produtos/Serviços','Multas','Perda de Mercado','Perda de clientes','xyz','editar'],
    }

    dicio_retorno = {'macros':macros,

                     'competitividade': competitividade, 'analise': analise,
                     'choices': choices
                    }
    return render(request, 'swot/swot_macro.html', dicio_retorno)

@login_required
@csrf_exempt
@is_allowed
def salvar_macro(request, user):
    if request.method == 'POST':
        try:
            owner = get_object_or_404(User, username=user)
            macro = Macro.objects.get(pk=int(request.POST['pk']),user=owner)
            macro.preco = request.POST['preco']
            macro.qualidade = request.POST['qualidade']
            macro.entrega = request.POST['entrega']
            macro.inovacao = request.POST['inovacao']
            macro.portifolio = request.POST['portifolio']
            macro.save()
        except:
            pass
    return HttpResponse('')

@login_required
@csrf_exempt
@is_allowed
def salvar_analise_macro(request, user):
    if request.method == 'POST':
        owner = get_object_or_404(User, username=user)
        analise = AnalisesMacro.objects.get(user=owner)
        analise.ameaca_1 = request.POST['ameaca_1']
        analise.ameaca_1_probabilidade = request.POST['ameaca_1_probabilidade']
        analise.ameaca_1_relevancia = request.POST['ameaca_1_relevancia']
        analise.ameaca_2 = request.POST['ameaca_2']
        analise.ameaca_2_probabilidade = request.POST['ameaca_2_probabilidade']
        analise.ameaca_2_relevancia = request.POST['ameaca_2_relevancia']
        analise.ameaca_3 = request.POST['ameaca_3']
        analise.ameaca_3_probabilidade = request.POST['ameaca_3_probabilidade']
        analise.ameaca_3_relevancia = request.POST['ameaca_3_relevancia']
        analise.ameaca_4 = request.POST['ameaca_4']
        analise.ameaca_4_probabilidade = request.POST['ameaca_4_probabilidade']
        analise.ameaca_4_relevancia = request.POST['ameaca_4_relevancia']
        analise.ameaca_5 = request.POST['ameaca_5']
        analise.ameaca_5_probabilidade = request.POST['ameaca_5_probabilidade']
        analise.ameaca_5_relevancia = request.POST['ameaca_5_relevancia']
        analise.objetivo_1 = request.POST['objetivo_1']
        analise.objetivo_1_atratividade = request.POST['objetivo_1_atratividade']
        analise.objetivo_1_probabilidade = request.POST['objetivo_1_probabilidade']
        analise.objetivo_2 = request.POST['objetivo_2']
        analise.objetivo_2_atratividade = request.POST['objetivo_2_atratividade']
        analise.objetivo_2_probabilidade = request.POST['objetivo_2_probabilidade']
        analise.objetivo_3 = request.POST['objetivo_3']
        analise.objetivo_3_atratividade = request.POST['objetivo_3_atratividade']
        analise.objetivo_3_probabilidade = request.POST['objetivo_3_probabilidade']
        analise.objetivo_4 = request.POST['objetivo_4']
        analise.objetivo_4_atratividade = request.POST['objetivo_4_atratividade']
        analise.objetivo_4_probabilidade = request.POST['objetivo_4_probabilidade']
        analise.objetivo_5 = request.POST['objetivo_5']
        analise.objetivo_5_atratividade = request.POST['objetivo_5_atratividade']
        analise.objetivo_5_probabilidade = request.POST['objetivo_5_probabilidade']
        analise.save()
    return HttpResponse('')
