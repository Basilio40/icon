from django.shortcuts import render, get_object_or_404
from accounts.decorators import is_allowed
from django.contrib.auth.models import User
from dre.models import Dre
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .models import *
from .utils import select_smile, calcula_campos_dinamicos
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
@login_required
@is_allowed
def definir_objetivo_de_receitas(request, user):
    # Objetos do banco de dados
    owner = get_object_or_404(User, username=user)
    dre = Dre.objects.all().filter(user=owner).order_by('-ano_exercicio')[0]
    objetivo = ObjetivoReceitas.objects.get_or_create(dre_base=dre)[0]
    analise_objetivo = AnaliseObjetivoReceitas.objects.get_or_create(objetivo_receitas_base=objetivo)[0]

    # Campos para exibição
    receita_bruta = dre.receita_servico + dre.receita_produto + dre.outras_receitas
    try:
        dre_passado = Dre.objects.get(user=owner, ano_exercicio=dre.ano_exercicio-3)
        receita_bruta_passado = dre_passado.receita_servico + dre_passado.receita_produto + dre_passado.outras_receitas
        crescimento_quatro = receita_bruta - receita_bruta_passado
        crescimento = (crescimento_quatro / receita_bruta_passado) * 100
    except Exception as e:
        crescimento_quatro = 0.0
        crescimento = 0.0
    #tags = {
    #    '1.0': {'text': 'Estável','value': 1.0},
    #    '1.05': {'text': '5%','value': 1.05},
    #    '1.1': {'text': '10%','value': 1.10},
    #}

    # Campo porcentagem
    #tag_destaque = []
    #tag_destaque.append(tags[str(objetivo.percentage)])
    #del tags[str(objetivo.percentage)]
    #for key in tags:
    #    tag_destaque.append(tags[key])

    # Campos smile
    smiles = {}
    smiles['smile_receita_bruta'] = select_smile(analise_objetivo.smile_receita_bruta)
    smiles['smile_crescimento_quatro'] = select_smile(analise_objetivo.smile_crescimento_quatro)
    smiles['smile_crescimento'] = select_smile(analise_objetivo.smile_crescimento)

    dicio_retorno = {'receita': receita_bruta,  'smiles':smiles,
                     'receita_': receita_bruta * objetivo.percentage,
                     'crescimento_quatro': crescimento_quatro,
                     'crescimento': crescimento, 'objetivo_atual': (objetivo.percentage-1)*100}
    return render(request, 'objetivos/def_objetivos_receitas.html', dicio_retorno)

@login_required
@csrf_exempt
@is_allowed
def salvar_objetivo_de_receitas(request, user):
    if request.method == 'POST':
        # Objetos do banco de dados
        owner = get_object_or_404(User, username=user)
        dre = Dre.objects.all().filter(user=owner).order_by('-ano_exercicio')[0]
        objetivo = ObjetivoReceitas.objects.get_or_create(dre_base=dre)[0]
        analise_objetivo = AnaliseObjetivoReceitas.objects.get_or_create(objetivo_receitas_base=objetivo)[0]

        # Atualização de campos
        objetivo.percentage = float(request.POST['percentage'])
        analise_objetivo.smile_receita_bruta = request.POST['smile_receita_bruta']
        analise_objetivo.smile_crescimento_quatro = request.POST['smile_crescimento_quatro']
        analise_objetivo.smile_crescimento = request.POST['smile_crescimento']

        # Salvamento no banco de dados
        objetivo.save()
        analise_objetivo.save()
    return HttpResponse('')

@login_required
@is_allowed
def definir_objetivo_de_rentabilidade(request, user):
    # Objetos do banco de dados
    owner = get_object_or_404(User, username=user)
    dre = Dre.objects.all().filter(user=owner).order_by('-ano_exercicio')[0]
    objetivo = ObjetivoRentabilidade.objects.get_or_create(dre_base=dre)[0]
    analise_objetivo = AnaliseObjetivoRentabilidade.objects.get_or_create(objetivo_rentabilidade_base=objetivo)[0]

    # Campos para exibição
    campos_dinamicos =  calcula_campos_dinamicos(dre)
    receita_bruta = campos_dinamicos['receita_bruta']
    lucro_liquido = campos_dinamicos['lucro_liquido']
    count = 1
    ebitda_total = campos_dinamicos['ebitda']
    rentabilidade_total = campos_dinamicos['rentabilidade']
    for i in range(1,4):
        try:
            novo_dre = Dre.objects.get(ano_exercicio=dre.ano_exercicio-i)
            novos_campos_dinamicos = calcula_campos_dinamicos(novo_dre)
            ebitda_total += novos_campos_dinamicos['ebitda']
            rentabilidade_total += novos_campos_dinamicos['rentabilidade']

            count += 1
        except:
            pass
    ebitda_medio = ebitda_total / count
    rentabilidade_media = rentabilidade_total / count
    try:
        novo_dre = Dre.objects.get(ano_exercicio=dre.ano_exercicio-1)
        rentabilidade_ano_passado = calcula_campos_dinamicos(novo_dre)['rentabilidade']
    except:
        rentabilidade_ano_passado = 0.0

    # Campos smile
    smiles = {}
    smiles['smile_lucro_liquido'] = select_smile(analise_objetivo.smile_lucro_liquido)
    smiles['smile_rentabilidade_media'] = select_smile(analise_objetivo.smile_rentabilidade_media)
    smiles['smile_rentabilidade_ultimo'] = select_smile(analise_objetivo.smile_rentabilidade_ultimo)
    smiles['smile_rentabilidade_comparada'] = select_smile(analise_objetivo.smile_rentabilidade_comparada)
    smiles['smile_ebitda_medio'] = select_smile(analise_objetivo.smile_ebitda_medio)
    smiles['smile_ebitda_ultimo'] = select_smile(analise_objetivo.smile_ebitda_ultimo)

    dicio_retorno = {'receita': receita_bruta,
                     'receita_': receita_bruta * objetivo.rentabilidade_percentage,
                     'ebitda': campos_dinamicos['ebitda'], 'smiles': smiles,
                     'ebitda_': campos_dinamicos['ebitda'] * objetivo.ebitda_percentage,
                     'lucro_liquido': lucro_liquido,
                     'ebitda_medio': ebitda_medio,
                     'rentabilidade_media': rentabilidade_media,
                     'rentabilidade': campos_dinamicos['rentabilidade'],
                     'rentabilidade_comparada': campos_dinamicos['rentabilidade'] - rentabilidade_ano_passado,
                     'rentabilidade_percentage': objetivo.rentabilidade_percentage * 100,
                     'ebitda_percentage': (objetivo.ebitda_percentage - 1) * 100
    }
    return render(request, 'objetivos/def_objetivos_rentabilidade.html', dicio_retorno)

@login_required
@csrf_exempt
@is_allowed
def salvar_objetivo_de_rentabilidade(request, user):
    if request.method == 'POST':
        # Objetos do banco de dados
        owner = get_object_or_404(User, username=user)
        dre = Dre.objects.all().filter(user=owner).order_by('-ano_exercicio')[0]
        objetivo = ObjetivoRentabilidade.objects.get_or_create(dre_base=dre)[0]
        analise_objetivo = AnaliseObjetivoRentabilidade.objects.get_or_create(objetivo_rentabilidade_base=objetivo)[0]

        # Atualização de campos
        objetivo.rentabilidade_percentage = float(request.POST['rentabilidade_percentage'])
        objetivo.ebitda_percentage = float(request.POST['ebitda_percentage'])
        analise_objetivo.smile_lucro_liquido = request.POST['smile_lucro_liquido']
        analise_objetivo.smile_rentabilidade_media = request.POST['smile_rentabilidade_media']
        analise_objetivo.smile_rentabilidade_ultimo = request.POST['smile_rentabilidade_ultimo']
        analise_objetivo.smile_rentabilidade_comparada = request.POST['smile_rentabilidade_comparada']
        analise_objetivo.smile_ebitda_medio = request.POST['smile_ebitda_medio']
        analise_objetivo.smile_ebitda_ultimo = request.POST['smile_ebitda_ultimo']

        # Salvamento no banco de dados
        objetivo.save()
        analise_objetivo.save()
    return HttpResponse('')

@login_required
@is_allowed
def definir_objetivo_de_endividamento(request, user):
    # Objetos do banco de dados
    owner = get_object_or_404(User, username=user)
    dre = Dre.objects.all().filter(user=owner).order_by('-ano_exercicio')[0]
    objetivo = ObjetivoEndividamento.objects.get_or_create(dre_base=dre)[0]
    analise_objetivo = AnaliseObjetivoEndividamento.objects.get_or_create(objetivo_endividamento_base=objetivo)[0]

    # Campos para exibição
    campos_dinamicos =  calcula_campos_dinamicos(dre)
    lucro = campos_dinamicos['lucro_liquido']

    # Campos smile
    smiles = {}
    smiles['smile_divida'] = select_smile(analise_objetivo.smile_divida)
    smiles['smile_taxa_divida_lucro'] = select_smile(analise_objetivo.smile_taxa_divida_lucro)
    smiles['smile_inadimplencia'] = select_smile(analise_objetivo.smile_inadimplencia)

    dicio_retorno = {
                     'inadimplencia_percentage': (1-objetivo.inadimplencia_percentage)*100,
                     'divida_percentage': (1-objetivo.divida_percentage) * 100,
                     'inadimplencia': dre.inadimplencia,
                     'inadimplencia_': dre.inadimplencia * objetivo.inadimplencia_percentage,
                     'divida': dre.endividamento,
                     'divida_': dre.endividamento * objetivo.divida_percentage,
                     'smiles': smiles,
                     'taxa': dre.endividamento / lucro,
    }
    return render(request, 'objetivos/def_objetivos_endividamento.html', dicio_retorno)

@login_required
@csrf_exempt
@is_allowed
def salvar_objetivo_de_endividamento(request, user):
    if request.method == 'POST':
        # Objetos do banco de dados
        owner = get_object_or_404(User, username=user)
        dre = Dre.objects.all().filter(user=owner).order_by('-ano_exercicio')[0]
        objetivo = ObjetivoEndividamento.objects.get_or_create(dre_base=dre)[0]
        analise_objetivo = AnaliseObjetivoEndividamento.objects.get_or_create(objetivo_endividamento_base=objetivo)[0]

        # Atualização de campos
        objetivo.inadimplencia_percentage = float(request.POST['inadimplencia_percentage'])
        objetivo.divida_percentage = float(request.POST['divida_percentage'])
        analise_objetivo.smile_divida = request.POST['smile_divida']
        analise_objetivo.smile_taxa_divida_lucro = request.POST['smile_taxa_divida_lucro']
        analise_objetivo.smile_inadimplencia = request.POST['smile_inadimplencia']

        # Salvamento no banco de dados
        objetivo.save()
        analise_objetivo.save()
    return HttpResponse('')

@login_required
@is_allowed
def analise_desempenho_financeiro(request, user):
    """
    Essa view reaproveita código de todas as outras.
    """
    # Objetos do banco de dados
    owner = get_object_or_404(User, username=user)
    dre = Dre.objects.all().filter(user=owner).order_by('-ano_exercicio')[0]

    # Campos para exibição
    campos_dinamicos =  calcula_campos_dinamicos(dre)
    receita_bruta = campos_dinamicos['receita_bruta']
    lucro_liquido = campos_dinamicos['lucro_liquido']
    rentabilidade = campos_dinamicos['rentabilidade']
    ebitda = campos_dinamicos['ebitda']

    count = 1
    ebitda_total = campos_dinamicos['ebitda']
    rentabilidade_total = campos_dinamicos['rentabilidade']
    for i in range(1,4):
        try:
            novo_dre = Dre.objects.get(ano_exercicio=dre.ano_exercicio-i)
            novos_campos_dinamicos = calcula_campos_dinamicos(novo_dre)
            ebitda_total += novos_campos_dinamicos['ebitda']
            rentabilidade_total += novos_campos_dinamicos['rentabilidade']

            count += 1
        except:
            pass
    ebitda_medio = ebitda_total / count
    rentabilidade_media = rentabilidade_total / count
    try:
        novo_dre = Dre.objects.get(ano_exercicio=dre.ano_exercicio-1)
        rentabilidade_ano_passado = calcula_campos_dinamicos(novo_dre)['rentabilidade']
    except:
        rentabilidade_ano_passado = 0.0
    try:
        dre_passado = Dre.objects.get(user=owner, ano_exercicio=dre.ano_exercicio-3)
        receita_bruta_passado = dre_passado.receita_servico + dre_passado.receita_produto + dre_passado.outras_receitas
        crescimento_quatro = receita_bruta - receita_bruta_passado
        crescimento = (crescimento_quatro / receita_bruta_passado) * 100
    except Exception as e:
        crescimento_quatro = 0.0
        crescimento = 0.0

    # Smiles
    smiles = {}
    # Receitas
    objetivo = ObjetivoReceitas.objects.get_or_create(dre_base=dre)[0]
    analise_objetivo = AnaliseObjetivoReceitas.objects.get_or_create(objetivo_receitas_base=objetivo)[0]
    smiles['smile_receita_bruta'] = select_smile(analise_objetivo.smile_receita_bruta)
    smiles['smile_crescimento_quatro'] = select_smile(analise_objetivo.smile_crescimento_quatro)
    smiles['smile_crescimento'] = select_smile(analise_objetivo.smile_crescimento)
    # Rentabilidade
    objetivo = ObjetivoRentabilidade.objects.get_or_create(dre_base=dre)[0]
    analise_objetivo = AnaliseObjetivoRentabilidade.objects.get_or_create(objetivo_rentabilidade_base=objetivo)[0]
    smiles['smile_lucro_liquido'] = select_smile(analise_objetivo.smile_lucro_liquido)
    smiles['smile_rentabilidade_media'] = select_smile(analise_objetivo.smile_rentabilidade_media)
    smiles['smile_rentabilidade_ultimo'] = select_smile(analise_objetivo.smile_rentabilidade_ultimo)
    smiles['smile_rentabilidade_comparada'] = select_smile(analise_objetivo.smile_rentabilidade_comparada)
    smiles['smile_ebitda_medio'] = select_smile(analise_objetivo.smile_ebitda_medio)
    smiles['smile_ebitda_ultimo'] = select_smile(analise_objetivo.smile_ebitda_ultimo)
    # Endividamento
    objetivo = ObjetivoEndividamento.objects.get_or_create(dre_base=dre)[0]
    analise_objetivo = AnaliseObjetivoEndividamento.objects.get_or_create(objetivo_endividamento_base=objetivo)[0]
    smiles['smile_divida'] = select_smile(analise_objetivo.smile_divida)
    smiles['smile_taxa_divida_lucro'] = select_smile(analise_objetivo.smile_taxa_divida_lucro)
    smiles['smile_inadimplencia'] = select_smile(analise_objetivo.smile_inadimplencia)

    dicio_retorno = {'receita_bruta': receita_bruta, 'lucro_liquido': lucro_liquido,
                     'ebitda_medio': ebitda_medio, 'rentabilidade_media': rentabilidade_media,
                     'rentabilidade': rentabilidade, 'ebitda': ebitda,
                     'rentabilidade_comparada': campos_dinamicos['rentabilidade'] - rentabilidade_ano_passado,
                     'crescimento': crescimento, 'crescimento_quatro': crescimento_quatro,
                     'divida': dre.endividamento,
                     'taxa': dre.endividamento / lucro_liquido, 'smiles': smiles}
    return render(request, 'objetivos/analise_desemp_financ.html', dicio_retorno)

@login_required
@csrf_exempt
@is_allowed
def salvar_analise_desempenho_financeiro(request, user):
    if request.method == 'POST':
        # Objetos do banco de dados
        owner = get_object_or_404(User, username=user)
        dre = Dre.objects.all().filter(user=owner).order_by('-ano_exercicio')[0]

        # Receitas
        objetivo = ObjetivoReceitas.objects.get_or_create(dre_base=dre)[0]
        analise_objetivo = AnaliseObjetivoReceitas.objects.get_or_create(objetivo_receitas_base=objetivo)[0]

        # Atualização de campos
        analise_objetivo.smile_receita_bruta = request.POST['smile_receita_bruta']
        analise_objetivo.smile_crescimento_quatro = request.POST['smile_crescimento_quatro']
        analise_objetivo.smile_crescimento = request.POST['smile_crescimento']

        # Salvamento no banco de dados
        analise_objetivo.save()

        # Rentabilidade
        objetivo = ObjetivoRentabilidade.objects.get_or_create(dre_base=dre)[0]
        analise_objetivo = AnaliseObjetivoRentabilidade.objects.get_or_create(objetivo_rentabilidade_base=objetivo)[0]

        # Atualização de campos
        analise_objetivo.smile_lucro_liquido = request.POST['smile_lucro_liquido']
        analise_objetivo.smile_rentabilidade_media = request.POST['smile_rentabilidade_media']
        analise_objetivo.smile_rentabilidade_ultimo = request.POST['smile_rentabilidade_ultimo']
        analise_objetivo.smile_rentabilidade_comparada = request.POST['smile_rentabilidade_comparada']
        analise_objetivo.smile_ebitda_medio = request.POST['smile_ebitda_medio']
        analise_objetivo.smile_ebitda_ultimo = request.POST['smile_ebitda_ultimo']

        # Salvamento no banco de dados
        analise_objetivo.save()

        # Endividamento
        objetivo = ObjetivoEndividamento.objects.get_or_create(dre_base=dre)[0]
        analise_objetivo = AnaliseObjetivoEndividamento.objects.get_or_create(objetivo_endividamento_base=objetivo)[0]

        # Atualização de campos
        analise_objetivo.smile_divida = request.POST['smile_divida']
        analise_objetivo.smile_taxa_divida_lucro = request.POST['smile_taxa_divida_lucro']
        analise_objetivo.smile_inadimplencia = request.POST['smile_inadimplencia']

        # Salvamento no banco de dados
        analise_objetivo.save()
    return HttpResponse('')

@login_required
@is_allowed
def definir_objetivo_de_custos(request, user):
    # Objetos do banco de dados
    owner = get_object_or_404(User, username=user)
    dre = Dre.objects.all().filter(user=owner).order_by('-ano_exercicio')[0]
    objetivo = ObjetivoCusto.objects.get_or_create(dre_base=dre)[0]
    custos = dre.despesas_com_pessoal + dre.despesas_administrativas+ dre.despesas_ocupacao+dre.despesas_logistica + dre.despesas_vendas + dre.despesas_viagens + dre.despesas_servicos_pj+dre.despesas_tributarias+dre.despesas_financeiras+dre.depreciacao_amortizacao
    porcentagem = objetivo.despesas_com_pessoal + objetivo.despesas_administrativas+ objetivo.despesas_ocupacao+objetivo.despesas_logistica + objetivo.despesas_vendas + objetivo.despesas_viagens + objetivo.despesas_servicos_pj+objetivo.despesas_tributarias+objetivo.despesas_financeiras+objetivo.depreciacao_amortizacao
    dicio_retorno = {'dre': dre, 'objetivo': objetivo, 'custos_totais': custos, 'custos': custos*porcentagem/100, 'porcentagem': porcentagem}
    return render(request, 'objetivos/def_objetivos_custos.html', dicio_retorno)

@login_required
@csrf_exempt
@is_allowed
def salvar_objetivo_de_custos(request, user):
    if request.method == 'POST':
        # Objetos do banco de dados
        owner = get_object_or_404(User, username=user)
        dre = Dre.objects.all().filter(user=owner).order_by('-ano_exercicio')[0]
        objetivo = ObjetivoCusto.objects.get_or_create(dre_base=dre)[0]

        objetivo.despesas_com_pessoal = int(request.POST['despesas_com_pessoal'])
        objetivo.despesas_administrativas = int(request.POST['despesas_administrativas'])
        objetivo.despesas_ocupacao = int(request.POST['despesas_ocupacao'])
        objetivo.despesas_logistica = int(request.POST['despesas_logistica'])
        objetivo.despesas_vendas = int(request.POST['despesas_vendas'])
        objetivo.despesas_viagens = int(request.POST['despesas_viagens'])
        objetivo.despesas_servicos_pj = int(request.POST['despesas_servicos_pj'])
        objetivo.despesas_tributarias = int(request.POST['despesas_tributarias'])
        objetivo.despesas_financeiras = int(request.POST['despesas_financeiras'])
        objetivo.depreciacao_amortizacao = int(request.POST['depreciacao_amortizacao'])

        ObjetivoCustoMensal.objects.filter(objetivo_custo_base=objetivo).delete()

        objetivo.save()
    return HttpResponse('')

@login_required
@is_allowed
def definir_orcamento_mensal(request, user):
    # Objetos do banco de dados
    owner = get_object_or_404(User, username=user)
    dre = Dre.objects.all().filter(user=owner).order_by('-ano_exercicio')[0]
    objetivo = ObjetivoCusto.objects.get(dre_base=dre)

    custos_t = dre.despesas_com_pessoal + dre.despesas_administrativas+ dre.despesas_ocupacao+dre.despesas_logistica + dre.despesas_vendas + dre.despesas_viagens + dre.despesas_servicos_pj+dre.despesas_tributarias+dre.despesas_financeiras+dre.depreciacao_amortizacao

    porcentagem = objetivo.despesas_com_pessoal + objetivo.despesas_administrativas+ objetivo.despesas_ocupacao+objetivo.despesas_logistica + objetivo.despesas_vendas + objetivo.despesas_viagens + objetivo.despesas_servicos_pj+objetivo.despesas_tributarias+objetivo.despesas_financeiras+objetivo.depreciacao_amortizacao

    receita_bruta = dre.receita_servico + dre.receita_produto + dre.outras_receitas

    custo_total = custos_t * porcentagem/100

    balanco = receita_bruta - custo_total

    #ObjetivoCustoMensal.objects.filter(objetivo_custo_base=objetivo).delete()
    try:
        ObjetivoCustoMensal.objects.get(objetivo_custo_base=objetivo, mes=1)
    except:
        meses = list(range(1, 13))
        for mes in meses:
            este = ObjetivoCustoMensal(objetivo_custo_base=objetivo, mes=mes)
            este.despesas_com_pessoal = custo_total/100* objetivo.despesas_com_pessoal/12
            este.despesas_vendas = custo_total/100 * objetivo.despesas_vendas/12
            este.despesas_viagens = custo_total/100 * objetivo.despesas_viagens/12
            este.despesas_ocupacao = custo_total/100 * objetivo.despesas_ocupacao/12
            este.despesas_logistica = custo_total/100 * objetivo.despesas_logistica/12
            este.despesas_financeiras = custo_total/100 * objetivo.despesas_financeiras/12
            este.despesas_tributarias = custo_total/100 * objetivo.despesas_tributarias/12
            este.despesas_administrativas = custo_total/100 * objetivo.despesas_administrativas/12
            este.despesas_servicos_pj = custo_total/100 * objetivo.despesas_servicos_pj/12
            este.depreciacao_amortizacao = custo_total/100 * objetivo.depreciacao_amortizacao/12
            este.save()

    desp_total = {
        'despesas_com_pessoal': custo_total/100 * objetivo.despesas_com_pessoal,
        'despesas_vendas': custo_total/100 * objetivo.despesas_vendas,
        'despesas_viagens': custo_total/100 * objetivo.despesas_viagens,
        'despesas_ocupacao': custo_total/100 * objetivo.despesas_ocupacao,
        'despesas_logistica': custo_total/100 * objetivo.despesas_logistica,
        'despesas_financeiras': custo_total/100 * objetivo.despesas_financeiras,
        'despesas_tributarias': custo_total/100 * objetivo.despesas_tributarias,
        'despesas_administrativas': custo_total/100 * objetivo.despesas_administrativas,
        'despesas_servicos_pj': custo_total/100 * objetivo.despesas_servicos_pj,
        'depreciacao_amortizacao': custo_total/100 * objetivo.depreciacao_amortizacao,
    }
    desp = []
    for i in list(range(1, 13)):
        objetivos_mensais = ObjetivoCustoMensal.objects.get(objetivo_custo_base=objetivo, mes=i)
        desp.append(objetivos_mensais)


    #fields = ['despesas_com_pessoal', 'despesas_administrativas', 'despesas_ocupacao', 'despesas_logistica','despesas_vendas', 'despesas_viagens', 'despesas_servicos_pj', 'despesas_tributarias', 'despesas_financeiras', 'depreciacao_amortizacao']

    today = datetime.today()

    dicio_retorno = {'custo_total': custo_total, 'receita_bruta': receita_bruta, 'balanco': balanco, 'desp': desp, 'range': list(range(1, 13)), 'desp_total': desp_total, 'mes': int(today.month)}
    return render(request, 'objetivos/def_orcamento_mensal.html', dicio_retorno)

@login_required
@is_allowed
@csrf_exempt
def salvar_orcamento_mensal(request, user):
    if request.method == 'POST':
        owner = get_object_or_404(User, username=user)
        dre = Dre.objects.all().filter(user=owner).order_by('-ano_exercicio')[0]
        objetivo = ObjetivoCusto.objects.get(dre_base=dre)

        meses = list(range(1, 13))
        for mes in meses:
            este = ObjetivoCustoMensal.objects.get(objetivo_custo_base=objetivo, mes=mes)
            este.despesas_com_pessoal = request.POST['despesas_com_pessoal_' + str(mes)]
            este.despesas_vendas = request.POST['despesas_vendas_'+str(mes)]
            este.despesas_viagens = request.POST['despesas_viagens_'+str(mes)]
            este.despesas_ocupacao = request.POST['despesas_ocupacao_'+str(mes)]
            este.despesas_logistica = request.POST['despesas_logistica_'+str(mes)]
            este.despesas_financeiras = request.POST['despesas_financeiras_' + str(mes)]
            este.despesas_tributarias = request.POST['despesas_tributarias_' + str(mes)]
            este.despesas_administrativas = request.POST['despesas_administrativas_' + str(mes)]
            este.despesas_servicos_pj = request.POST['despesas_servicos_pj_' + str(mes)]
            este.depreciacao_amortizacao = request.POST['depreciacao_amortizacao_' + str(mes)]
            este.save()
    return HttpResponse('')

@login_required
@is_allowed
def gestao_a_vista(request, user):
    # Objetos do banco de dados
    owner = get_object_or_404(User, username=user)
    dre = Dre.objects.all().filter(user=owner).order_by('-ano_exercicio')[0]
    objetivo = ObjetivoCusto.objects.get(dre_base=dre)

    custos_t = dre.despesas_com_pessoal + dre.despesas_administrativas+ dre.despesas_ocupacao+dre.despesas_logistica + dre.despesas_vendas + dre.despesas_viagens + dre.despesas_servicos_pj+dre.despesas_tributarias+dre.despesas_financeiras+dre.depreciacao_amortizacao

    porcentagem = objetivo.despesas_com_pessoal + objetivo.despesas_administrativas+ objetivo.despesas_ocupacao+objetivo.despesas_logistica + objetivo.despesas_vendas + objetivo.despesas_viagens + objetivo.despesas_servicos_pj+objetivo.despesas_tributarias+objetivo.despesas_financeiras+objetivo.depreciacao_amortizacao

    receita_bruta = dre.receita_servico + dre.receita_produto + dre.outras_receitas

    custo_total = custos_t * porcentagem/100

    balanco = receita_bruta - custo_total

    desp_total = {
        'despesas_com_pessoal': dre.despesas_com_pessoal * objetivo.despesas_com_pessoal,
        'despesas_vendas': dre.despesas_vendas * objetivo.despesas_vendas,
        'despesas_viagens': dre.despesas_viagens * objetivo.despesas_viagens,
        'despesas_ocupacao': dre.despesas_ocupacao * objetivo.despesas_ocupacao,
        'despesas_logistica': dre.despesas_logistica * objetivo.despesas_logistica,
        'despesas_financeiras': dre.despesas_financeiras * objetivo.despesas_financeiras,
        'despesas_tributarias': dre.despesas_tributarias * objetivo.despesas_tributarias,
        'despesas_administrativas': dre.despesas_administrativas * objetivo.despesas_administrativas,
        'despesas_servicos_pj': dre.despesas_servicos_pj * objetivo.despesas_servicos_pj,
        'depreciacao_amortizacao': dre.depreciacao_amortizacao * objetivo.depreciacao_amortizacao,
    }
    desp = []
    for i in list(range(1, 13)):
        objetivos_mensais = ObjetivoCustoMensal.objects.get(objetivo_custo_base=objetivo, mes=i)
        desp.append(objetivos_mensais)


    #fields = ['despesas_com_pessoal', 'despesas_administrativas', 'despesas_ocupacao', 'despesas_logistica','despesas_vendas', 'despesas_viagens', 'despesas_servicos_pj', 'despesas_tributarias', 'despesas_financeiras', 'depreciacao_amortizacao']

    today = datetime.today()

    dicio_retorno = {'custo_total': custo_total, 'receita_bruta': receita_bruta, 'balanco': balanco, 'desp': desp, 'range': list(range(1, 13)), 'desp_total': desp_total, 'mes': int(today.month)}
    return render(request, 'objetivos/gestao_a_vista.html', dicio_retorno)
