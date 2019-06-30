from django.shortcuts import render, get_object_or_404
from accounts.decorators import is_allowed
from django.contrib.auth.models import User
#from pessoas.models import Pessoas
#from pessoa.models import Pessoas, AvaliacaoPessoas
from django.contrib.auth.decorators import login_required
#from .utils import select_smile, calcula_campos_dinamicos
from django.views.decorators.csrf import csrf_exempt
from .models import *
from django.http import HttpResponse



@login_required
@is_allowed
def analise_desempenho_pessoas(request,user):
    owner = get_object_or_404 ( User, username=user )
    pessoas_objects = Pessoas.objects.filter(user=owner).all().order_by('-ano_exercicio')[:1]

    # Campos que serão exibidos
    pessoas_list = {
        # Campos estáticos
        'ano_exercicio': [],
        'funcionarios_antigos': [],
        'rotatividade': [],
        'absenteismo': [],
    }
    for pessoas in pessoas_objects:
        # Campos estáticos
        pessoas_list['ano_exercicio'].append(pessoas.ano_exercicio)
        vObj = Pessoas.objects.get(user=owner,ano_exercicio=pessoas.ano_exercicio)
        pessoas_list['funcionarios_antigos'].append(pessoas.funcionarios_antigos)
        pessoas_list['rotatividade'].append(pessoas.rotatividade)
        pessoas_list['absenteismo'].append(pessoas.absenteismo)


    anos = pessoas_list['ano_exercicio']
    for key in pessoas_list:
        pessoas_list[key] = zip (pessoas_list[key], anos)
    pessoas_list['id'] = anos

    v = 'e'

    try:
        avaliacao = AvaliacaoPessoas.objects.get(pessoas=vObj)
    except AvaliacaoPessoas.DoesNotExist:
        avaliacao = AvaliacaoPessoas(pessoas=vObj)
        avaliacao.save()
        v = 'e'
    return render(request, 'analise_desempenho_pessoas.html',{
        'pessoas': pessoas_list,
        'avaliacao': avaliacao,
        'v': v,
    })


@login_required
@is_allowed
@csrf_exempt
def salvar_objetivo_de_pessoas(request, user):
    if request.method == 'POST':
        owner = get_object_or_404(User, username=user)
        pessoas = Pessoas.objects.get ( user=owner, ano_exercicio=request.POST['ano'] )
        avaliacao = AvaliacaoPessoas.objects.get ( pessoas=pessoas )
        str = "avaliacao." + request.POST['key'] + " = '" + request.POST['v'] + "'"
        exec ( str )
        avaliacao.save ()
    return HttpResponse ()


@login_required
@is_allowed
def painel_desempenho_pessoas(request,user):
    owner = get_object_or_404 ( User, username=user )
    pessoas_objects: object = Pessoas.objects.filter ( user=owner ).all ().order_by ( '-ano_exercicio' )[:4]

    # Campos que serão exibidos
    pessoas_list = {
        # Campos estáticos
        'ano_exercicio': [],
        'funcionarios_antigos': [],
        'rotatividade': [],
        'absenteismo': [],

    }
    for pessoas in pessoas_objects:
        # Campos estáticos
        pessoas_list['ano_exercicio'].append ( pessoas.ano_exercicio )
        vObj = Pessoas.objects.get ( user=owner, ano_exercicio=pessoas.ano_exercicio )
        pessoas_list['funcionarios_antigos'].append ( pessoas.funcionarios_antigos )
        pessoas_list['rotatividade'].append ( pessoas.rotatividade )
        pessoas_list['absenteismo'].append ( pessoas.absenteismo )

        #vendas.taxa_conversao_proposta = vendas.propostas_aprovadas_no_ano/vendas.propostas_enviadas_no_ano
        #vendas_list['taxa_conversao_proposta'].append(taxa_conversao_proposta)

        #vendas.ticket_medio = dre.receita_bruta / vendas.notas_fiscais_emitidas
        #vendas.clientes_fidelizados_ano = vendas.clientes_fidelizados / vendas.carteira_de_clientes_ativa
        #vendas.reclamacoes_nf = vendas.reclamacoes_clientes / vendas.notas_fiscais_emitidas
        # dre.despesas_operacionais = dre.despesas_administrativas + dre.despesas_com_pessoal + dre.despesas_ocupacao + dre.despesas_logistica + dre.despesas_vendas + dre.despesas_viagens + dre.despesas_servicos_pj + dre.despesas_tributarias + dre.depreciacao_amortizacao

    anos = pessoas_list['ano_exercicio']
    for key in pessoas_list:
        pessoas_list[key] = zip ( pessoas_list[key], anos )
    pessoas_list['id'] = anos



    return render(request,'painel_desempenho_pessoas.html',{'pessoas': pessoas_list})

@login_required
@is_allowed
def multi_pessoas(request, user):
    owner = get_object_or_404 ( User, username=user )
    competencias = Competencias.objects.filter ( user=owner )

    competencia = {'categoria': 0}
    for competencias in competencia:
        competencia['categoria'] = competencia
    competencia_media = 0.0
    for i in competencia:
        try:
            competencia[i] = (competencia[i] / (len (competencias) * 1)) * 100
            competencia_media += competencia[i]
        except:
            pass
    competencia['media'] = competencia_media

    return render(request,'multi_pessoas.html')


@login_required
@is_allowed
def dashboard_pessoas(request,user):

    return render(request,'dashboard_pessoas.html')

@login_required
@is_allowed
def competencia(request,user):
    owner = get_object_or_404 ( User, username=user )
    pessoas_objects = Pessoas.objects.filter ( user=owner ).all ().order_by ( '-ano_exercicio' )[:1]

    # Campos que serão exibidos
    pessoas_list = {
        # Campos estáticos
        'ano_exercicio': [],
        'funcionarios_antigos': [],
        'rotatividade': [],
        'absenteismo': [],
    }
    for pessoas in pessoas_objects:
        # Campos estáticos
        pessoas_list['ano_exercicio'].append ( pessoas.ano_exercicio )
        # vObj = Pessoas.objects.get(user=owner,ano_exercicio=pessoas.ano_exercicio)
        pessoas_list['funcionarios_antigos'].append ( pessoas.funcionarios_antigos )
        pessoas_list['rotatividade'].append ( pessoas.rotatividade )
        pessoas_list['absenteismo'].append ( pessoas.absenteismo )

    anos = pessoas_list['ano_exercicio']
    for key in pessoas_list:
        pessoas_list[key] = zip ( pessoas_list[key], anos )
    pessoas_list['id'] = anos

    v = 'e'

    try:
        avaliacao = AvaliacaoPessoas.objects.get
    except AvaliacaoPessoas.DoesNotExist:
        avaliacao = AvaliacaoPessoas
        avaliacao.save ()
        v = 'e'
    return render ( request, 'objetivos/competencia.html', {
        'pessoas': pessoas_list,
        'avaliacao': avaliacao,
        'v': v,
    } )


@login_required
@is_allowed
def engajamento(request,user):
    owner = get_object_or_404 ( User, username=user )
    pessoas_objects = Pessoas.objects.filter ( user=owner ).all ().order_by ( '-ano_exercicio' )[:1]

    # Campos que serão exibidos
    pessoas_list = {
        # Campos estáticos
        'ano_exercicio': [],
        'funcionarios_antigos': [],
        'rotatividade': [],
        'absenteismo': [],
    }
    for pessoas in pessoas_objects:
        # Campos estáticos
        pessoas_list['ano_exercicio'].append ( pessoas.ano_exercicio )
        # vObj = Pessoas.objects.get(user=owner,ano_exercicio=pessoas.ano_exercicio)
        pessoas_list['funcionarios_antigos'].append ( pessoas.funcionarios_antigos )
        pessoas_list['rotatividade'].append ( pessoas.rotatividade )
        pessoas_list['absenteismo'].append ( pessoas.absenteismo )

    anos = pessoas_list['ano_exercicio']
    for key in pessoas_list:
        pessoas_list[key] = zip ( pessoas_list[key], anos )
    pessoas_list['id'] = anos

    v = 'e'

    try:
        avaliacao = AvaliacaoPessoas.objects.get
    except AvaliacaoPessoas.DoesNotExist:
        avaliacao = AvaliacaoPessoas
        avaliacao.save ()
        v = 'e'
    return render ( request, 'objetivos/engajamento.html', {
        'pessoas': pessoas_list,
        'avaliacao': avaliacao,
        'v': v,
    } )


@login_required
@is_allowed
def retencao(request,user):
    owner = get_object_or_404 ( User, username=user )
    pessoas_objects = Pessoas.objects.filter ( user=owner ).all ().order_by ( '-ano_exercicio' )[:1]

    # Campos que serão exibidos
    pessoas_list = {
        # Campos estáticos
        'ano_exercicio': [],
        'funcionarios_antigos': [],
        'rotatividade': [],
        'absenteismo': [],
    }
    for pessoas in pessoas_objects:
        # Campos estáticos
        pessoas_list['ano_exercicio'].append ( pessoas.ano_exercicio )
        # vObj = Pessoas.objects.get(user=owner,ano_exercicio=pessoas.ano_exercicio)
        pessoas_list['funcionarios_antigos'].append ( pessoas.funcionarios_antigos )
        pessoas_list['rotatividade'].append ( pessoas.rotatividade )
        pessoas_list['absenteismo'].append ( pessoas.absenteismo )

    anos = pessoas_list['ano_exercicio']
    for key in pessoas_list:
        pessoas_list[key] = zip ( pessoas_list[key], anos )
    pessoas_list['id'] = anos

    v = 'e'

    try:
        avaliacao = AvaliacaoPessoas.objects.get
    except AvaliacaoPessoas.DoesNotExist:
        avaliacao = AvaliacaoPessoas
        avaliacao.save ()
        v = 'e'
    return render ( request, 'objetivos/retencao.html', {
        'pessoas': pessoas_list,
        'avaliacao': avaliacao,
        'v': v,
    } )
