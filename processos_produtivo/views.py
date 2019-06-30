from django.shortcuts import render, get_object_or_404
from accounts.decorators import is_allowed
from django.contrib.auth.models import User
#from processos.models import Processos
from processos_produtivo.models import Processos, AvaliacaoProcessos
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .models import *
from .utils import select_smile, calcula_campos_dinamicos
from django.views.decorators.csrf import csrf_exempt
from .models import *
from django.http import HttpResponse



@login_required
@is_allowed
def analise_desemp_processos_produtivos(request,user):
    owner = get_object_or_404 ( User, username=user )
    processos_objects = Processos.objects.filter ( user=owner ).all ().order_by ( '-ano_exercicio' )[:1]

    # Campos que serão exibidos
    processos_list = {
        # Campos estáticos
        'ano_exercicio': [],
        'funcionarios': [],
        'volume_produzido_no_ano': [],
        'capacidade_produzida': [],
        'refugo_retrabalho': [],
        'custos_garantia': [],
        'entregas_no_prazo': [],
        'valor_do_estoque': [],
    }
    for processos in processos_objects:
        # Campos estáticos
        processos_list['ano_exercicio'].append ( processos.ano_exercicio )
        vObj = Processos.objects.get ( user=owner, ano_exercicio=processos.ano_exercicio )
        processos_list['funcionarios'].append ( processos.funcionarios )
        processos_list['volume_produzido_no_ano'].append ( processos.volume_produzido_no_ano )
        processos_list['capacidade_produzida'].append ( processos.capacidade_produzida )
        processos_list['refugo_retrabalho'].append ( processos.refugo_retrabalho )
        processos_list['custos_garantia'].append ( processos.custos_garantia )
        processos_list['entregas_no_prazo'].append ( processos.entregas_no_prazo )
        processos_list['valor_do_estoque'].append ( processos.valor_do_estoque )

    anos = processos_list['ano_exercicio']
    for key in processos_list:
        processos_list[key] = zip ( processos_list[key], anos )
    processos_list['id'] = anos

    v = 'e'

    try:
        avaliacao = AvaliacaoProcessos.objects.get ( processos=vObj )
    except AvaliacaoProcessos.DoesNotExist:
        avaliacao = AvaliacaoProcessos ( processos=vObj )
        avaliacao.save ()
        v = 'ne'
    return render ( request, 'analise_desemp_processos_produtivos.html',{
        'processos': processos_list,
        'avaliacao': avaliacao,
        'v': v,
    } )


@login_required
@csrf_exempt
@is_allowed
def salvar_objetivo_de_processos(request, user):
    if request.method == 'POST':
        owner = get_object_or_404 ( User, username=user )
        processos = Processos.objects.get ( user=owner, ano_exercicio=request.POST['ano'] )
        avaliacao = AvaliacaoProcessos.objects.get ( processos=processos )
        str = "avaliacao." + request.POST['key'] + " = '" + request.POST['v'] + "'"
        exec ( str )
        avaliacao.save ()
    return HttpResponse ()


@login_required
@is_allowed
def painel_desempenho_processos_produtivos(request,user):
    owner = get_object_or_404 ( User, username=user )
    processos_objects: object = Processos.objects.filter ( user=owner ).all ().order_by ( '-ano_exercicio' )[:4]

    # Campos que serão exibidos
    processos_list = {
        # Campos estáticos
        'ano_exercicio': [],
        'funcionarios': [],
        'volume_produzido_no_ano': [],
        'capacidade_produzida': [],
        'refugo_retrabalho': [],
        'custos_garantia': [],
        'entregas_no_prazo': [],
        'valor_do_estoque': [],

    }
    for processos in processos_objects:
        # Campos estáticos
        processos_list['ano_exercicio'].append ( processos.ano_exercicio )
        vObj = Processos.objects.get ( user=owner, ano_exercicio=processos.ano_exercicio )
        processos_list['funcionarios'].append ( processos.funcionarios )
        processos_list['volume_produzido_no_ano'].append ( processos.volume_produzido_no_ano )
        processos_list['capacidade_produzida'].append ( processos.capacidade_produzida )
        processos_list['refugo_retrabalho'].append ( processos.refugo_retrabalho )
        processos_list['custos_garantia'].append ( processos.custos_garantia )
        processos_list['entregas_no_prazo'].append ( processos.entregas_no_prazo )
        processos_list['valor_do_estoque'].append ( processos.valor_do_estoque )

        #vendas.taxa_conversao_proposta = vendas.propostas_aprovadas_no_ano/vendas.propostas_enviadas_no_ano
        #vendas_list['taxa_conversao_proposta'].append(taxa_conversao_proposta)

        #vendas.ticket_medio = dre.receita_bruta / vendas.notas_fiscais_emitidas
        #vendas.clientes_fidelizados_ano = vendas.clientes_fidelizados / vendas.carteira_de_clientes_ativa
        #vendas.reclamacoes_nf = vendas.reclamacoes_clientes / vendas.notas_fiscais_emitidas
        # dre.despesas_operacionais = dre.despesas_administrativas + dre.despesas_com_pessoal + dre.despesas_ocupacao + dre.despesas_logistica + dre.despesas_vendas + dre.despesas_viagens + dre.despesas_servicos_pj + dre.despesas_tributarias + dre.depreciacao_amortizacao

    anos = processos_list['ano_exercicio']
    for key in processos_list:
        processos_list[key] = zip ( processos_list[key], anos )
    processos_list['id'] = anos


    return render(request,'painel_desempenho_processos_produtivos.html',{'processos': processos_list})

@login_required
@is_allowed
def dashboard_processos(request,user):

    return render(request,'dashboard_processos.html')

@login_required
@is_allowed
def produtividade(request,user):
    owner = get_object_or_404 ( User, username=user )
    processos_objects = Processos.objects.filter ( user=owner ).all ().order_by ( '-ano_exercicio' )[:1]

    # Campos que serão exibidos
    processos_list = {
        # Campos estáticos
        'ano_exercicio': [],
        'funcionarios': [],
        'volume_produzido_no_ano': [],
        'capacidade_produzida': [],
        'refugo_retrabalho': [],
        'custos_garantia': [],
        'entregas_no_prazo': [],
        'valor_do_estoque': [],
    }
    for processos in processos_objects:
        # Campos estáticos
        processos_list['ano_exercicio'].append ( processos.ano_exercicio )
        vObj = Processos.objects.get ( user=owner, ano_exercicio=processos.ano_exercicio )
        processos_list['funcionarios'].append ( processos.funcionarios )
        processos_list['volume_produzido_no_ano'].append ( processos.volume_produzido_no_ano )
        processos_list['capacidade_produzida'].append ( processos.capacidade_produzida )
        processos_list['refugo_retrabalho'].append ( processos.refugo_retrabalho )
        processos_list['custos_garantia'].append ( processos.custos_garantia )
        processos_list['entregas_no_prazo'].append ( processos.entregas_no_prazo )
        processos_list['valor_do_estoque'].append ( processos.valor_do_estoque )

    anos = processos_list['ano_exercicio']
    for key in processos_list:
        processos_list[key] = zip ( processos_list[key], anos )
    processos_list['id'] = anos

    v = 'e'

    try:
        avaliacao = AvaliacaoProcessos.objects.get ( processos=vObj )
    except AvaliacaoProcessos.DoesNotExist:
        avaliacao = AvaliacaoProcessos ( processos=vObj )
        avaliacao.save ()
        v = 'ne'
    return render ( request, 'objetivos/produtividade.html', {
        'processos': processos_list,
        'avaliacao': avaliacao,
        'v': v,
    } )



@login_required
@is_allowed
def qualidade(request,user):
    owner = get_object_or_404 ( User, username=user )
    processos_objects = Processos.objects.filter ( user=owner ).all ().order_by ( '-ano_exercicio' )[:1]

    # Campos que serão exibidos
    processos_list = {
        # Campos estáticos
        'ano_exercicio': [],
        'funcionarios': [],
        'volume_produzido_no_ano': [],
        'capacidade_produzida': [],
        'refugo_retrabalho': [],
        'custos_garantia': [],
        'entregas_no_prazo': [],
        'valor_do_estoque': [],
    }
    for processos in processos_objects:
        # Campos estáticos
        processos_list['ano_exercicio'].append ( processos.ano_exercicio )
        vObj = Processos.objects.get ( user=owner, ano_exercicio=processos.ano_exercicio )
        processos_list['funcionarios'].append ( processos.funcionarios )
        processos_list['volume_produzido_no_ano'].append ( processos.volume_produzido_no_ano )
        processos_list['capacidade_produzida'].append ( processos.capacidade_produzida )
        processos_list['refugo_retrabalho'].append ( processos.refugo_retrabalho )
        processos_list['custos_garantia'].append ( processos.custos_garantia )
        processos_list['entregas_no_prazo'].append ( processos.entregas_no_prazo )
        processos_list['valor_do_estoque'].append ( processos.valor_do_estoque )

    anos = processos_list['ano_exercicio']
    for key in processos_list:
        processos_list[key] = zip ( processos_list[key], anos )
    processos_list['id'] = anos

    v = 'e'

    try:
        avaliacao = AvaliacaoProcessos.objects.get ( processos=vObj )
    except AvaliacaoProcessos.DoesNotExist:
        avaliacao = AvaliacaoProcessos ( processos=vObj )
        avaliacao.save ()
        v = 'ne'
    return render ( request, 'objetivos/qualidade.html', {
        'processos': processos_list,
        'avaliacao': avaliacao,
        'v': v,
    } )



@login_required
@is_allowed
def prazos_estoques(request,user):
    owner = get_object_or_404 ( User, username=user )
    processos_objects = Processos.objects.filter ( user=owner ).all ().order_by ( '-ano_exercicio' )[:1]

    # Campos que serão exibidos
    processos_list = {
        # Campos estáticos
        'ano_exercicio': [],
        'funcionarios': [],
        'volume_produzido_no_ano': [],
        'capacidade_produzida': [],
        'refugo_retrabalho': [],
        'custos_garantia': [],
        'entregas_no_prazo': [],
        'valor_do_estoque': [],
    }
    for processos in processos_objects:
        # Campos estáticos
        processos_list['ano_exercicio'].append ( processos.ano_exercicio )
        vObj = Processos.objects.get ( user=owner, ano_exercicio=processos.ano_exercicio )
        processos_list['funcionarios'].append ( processos.funcionarios )
        processos_list['volume_produzido_no_ano'].append ( processos.volume_produzido_no_ano )
        processos_list['capacidade_produzida'].append ( processos.capacidade_produzida )
        processos_list['refugo_retrabalho'].append ( processos.refugo_retrabalho )
        processos_list['custos_garantia'].append ( processos.custos_garantia )
        processos_list['entregas_no_prazo'].append ( processos.entregas_no_prazo )
        processos_list['valor_do_estoque'].append ( processos.valor_do_estoque )

    anos = processos_list['ano_exercicio']
    for key in processos_list:
        processos_list[key] = zip ( processos_list[key], anos )
    processos_list['id'] = anos

    v = 'e'

    try:
        avaliacao = AvaliacaoProcessos.objects.get ( processos=vObj )
    except AvaliacaoProcessos.DoesNotExist:
        avaliacao = AvaliacaoProcessos ( processos=vObj )
        avaliacao.save ()
        v = 'ne'
    return render ( request, 'objetivos/prazos_estoques.html', {
        'processos': processos_list,
        'avaliacao': avaliacao,
        'v': v,
    } )




