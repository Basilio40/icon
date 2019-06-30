from django.shortcuts import render, get_object_or_404
from accounts.decorators import is_allowed
from django.contrib.auth.models import User
#from vendas.models import Vendas
from vendas.models import Vendas, AvaliacaoVendas
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .models import *
from .utils import select_smile, calcula_campos_dinamicos
#from django.views.decorators.csrf import csrf_exempt
from .models import *
from django.http import HttpResponse
from swot.utils import calcula_competitividade



@login_required
@is_allowed
def definir_objetivo_de_vendas(request,user):
    owner = get_object_or_404 ( User, username=user )
    vendas_objects = Vendas.objects.filter(user=owner).all().order_by('-ano_exercicio')[:1]

    # Campos que serão exibidos
    vendas_list = {
        # Campos estáticos
        'ano_exercicio': [],
        'carteira_de_clientes_ativa': [],
        'novos_clientes_no_ano': [],
        'propostas_enviadas_no_ano': [],
        'propostas_aprovadas_no_ano': [],
        'notas_fiscais_emitidas': [],
        'clientes_fidelizados': [],
        'reclamacoes_clientes': [],
        'clientes_perdidos': [],

    }
    for vendas in vendas_objects:
        # Campos estáticos
        vendas_list['ano_exercicio'].append ( vendas.ano_exercicio )
        vObj = Vendas.objects.get(user=owner,ano_exercicio=vendas.ano_exercicio)
        vendas_list['carteira_de_clientes_ativa'].append ( vendas.carteira_de_clientes_ativa )
        vendas_list['novos_clientes_no_ano'].append ( vendas.novos_clientes_no_ano )
        vendas_list['propostas_enviadas_no_ano'].append ( vendas.propostas_enviadas_no_ano )
        vendas_list['propostas_aprovadas_no_ano'].append ( vendas.propostas_aprovadas_no_ano )
        vendas_list['notas_fiscais_emitidas'].append ( vendas.notas_fiscais_emitidas )
        vendas_list['clientes_fidelizados'].append ( vendas.clientes_fidelizados )
        vendas_list['reclamacoes_clientes'].append ( vendas.reclamacoes_clientes )
        vendas_list['clientes_perdidos'].append ( vendas.clientes_perdidos )

    anos = vendas_list['ano_exercicio']
    for key in vendas_list:
        vendas_list[key] = zip ( vendas_list[key], anos )
    vendas_list['id'] = anos

    v = 'e'

    try:
        avaliacao = AvaliacaoVendas.objects.get(vendas=vObj)
    except AvaliacaoVendas.DoesNotExist:
        avaliacao = AvaliacaoVendas(vendas=vObj)
        avaliacao.save()
        v = 'ne'
    return render(request,'analise_desempenho_vendas.html',{
        'vendas': vendas_list,
        'avaliacao': avaliacao,
        'v': v,
    })

@login_required
@csrf_exempt
@is_allowed
def salvar_objetivo_de_vendas(request,user):
    if request.method == 'POST':
        owner = get_object_or_404 ( User, username=user )
        vendas = Vendas.objects.get(user=owner, ano_exercicio=request.POST['ano'])
        avaliacao = AvaliacaoVendas.objects.get(vendas=vendas)
        str = "avaliacao." + request.POST['key'] + " = '" + request.POST['v'] + "'"
        exec(str)
        avaliacao.save()
    return HttpResponse()

@login_required
@is_allowed
def painel_desempenho_vendas(request,user):
    owner = get_object_or_404 ( User, username=user )
    vendas_objects: object = Vendas.objects.filter ( user=owner ).all ().order_by ( '-ano_exercicio' )[:4]

    # Campos que serão exibidos
    vendas_list = {
        # Campos estáticos
        'ano_exercicio':[],
        'carteira_de_clientes_ativa':[],
        'novos_clientes_no_ano':[],
        'propostas_enviadas_no_ano':[],
        'notas_fiscais_emitidas':[],
        'clientes_fidelizados':[],
        'reclamacoes_clientes':[],
        'clientes_perdidos':[],

    }
    for vendas in vendas_objects:
        # Campos estáticos
        vendas_list['ano_exercicio'].append ( vendas.ano_exercicio )
        vendas_list['carteira_de_clientes_ativa'].append ( vendas.carteira_de_clientes_ativa )
        vendas_list['novos_clientes_no_ano'].append ( vendas.novos_clientes_no_ano )
        vendas_list['propostas_enviadas_no_ano'].append ( vendas.propostas_enviadas_no_ano )
        vendas_list['notas_fiscais_emitidas'].append ( vendas.notas_fiscais_emitidas )
        vendas_list['clientes_fidelizados'].append ( vendas.clientes_fidelizados )
        vendas_list['reclamacoes_clientes'].append(vendas.reclamacoes_clientes)
        vendas_list['clientes_perdidos'].append(vendas.clientes_perdidos)

        #vendas.taxa_conversao_proposta = vendas.propostas_aprovadas_no_ano/vendas.propostas_enviadas_no_ano
        #vendas_list['taxa_conversao_proposta'].append(taxa_conversao_proposta)

        #vendas.ticket_medio = dre.receita_bruta / vendas.notas_fiscais_emitidas
        #vendas.clientes_fidelizados_ano = vendas.clientes_fidelizados / vendas.carteira_de_clientes_ativa
        #vendas.reclamacoes_nf = vendas.reclamacoes_clientes / vendas.notas_fiscais_emitidas
        # dre.despesas_operacionais = dre.despesas_administrativas + dre.despesas_com_pessoal + dre.despesas_ocupacao + dre.despesas_logistica + dre.despesas_vendas + dre.despesas_viagens + dre.despesas_servicos_pj + dre.despesas_tributarias + dre.depreciacao_amortizacao

    anos = vendas_list['ano_exercicio']
    for key in vendas_list:
        vendas_list[key] = zip ( vendas_list[key], anos )
    vendas_list['id'] = anos




    return render(request,'painel_desempenho_vendas.html',{'vendas': vendas_list})

def detail_vendas(request, user, ano):
    """
        View que retorna apenas 1 DRE, com base no ano, para exibição.
    """
    owner = get_object_or_404(User, username=user)
    vendas = get_object_or_404(Vendas, user=owner, ano_exercicio=ano)
    # Campos dinâmicos
    #vendas.taxa_conversao_proposta = vendas.propostas_aprovadas_no_ano / vendas.
    #vendas_list['taxa_conversao_proposta'].append ( taxa_conversao_proposta )
    #vendas.ticket_medio = dre.receita_bruta /vendas.notas_fiscais_emitidas
    #vendas.clientes_fidelizados_ano = vendas.clientes_fidelizados / vendas.carteira_de_clientes_ativa
    #vendas.reclamacoes_nf = vendas.reclamacoes_clientes / vendas.notas_fiscais_emitidas
    #dre.despesas_operacionais = dre.despesas_administrativas + dre.despesas_com_pessoal + dre.despesas_ocupacao + dre.despesas_logistica + dre.despesas_vendas + dre.despesas_viagens + dre.despesas_servicos_pj + dre.despesas_tributarias + dre.depreciacao_amortizacao


    return render(request, 'vendas/detail_vendas.html', {'vendas': vendas})

    # Campos para exibição
    campos_dinamicos =  calcula_campos_dinamicos(vendas)
    taxa_conversao_proposta = campos_dinamicos['taxa_conversao_proposta']
    ticket_medio = campos_dinamicos['ticket_medio']
    clientes_fidelizados_ano = campos_dinamicos['clientes_fidelizados_ano']
    reclamacoes_nf = campos_dinamicos['reclamacoes_nf']

    count = 1
    for i in range(1,4):
        try:
            novo_vendas = Vendas.objects.get(ano_exercicio=vendas.ano_exercicio-i)
            novos_campos_dinamicos = calcula_campos_dinamicos(novo_vendas)
            #count += 1
        except:
            pass
        #
    try:
        novo_vendas = Vendas.objects.get(ano_exercicio=vendas.ano_exercicio-1)
        rentabilidade_ano_passado = calcula_campos_dinamicos(novo_vendas)['reclamacoes_nf']
    except:
        rentabilidade_ano_passado = 0.0
    try:
        vendas_passado = Vendas.objects.get(user=owner, ano_exercicio=vendas.ano_exercicio-3)

    except Exception as e:
        reclamacoes_nf = 0.0

    return render(request, 'vendas/detail_vendas.html', {'vendas': vendas})

@login_required
@is_allowed
def dashboard_vendas(request,user):

    return render(request,'dashboard_vendas.html')


@ login_required
@ is_allowed
def mkt_relacionamento(request, user):
    owner = get_object_or_404 ( User, username=user )
    vendas_objects = Vendas.objects.filter ( user=owner ).all ().order_by ( '-ano_exercicio' )[:1]

    # Campos que serão exibidos
    vendas_list = {
        # Campos estáticos
        'ano_exercicio': [],
        'carteira_de_clientes_ativa': [],
        'novos_clientes_no_ano': [],
        'propostas_enviadas_no_ano': [],
        'propostas_aprovadas_no_ano': [],
        'notas_fiscais_emitidas': [],
        'clientes_fidelizados': [],
        'reclamacoes_clientes': [],
        'clientes_perdidos': [],

    }
    for vendas in vendas_objects:
        # Campos estáticos
        vendas_list['ano_exercicio'].append ( vendas.ano_exercicio )
        vObj = Vendas.objects.get ( user=owner, ano_exercicio=vendas.ano_exercicio )
        vendas_list['carteira_de_clientes_ativa'].append ( vendas.carteira_de_clientes_ativa )
        vendas_list['novos_clientes_no_ano'].append ( vendas.novos_clientes_no_ano )
        vendas_list['propostas_enviadas_no_ano'].append ( vendas.propostas_enviadas_no_ano )
        vendas_list['propostas_aprovadas_no_ano'].append ( vendas.propostas_aprovadas_no_ano )
        vendas_list['notas_fiscais_emitidas'].append ( vendas.notas_fiscais_emitidas )
        vendas_list['clientes_fidelizados'].append ( vendas.clientes_fidelizados )
        vendas_list['reclamacoes_clientes'].append ( vendas.reclamacoes_clientes )
        vendas_list['clientes_perdidos'].append ( vendas.clientes_perdidos )

    anos = vendas_list['ano_exercicio']
    for key in vendas_list:
        vendas_list[key] = zip ( vendas_list[key], anos )
    vendas_list['id'] = anos

    v = 'e'

    try:
        avaliacao = AvaliacaoVendas.objects.get ( vendas=vObj )
    except AvaliacaoVendas.DoesNotExist:
        avaliacao = AvaliacaoVendas ( vendas=vObj )
        avaliacao.save ()
        v = 'ne'
    return render ( request, 'objetivos/mkt_relacionamento.html',{
        'vendas': vendas_list,
        'avaliacao': avaliacao,
        'v': v,
    } )



@ login_required
@ is_allowed
def metas_vendas(request, user):
    owner = get_object_or_404 ( User, username=user )
    vendas_objects = Vendas.objects.filter ( user=owner ).all ().order_by ( '-ano_exercicio' )[:1]

    # Campos que serão exibidos
    vendas_list = {
        # Campos estáticos
        'ano_exercicio': [],
        'carteira_de_clientes_ativa': [],
        'novos_clientes_no_ano': [],
        'propostas_enviadas_no_ano': [],
        'propostas_aprovadas_no_ano': [],
        'notas_fiscais_emitidas': [],
        'clientes_fidelizados': [],
        'reclamacoes_clientes': [],
        'clientes_perdidos': [],

    }
    for vendas in vendas_objects:
        # Campos estáticos
        vendas_list['ano_exercicio'].append ( vendas.ano_exercicio )
        vObj = Vendas.objects.get ( user=owner, ano_exercicio=vendas.ano_exercicio )
        vendas_list['carteira_de_clientes_ativa'].append ( vendas.carteira_de_clientes_ativa )
        vendas_list['novos_clientes_no_ano'].append ( vendas.novos_clientes_no_ano )
        vendas_list['propostas_enviadas_no_ano'].append ( vendas.propostas_enviadas_no_ano )
        vendas_list['propostas_aprovadas_no_ano'].append ( vendas.propostas_aprovadas_no_ano )
        vendas_list['notas_fiscais_emitidas'].append ( vendas.notas_fiscais_emitidas )
        vendas_list['clientes_fidelizados'].append ( vendas.clientes_fidelizados )
        vendas_list['reclamacoes_clientes'].append ( vendas.reclamacoes_clientes )
        vendas_list['clientes_perdidos'].append ( vendas.clientes_perdidos )

    anos = vendas_list['ano_exercicio']
    for key in vendas_list:
        vendas_list[key] = zip ( vendas_list[key], anos )
    vendas_list['id'] = anos

    v = 'e'

    try:
        avaliacao = AvaliacaoVendas.objects.get ( vendas=vObj )
    except AvaliacaoVendas.DoesNotExist:
        avaliacao = AvaliacaoVendas ( vendas=vObj )
        avaliacao.save ()
        v = 'ne'
    return render ( request, 'objetivos/metas_vendas.html', {
        'vendas': vendas_list,
        'avaliacao': avaliacao,
        'v': v,
    } )


@ login_required
@ is_allowed
def satisfacao_clientes(request, user):
    owner = get_object_or_404 ( User, username=user )
    vendas_objects = Vendas.objects.filter ( user=owner ).all ().order_by ( '-ano_exercicio' )[:1]

    # Campos que serão exibidos
    vendas_list = {
        # Campos estáticos
        'ano_exercicio': [],
        'carteira_de_clientes_ativa': [],
        'novos_clientes_no_ano': [],
        'propostas_enviadas_no_ano': [],
        'propostas_aprovadas_no_ano': [],
        'notas_fiscais_emitidas': [],
        'clientes_fidelizados': [],
        'reclamacoes_clientes': [],
        'clientes_perdidos': [],

    }
    for vendas in vendas_objects:
        # Campos estáticos
        vendas_list['ano_exercicio'].append ( vendas.ano_exercicio )
        vObj = Vendas.objects.get ( user=owner, ano_exercicio=vendas.ano_exercicio )
        vendas_list['carteira_de_clientes_ativa'].append ( vendas.carteira_de_clientes_ativa )
        vendas_list['novos_clientes_no_ano'].append ( vendas.novos_clientes_no_ano )
        vendas_list['propostas_enviadas_no_ano'].append ( vendas.propostas_enviadas_no_ano )
        vendas_list['propostas_aprovadas_no_ano'].append ( vendas.propostas_aprovadas_no_ano )
        vendas_list['notas_fiscais_emitidas'].append ( vendas.notas_fiscais_emitidas )
        vendas_list['clientes_fidelizados'].append ( vendas.clientes_fidelizados )
        vendas_list['reclamacoes_clientes'].append ( vendas.reclamacoes_clientes )
        vendas_list['clientes_perdidos'].append ( vendas.clientes_perdidos )

    anos = vendas_list['ano_exercicio']
    for key in vendas_list:
        vendas_list[key] = zip ( vendas_list[key], anos )
    vendas_list['id'] = anos

    v = 'e'

    try:
        avaliacao = AvaliacaoVendas.objects.get ( vendas=vObj )
    except AvaliacaoVendas.DoesNotExist:
        avaliacao = AvaliacaoVendas ( vendas=vObj )
        avaliacao.save ()
        v = 'ne'
    return render ( request, 'objetivos/satisfacao_clientes.html', {
        'vendas': vendas_list,
        'avaliacao': avaliacao,
        'v': v,
    } )
