from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import DreForm
from .models import Dre
from django.views.decorators.csrf import csrf_exempt
from accounts.decorators import  is_allowed
from django.contrib.auth.models import User
from django.utils.formats import localize

@is_allowed
def list(request, user):
    """
        View que lista os últimos 4 DREs, tratados para exibição.
    """
    owner = get_object_or_404(User, username=user)
    dre_objects: object = Dre.objects.filter(user=owner).all().order_by('-ano_exercicio')[:4]

    # Campos que serão exibidos
    dre_list = {
        # Campos estáticos
        'ano_exercicio': [],
        'receita_servico': [],
        'receita_produto': [],
        'outras_receitas': [],
        'deducoes_receitas': [],
        'imposto_sobre_receitas': [],
        #'custo_fixo': [],
        #'custo_fixo_folha': [],
        #'custo_fixo_material': [],
        'custo_das_mercadorias_vendidas': [],
        'custo_dos_produtos_industrializados': [],
        'despesas_com_pessoal': [],
        'despesas_administrativas': [],
        #'despesas_comunicacao': [],
        'despesas_ocupacao': [],
        #'despesas_escritorio': [],
        'despesas_logistica': [],
        'despesas_vendas': [],
        'despesas_viagens': [],
        'despesas_servicos_pj': [],
        'despesas_tributarias': [],
        'despesas_operacionais': [],
        #'despesas_folha': [],
        'receitas_financeiras': [],
        'despesas_financeiras': [],
        'despesas_indedutiveis': [],
        'alienacao_ativo_fixo': [],
        'depreciacao_amortizacao': [],
        'irpj_e_csll': [],
        'equivalente_patrimonial': [],
        #'despesas_nao_operacionais': [],
        'restituicao_correcao_monetaria': [],
        'endividamento': [],
        'inadimplencia': [],
        # Campos dinâmicos
        'receita_bruta': [],
        'receita_liquida': [],
        'custo_total': [],
        'lucro_bruto': [],
        'ebitda': [],
        'ebit': [],
        'rdd': [],
        'lucro_operacional': [],
        'lucro_liquido': [],
        'resultado_exercicio': [],
    }

    # Loop que cria a lista tratada
    for dre in dre_objects:
        # Campos estáticos
        dre_list['ano_exercicio'].append(dre.ano_exercicio)
        dre_list['receita_servico'].append(dre.receita_servico)
        dre_list['receita_produto'].append(dre.receita_produto)
        dre_list['outras_receitas'].append(dre.outras_receitas)
        dre_list['deducoes_receitas'].append(dre.imposto_sobre_receitas)
        dre_list['imposto_sobre_receitas'].append(dre.imposto_sobre_receitas)
        #dre_list['custo_fixo'].append(dre.custo_fixo)
        #dre_list['custo_fixo_folha'].append(dre.custo_fixo_folha)
        #dre_list['custo_fixo_material'].append(dre.custo_fixo_material)
        dre_list['custo_das_mercadorias_vendidas'].append(dre.custo_das_mercadorias_vendidas)
        dre_list['custo_dos_produtos_industrializados'].append(dre.custo_dos_produtos_industrializados)
        dre_list['despesas_com_pessoal'].append(dre.despesas_com_pessoal)
        dre_list['despesas_administrativas'].append(dre.despesas_administrativas)
      # dre_list['despesas_comunicacao'].append(dre.despesas_comunicacao )
        dre_list['despesas_ocupacao'].append(dre.despesas_ocupacao )
        #dre_list['despesas_escritorio'].append ( dre.despesas_escritorio )
        dre_list['despesas_logistica'].append ( dre.despesas_logistica )
        dre_list['despesas_vendas'].append ( dre.despesas_vendas )
        dre_list['despesas_viagens'].append ( dre.despesas_viagens )
        dre_list['despesas_servicos_pj'].append ( dre.despesas_servicos_pj )
        dre_list['despesas_tributarias'].append ( dre.despesas_tributarias )

        despesas_operacionais = dre.despesas_administrativas + dre.despesas_com_pessoal + dre.despesas_ocupacao + dre.despesas_logistica + dre.despesas_vendas + dre.despesas_viagens + dre.despesas_servicos_pj + dre.despesas_tributarias + dre.depreciacao_amortizacao
        dre_list['despesas_operacionais'].append (despesas_operacionais )

        dre_list['despesas_financeiras'].append(dre.despesas_financeiras)
        dre_list['receitas_financeiras'].append(dre.receitas_financeiras)

        dre_list['alienacao_ativo_fixo'].append(dre.alienacao_ativo_fixo)
        dre_list['despesas_indedutiveis'].append(dre.despesas_indedutiveis)

        dre_list['irpj_e_csll'].append(dre.irpj_e_csll)
        #dre_list['despesas_folha'].append(dre.despesas_folha)
        dre_list['depreciacao_amortizacao'].append(dre.depreciacao_amortizacao)
        dre_list['equivalente_patrimonial'].append(dre.equivalente_patrimonial)
        #dre_list['despesas_nao_operacionais'].append(dre.despesas_nao_operacionais)
        dre_list['restituicao_correcao_monetaria'].append(dre.restituicao_correcao_monetaria)
        dre_list['endividamento'].append(dre.endividamento)
        dre_list['inadimplencia'].append(dre.inadimplencia)
        # Campos dinâmicos
        receita_bruta = dre.receita_servico + dre.receita_produto + dre.outras_receitas
        dre_list['receita_bruta'].append(receita_bruta)

        receita_liquida = receita_bruta - dre.imposto_sobre_receitas
        dre_list['receita_liquida'].append(receita_liquida)

        custo_total = dre.custo_das_mercadorias_vendidas + dre.custo_dos_produtos_industrializados
        dre_list['custo_total'].append(custo_total)

        lucro_bruto = receita_liquida - custo_total
        dre_list['lucro_bruto'].append(lucro_bruto)

       


        lucro_operacional = lucro_bruto + dre.receitas_financeiras - dre.despesas_financeiras - despesas_operacionais
        dre_list['lucro_operacional'].append(lucro_operacional)

        lucro_liquido = lucro_operacional - dre.despesas_indedutiveis + dre.alienacao_ativo_fixo
        dre_list['lucro_liquido'].append(lucro_liquido)

        resultado_exercicio = lucro_liquido - dre.irpj_e_csll
        dre_list['resultado_exercicio'].append(resultado_exercicio)

        ebitda = dre.receitas_financeiras + lucro_operacional + dre.imposto_sobre_receitas - dre.depreciacao_amortizacao
        dre_list['ebitda'].append(ebitda)

        ebit = ebitda - dre.depreciacao_amortizacao
        dre_list['ebit'].append(ebit)

        rdd = dre.endividamento * 0.058
        dre_list['rdd'].append(rdd)
    # Completa os campos com placeholder, caso necessário
    for i in range(4-len(dre_objects)):
        for key in dre_list:
            dre_list[key].append('')

    # Adiciona o campo ano a cada um dos campos
    anos = dre_list['ano_exercicio']
    for key in dre_list:
        dre_list[key] = zip(dre_list[key], anos)
    dre_list['id'] = anos

    return render(request, 'dre/dre_listing.html', {'dre': dre_list})


def detail(request, user, ano):
    """
        View que retorna apenas 1 DRE, com base no ano, para exibição.
    """
    owner = get_object_or_404(User, username=user)
    dre = get_object_or_404(Dre, user=owner, ano_exercicio=ano)
    # Campos dinâmicos
    dre.receita_bruta = dre.receita_servico + dre.receita_produto + dre.outras_receitas
    dre.receita_liquida = dre.receita_bruta - dre.imposto_sobre_receitas
    dre.custo_total = dre.custo_das_mercadorias_vendidas + dre.custo_dos_produtos_industrializados
    dre.lucro_bruto = dre.receita_liquida - dre.custo_total
    dre.despesas_operacionais = dre.despesas_administrativas + dre.despesas_com_pessoal + dre.despesas_ocupacao + dre.despesas_logistica + dre.despesas_vendas + dre.despesas_viagens + dre.despesas_servicos_pj + dre.despesas_tributarias + dre.depreciacao_amortizacao
    dre.lucro_operacional = dre.lucro_bruto + dre.receitas_financeiras - dre.despesas_financeiras - dre.despesas_operacionais
    dre.ebitda = dre.receitas_financeiras + dre.lucro_operacional + dre.imposto_sobre_receitas - dre.depreciacao_amortizacao
    dre.ebit = dre.ebitda - dre.depreciacao_amortizacao
    dre.rdd = dre.endividamento * 0.058
    dre.lucro_liquido = dre.lucro_operacional - dre.despesas_indedutiveis + dre.alienacao_ativo_fixo

    return render(request, 'dre/dre_detail.html', {'dre': dre})


@login_required
@is_allowed
def create(request, user):
    title = "DRE – Demonstração do Resultado do Exercício"
    form = DreForm(request.POST or None)
    form.fields['ano_exercicio'].widget.attrs['readonly'] = False

    if form.is_valid():
        form.save()
        messages.success(request,
                         'DRE cadastrada com sucesso!')
        return redirect('dre:list', user=user)

    context = {
        'title': title,
        'form': form
    }

    return render(request, 'dre/dre_form.html', context)


@login_required
def edit(request, user, ano):
    title = "DRE – Demonstração do Resultado do Exercício"
    owner = get_object_or_404(User, username=user)
    dre = get_object_or_404(Dre, user=owner, ano_exercicio=ano)
    form = DreForm(request.POST or None, instance=dre)

    if form.is_valid():
        form.save()
        messages.success(request,
                         'DRE editada com sucesso!')
        return redirect('dre:list', user=user)

    context = {
        'title': title,
        'form': form,
    }

    return render(request, 'dre/dre_form.html', context)


@login_required
def delete(request, user, ano):
    owner = get_object_or_404(User, username=user)
    dre = get_object_or_404(Dre, user=owner, ano_exercicio=ano)

    if request.method == 'POST':
        dre.delete()
        messages.success(request,
                         'DRE deletada com sucesso!')
        return redirect('dre:list', user=user)

    return render(request, 'dre/dre_delete.html', {'dre': dre, 'ano':ano})

@login_required
@csrf_exempt
@is_allowed
def api_save(request, user, ano):
    if request.method == 'POST':
        owner = get_object_or_404(User, username=user)
        dre = get_object_or_404(Dre, user=owner, ano_exercicio=ano)
        dre.receita_servico = request.POST['receita_servico']
        dre.receita_produto = request.POST['receita_produto']
        dre.outras_receitas = request.POST['outras_receitas']
        #dre.deducoes_receitas = request.POST['deducoes_receitas']
        dre.imposto_sobre_receitas = request.POST['imposto_sobre_receitas']
        dre.custo_das_mercadorias_vendidas = request.POST['custo_das_mercadorias_vendidas']
        dre.custo_dos_produtos_industrializados = request.POST['custo_dos_produtos_industrializados']
        dre.despesas_com_pessoal = request.POST['despesas_com_pessoal']       
        dre.despesas_administrativas = request.POST['despesas_administrativas']
       # dre.despesas_comunicacao = request.POST['despesas_comunicacao']
        dre.despesas_ocupacao = request.POST['despesas_ocupacao']
        #dre.despesas_escritorio = request.POST['despesas_escritorio']
        dre.despesas_logistica = request.POST['despesas_logistica']
        dre.despesas_vendas = request.POST['despesas_vendas']
        dre.despesas_viagens = request.POST['despesas_viagens']
        dre.despesas_servicos_pj = request.POST['despesas_servicos_pj']
        dre.despesas_tributarias = request.POST['despesas_tributarias']
        #dre.despesas_operacionais = request.POST['despesas_operacionais']
        #dre.despesas_folha = request.POST['despesas_folha']
        dre.receitas_financeiras = request.POST['receitas_financeiras']
        dre.despesas_financeiras = request.POST['despesas_financeiras']

        dre.alienacao_ativo_fixo = request.POST['alienacao_ativo_fixo']
        dre.despesas_indedutiveis = request.POST['despesas_indedutiveis']

        dre.depreciacao_amortizacao = request.POST['depreciacao_amortizacao']
        dre.equivalente_patrimonial = request.POST['equivalente_patrimonial']
        #dre.despesas_nao_operacionais = request.POST['despesas_nao_operacionais']
        dre.restituicao_correcao_monetaria = request.POST['restituicao_correcao_monetaria']
        dre.endividamento = request.POST['endividamento']
        dre.inadimplencia = request.POST['inadimplencia']
        dre.irpj_e_csll = request.POST['irpj_e_csll']
        dre.save()
    return redirect('dre:list', user=user)
