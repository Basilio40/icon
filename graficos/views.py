from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from accounts.decorators import is_allowed
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from objetivos.utils import calcula_campos_dinamicos
from dre.models import Dre
from objetivos.models import *
from swot.models import *
from .utils import *
from swot.utils import calcula_competitividade

# Create your views here.
@login_required
@is_allowed
def grafico_dre(request, user):
    # Objetos do banco de dados
    owner = get_object_or_404(User, username=user)
    dres = Dre.objects.all().filter(user=owner).order_by('ano_exercicio')
    dicio_retorno = {
        'anos': [],
        'receitas': [],
        'lucros': [],
        'rentabilidades': [],
        'ebitdas': [],
        'lucros_liquidos': [],
        'despesas': []
    }

    for dre in dres:
        campos_dinamicos = calcula_campos_dinamicos(dre)

        dicio_retorno['anos'].append(dre.ano_exercicio)
        dicio_retorno['receitas'].append(campos_dinamicos['receita_bruta'])
        dicio_retorno['lucros'].append(campos_dinamicos['lucro_bruto'])
        dicio_retorno['rentabilidades'].append(campos_dinamicos['rentabilidade'])
        dicio_retorno['ebitdas'].append(campos_dinamicos['ebitda'])
        dicio_retorno['lucros_liquidos'].append(campos_dinamicos['lucro_liquido'])
        dicio_retorno['despesas'].append(campos_dinamicos['custo_total'])

    return render(request, 'graficos/grafico_dre.html', dicio_retorno)

@login_required
@is_allowed
def ped_inicial(request, user):
    # Objetos do banco de dados
    owner = get_object_or_404(User, username=user)
    dre = Dre.objects.all().filter(user=owner).order_by('-ano_exercicio')[0]

    total_preenchimento = 0
    total_smile_points = 0

    # Verifica objetivos de receitas
    # Espera-se um range de -3/3 smiles points
    try:
        objetivo = ObjetivoReceitas.objects.get(dre_base=dre)
        analise_objetivo = AnaliseObjetivoReceitas.objects.get(objetivo_receitas_base=objetivo)
        total_preenchimento += 1
        total_smile_points += calcula_smile_points(analise_objetivo.smile_receita_bruta)
        total_smile_points += calcula_smile_points(analise_objetivo.smile_crescimento_quatro)
        total_smile_points += calcula_smile_points(analise_objetivo.smile_crescimento)
    except:
        pass

    # Verifica objetivos de rentabilidade
    # Espera-se um range de -6/6 smile points
    try:
        objetivo = ObjetivoRentabilidade.objects.get(dre_base=dre)
        analise_objetivo = AnaliseObjetivoRentabilidade.objects.get(objetivo_rentabilidade_base=objetivo)
        total_preenchimento += 1
        total_smile_points += calcula_smile_points(analise_objetivo.smile_lucro_liquido)
        total_smile_points += calcula_smile_points(analise_objetivo.smile_rentabilidade_media)
        total_smile_points += calcula_smile_points(analise_objetivo.smile_rentabilidade_ultimo)
        total_smile_points += calcula_smile_points(analise_objetivo.smile_rentabilidade_comparada)
        total_smile_points += calcula_smile_points(analise_objetivo.smile_ebitda_medio)
        total_smile_points += calcula_smile_points(analise_objetivo.smile_ebitda_ultimo)
    except:
        pass

    # Verifica objetivos de endividamento
    # Espera-se um range de -3/3 smiles points
    try:
        objetivo = ObjetivoEndividamentos.objects.get(dre_base=dre)
        analise_objetivo = AnaliseObjetivoEndividamento.objects.get(objetivo_endividamento_base=objetivo)
        total_preenchimento += 1
        total_smile_points += calcula_smile_points(smile_divida)
        total_smile_points += calcula_smile_points(smile_taxa_divida_lucro)
        total_smile_points += calcula_smile_points(smile_inadimplencia)
    except:
        pass

    porcentagem_financeiro = 1
    porcentagem_financeiro += 9 * total_preenchimento
    if total_smile_points > 0:
        porcentagem_financeiro += 6 * total_smile_points

    questoes = Questao.objects.all()
    respostas = []
    pontos_respostas = 0
    for questao in questoes:
        try:
            resposta = Resposta.objects.get(questao=questao, user=owner)
            respostas.append(resposta)
            if resposta.resposta == 'Sim':
                pontos_respostas += 1
            elif resposta.resposta == 'Não':
                pontos_respostas -= 1
            else:
                pass
        except:
            pass

    porcentagem_sobrevivencia = len(respostas) * (30/len(questoes))
    if pontos_respostas > 0:
        porcentagem_sobrevivencia += pontos_respostas * (70/len(questoes))

    # Objetos do banco de dados
    owner = get_object_or_404(User, username=user)
    dre = Dre.objects.all().filter(user=owner).order_by('-ano_exercicio')[0]

    total_preenchimento = 0
    total_smile_points = 0

    # Verifica objetivos de receitas
    # Espera-se um range de -3/3 smiles points
    try:
        objetivo = ObjetivoReceitas.objects.get(dre_base=dre)
        analise_objetivo = AnaliseObjetivoReceitas.objects.get(objetivo_receitas_base=objetivo)
        total_preenchimento += 1
        total_smile_points += calcula_smile_points(analise_objetivo.smile_receita_bruta)
        total_smile_points += calcula_smile_points(analise_objetivo.smile_crescimento_quatro)
        total_smile_points += calcula_smile_points(analise_objetivo.smile_crescimento)
    except:
        pass

    # Verifica objetivos de rentabilidade
    # Espera-se um range de -6/6 smile points
    try:
        objetivo = ObjetivoRentabilidade.objects.get(dre_base=dre)
        analise_objetivo = AnaliseObjetivoRentabilidade.objects.get(objetivo_rentabilidade_base=objetivo)
        total_preenchimento += 1
        total_smile_points += calcula_smile_points(analise_objetivo.smile_lucro_liquido)
        total_smile_points += calcula_smile_points(analise_objetivo.smile_rentabilidade_media)
        total_smile_points += calcula_smile_points(analise_objetivo.smile_rentabilidade_ultimo)
        total_smile_points += calcula_smile_points(analise_objetivo.smile_rentabilidade_comparada)
        total_smile_points += calcula_smile_points(analise_objetivo.smile_ebitda_medio)
        total_smile_points += calcula_smile_points(analise_objetivo.smile_ebitda_ultimo)
    except:
        pass

    # Verifica objetivos de endividamento
    # Espera-se um range de -3/3 smiles points
    try:
        objetivo = ObjetivoEndividamentos.objects.get(dre_base=dre)
        analise_objetivo = AnaliseObjetivoEndividamento.objects.get(objetivo_endividamento_base=objetivo)
        total_preenchimento += 1
        total_smile_points += calcula_smile_points(smile_divida)
        total_smile_points += calcula_smile_points(smile_taxa_divida_lucro)
        total_smile_points += calcula_smile_points(smile_inadimplencia)
    except:
        pass

    porcentagem_gestao = 1
    porcentagem_gestao += 33 * total_preenchimento


    porcentagem_resultado = 4
    if total_smile_points > 0:
        porcentagem_resultado += 8 * total_smile_points

    dicio_retorno = {'porcentagem_gestao': int((porcentagem_financeiro+porcentagem_sobrevivencia+porcentagem_gestao+porcentagem_resultado)/4),
                     'porcentagem_desempenho': int((porcentagem_gestao+porcentagem_resultado)/2)}
    return render(request, 'graficos/ped0_0.html', dicio_retorno)

@login_required
@is_allowed
def ped_gestao(request, user):
    # Objetos do banco de dados
    owner = get_object_or_404(User, username=user)
    dre = Dre.objects.all().filter(user=owner).order_by('-ano_exercicio')[0]

    total_preenchimento = 0
    total_smile_points = 0

    # Verifica objetivos de receitas
    # Espera-se um range de -3/3 smiles points
    try:
        objetivo = ObjetivoReceitas.objects.get(dre_base=dre)
        analise_objetivo = AnaliseObjetivoReceitas.objects.get(objetivo_receitas_base=objetivo)
        total_preenchimento += 1
        total_smile_points += calcula_smile_points(analise_objetivo.smile_receita_bruta)
        total_smile_points += calcula_smile_points(analise_objetivo.smile_crescimento_quatro)
        total_smile_points += calcula_smile_points(analise_objetivo.smile_crescimento)
    except:
        pass

    # Verifica objetivos de rentabilidade
    # Espera-se um range de -6/6 smile points
    try:
        objetivo = ObjetivoRentabilidade.objects.get(dre_base=dre)
        analise_objetivo = AnaliseObjetivoRentabilidade.objects.get(objetivo_rentabilidade_base=objetivo)
        total_preenchimento += 1
        total_smile_points += calcula_smile_points(analise_objetivo.smile_lucro_liquido)
        total_smile_points += calcula_smile_points(analise_objetivo.smile_rentabilidade_media)
        total_smile_points += calcula_smile_points(analise_objetivo.smile_rentabilidade_ultimo)
        total_smile_points += calcula_smile_points(analise_objetivo.smile_rentabilidade_comparada)
        total_smile_points += calcula_smile_points(analise_objetivo.smile_ebitda_medio)
        total_smile_points += calcula_smile_points(analise_objetivo.smile_ebitda_ultimo)
    except:
        pass

    # Verifica objetivos de endividamento
    # Espera-se um range de -3/3 smiles points
    try:
        objetivo = ObjetivoEndividamentos.objects.get(dre_base=dre)
        analise_objetivo = AnaliseObjetivoEndividamento.objects.get(objetivo_endividamento_base=objetivo)
        total_preenchimento += 1
        total_smile_points += calcula_smile_points(smile_divida)
        total_smile_points += calcula_smile_points(smile_taxa_divida_lucro)
        total_smile_points += calcula_smile_points(smile_inadimplencia)
    except:
        pass

    porcentagem_financeiro = 1
    porcentagem_financeiro += 9 * total_preenchimento
    if total_smile_points > 0:
        porcentagem_financeiro += 6 * total_smile_points

    questoes = Questao.objects.all()
    respostas = []
    pontos_respostas = 0
    for questao in questoes:
        try:
            resposta = Resposta.objects.get(questao=questao, user=owner)
            respostas.append(resposta)
            if resposta.resposta == 'Sim':
                pontos_respostas += 1
            elif resposta.resposta == 'Não':
                pontos_respostas -= 1
            else:
                pass
        except:
            pass

    porcentagem_sobrevivencia = len(respostas) * (30/len(questoes))
    if pontos_respostas > 0:
        porcentagem_sobrevivencia += pontos_respostas * (70/len(questoes))

    # Objetos do banco de dados
    owner = get_object_or_404(User, username=user)
    dre = Dre.objects.all().filter(user=owner).order_by('-ano_exercicio')[0]

    total_preenchimento = 0
    total_smile_points = 0

    # Verifica objetivos de receitas
    # Espera-se um range de -3/3 smiles points
    try:
        objetivo = ObjetivoReceitas.objects.get(dre_base=dre)
        analise_objetivo = AnaliseObjetivoReceitas.objects.get(objetivo_receitas_base=objetivo)
        total_preenchimento += 1
        total_smile_points += calcula_smile_points(analise_objetivo.smile_receita_bruta)
        total_smile_points += calcula_smile_points(analise_objetivo.smile_crescimento_quatro)
        total_smile_points += calcula_smile_points(analise_objetivo.smile_crescimento)
    except:
        pass

    # Verifica objetivos de rentabilidade
    # Espera-se um range de -6/6 smile points
    try:
        objetivo = ObjetivoRentabilidade.objects.get(dre_base=dre)
        analise_objetivo = AnaliseObjetivoRentabilidade.objects.get(objetivo_rentabilidade_base=objetivo)
        total_preenchimento += 1
        total_smile_points += calcula_smile_points(analise_objetivo.smile_lucro_liquido)
        total_smile_points += calcula_smile_points(analise_objetivo.smile_rentabilidade_media)
        total_smile_points += calcula_smile_points(analise_objetivo.smile_rentabilidade_ultimo)
        total_smile_points += calcula_smile_points(analise_objetivo.smile_rentabilidade_comparada)
        total_smile_points += calcula_smile_points(analise_objetivo.smile_ebitda_medio)
        total_smile_points += calcula_smile_points(analise_objetivo.smile_ebitda_ultimo)
    except:
        pass

    # Verifica objetivos de endividamento
    # Espera-se um range de -3/3 smiles points
    try:
        objetivo = ObjetivoEndividamentos.objects.get(dre_base=dre)
        analise_objetivo = AnaliseObjetivoEndividamento.objects.get(objetivo_endividamento_base=objetivo)
        total_preenchimento += 1
        total_smile_points += calcula_smile_points(smile_divida)
        total_smile_points += calcula_smile_points(smile_taxa_divida_lucro)
        total_smile_points += calcula_smile_points(smile_inadimplencia)
    except:
        pass

    porcentagem_gestao = 1
    porcentagem_gestao += 33 * total_preenchimento


    porcentagem_resultado = 4
    if total_smile_points > 0:
        porcentagem_resultado += 8 * total_smile_points

    dicio_retorno = {'porcentagem_diagnostico': int((porcentagem_financeiro + porcentagem_sobrevivencia)/2),
                     'porcentagem_estrategia': int((porcentagem_gestao+porcentagem_resultado)/2)}
    return render(request, 'graficos/ped0_1.html', dicio_retorno)

@login_required
@is_allowed
def ped_desempenho(request, user):
    # Objetos do banco de dados
    owner = get_object_or_404(User, username=user)
    dre = Dre.objects.all().filter(user=owner).order_by('-ano_exercicio')[0]

    total_preenchimento = 0
    total_smile_points = 0

    # Verifica objetivos de receitas
    # Espera-se um range de -3/3 smiles points
    try:
        objetivo = ObjetivoReceitas.objects.get(dre_base=dre)
        analise_objetivo = AnaliseObjetivoReceitas.objects.get(objetivo_receitas_base=objetivo)
        total_preenchimento += 1
        total_smile_points += calcula_smile_points(analise_objetivo.smile_receita_bruta)
        total_smile_points += calcula_smile_points(analise_objetivo.smile_crescimento_quatro)
        total_smile_points += calcula_smile_points(analise_objetivo.smile_crescimento)
    except:
        pass

    # Verifica objetivos de rentabilidade
    # Espera-se um range de -6/6 smile points
    try:
        objetivo = ObjetivoRentabilidade.objects.get(dre_base=dre)
        analise_objetivo = AnaliseObjetivoRentabilidade.objects.get(objetivo_rentabilidade_base=objetivo)
        total_preenchimento += 1
        total_smile_points += calcula_smile_points(analise_objetivo.smile_lucro_liquido)
        total_smile_points += calcula_smile_points(analise_objetivo.smile_rentabilidade_media)
        total_smile_points += calcula_smile_points(analise_objetivo.smile_rentabilidade_ultimo)
        total_smile_points += calcula_smile_points(analise_objetivo.smile_rentabilidade_comparada)
        total_smile_points += calcula_smile_points(analise_objetivo.smile_ebitda_medio)
        total_smile_points += calcula_smile_points(analise_objetivo.smile_ebitda_ultimo)
    except:
        pass

    # Verifica objetivos de endividamento
    # Espera-se um range de -3/3 smiles points
    try:
        objetivo = ObjetivoEndividamentos.objects.get(dre_base=dre)
        analise_objetivo = AnaliseObjetivoEndividamento.objects.get(objetivo_endividamento_base=objetivo)
        total_preenchimento += 1
        total_smile_points += calcula_smile_points(smile_divida)
        total_smile_points += calcula_smile_points(smile_taxa_divida_lucro)
        total_smile_points += calcula_smile_points(smile_inadimplencia)
    except:
        pass

    porcentagem_gestao = 1
    porcentagem_gestao += 33 * total_preenchimento


    porcentagem_resultado = 4
    if total_smile_points > 0:
        porcentagem_resultado += 8 * total_smile_points

    dicio_retorno = {'porcentagem_gestao': porcentagem_gestao,
                     'porcentagem_resultado': porcentagem_resultado}
    return render(request, 'graficos/ped2_0.html', dicio_retorno)

@login_required
@is_allowed
def ped_diagnostico(request, user):
    # Objetos do banco de dados
    owner = get_object_or_404(User, username=user)
    dre = Dre.objects.all().filter(user=owner).order_by('-ano_exercicio')[0]

    total_preenchimento = 0
    total_smile_points = 0

    # Verifica objetivos de receitas
    # Espera-se um range de -3/3 smiles points
    try:
        objetivo = ObjetivoReceitas.objects.get(dre_base=dre)
        analise_objetivo = AnaliseObjetivoReceitas.objects.get(objetivo_receitas_base=objetivo)
        total_preenchimento += 1
        total_smile_points += calcula_smile_points(analise_objetivo.smile_receita_bruta)
        total_smile_points += calcula_smile_points(analise_objetivo.smile_crescimento_quatro)
        total_smile_points += calcula_smile_points(analise_objetivo.smile_crescimento)
    except:
        pass

    # Verifica objetivos de rentabilidade
    # Espera-se um range de -6/6 smile points
    try:
        objetivo = ObjetivoRentabilidade.objects.get(dre_base=dre)
        analise_objetivo = AnaliseObjetivoRentabilidade.objects.get(objetivo_rentabilidade_base=objetivo)
        total_preenchimento += 1
        total_smile_points += calcula_smile_points(analise_objetivo.smile_lucro_liquido)
        total_smile_points += calcula_smile_points(analise_objetivo.smile_rentabilidade_media)
        total_smile_points += calcula_smile_points(analise_objetivo.smile_rentabilidade_ultimo)
        total_smile_points += calcula_smile_points(analise_objetivo.smile_rentabilidade_comparada)
        total_smile_points += calcula_smile_points(analise_objetivo.smile_ebitda_medio)
        total_smile_points += calcula_smile_points(analise_objetivo.smile_ebitda_ultimo)
    except:
        pass

    # Verifica objetivos de endividamento
    # Espera-se um range de -3/3 smiles points
    try:
        objetivo = ObjetivoEndividamentos.objects.get(dre_base=dre)
        analise_objetivo = AnaliseObjetivoEndividamento.objects.get(objetivo_endividamento_base=objetivo)
        total_preenchimento += 1
        total_smile_points += calcula_smile_points(smile_divida)
        total_smile_points += calcula_smile_points(smile_taxa_divida_lucro)
        total_smile_points += calcula_smile_points(smile_inadimplencia)
    except:
        pass

    porcentagem_financeiro = 1
    porcentagem_financeiro += 9 * total_preenchimento
    if total_smile_points > 0:
        porcentagem_financeiro += 6 * total_smile_points

    questoes = Questao.objects.all()
    respostas = []
    pontos_respostas = 0
    for questao in questoes:
        try:
            resposta = Resposta.objects.get(questao=questao, user=owner)
            respostas.append(resposta)
            if resposta.resposta == 'Sim':
                pontos_respostas += 1
            elif resposta.resposta == 'Não':
                pontos_respostas -= 1
            else:
                pass
        except:
            pass

    '''
    porcentagem_sobrevivencia = len(respostas) * (30/len(questoes))
    if pontos_respostas > 0:
        porcentagem_sobrevivencia += pontos_respostas * (70/len(questoes))
    '''
    porcentagem_sobrevivencia = 50
    porcentagem_sobrevivencia += (pontos_respostas) / len(questoes) * 100 / 3.23


    dicio_retorno = {'porcentagem_financeiro': porcentagem_financeiro,
                     'porcentagem_sobrevivencia': int(porcentagem_sobrevivencia)}
    return render(request, 'graficos/ped1_0.html', dicio_retorno)

@login_required
@is_allowed
def diagnostico_amb_ext(request, user):
    # Objetos do banco de dados
    owner = get_object_or_404(User, username=user)
    questoes = Questao.objects.all()
    respostas = []
    pontos_respostas = 0
    for questao in questoes:
        try:
            resposta = Resposta.objects.get(questao=questao, user=owner)
            respostas.append(resposta)
            if resposta.resposta == 'Sim':
                pontos_respostas += 1
            elif resposta.resposta == 'Não':
                pontos_respostas -= 1
            else:
                pass
        except:
            pass

    concorrentes = Concorrente.objects.filter(user=owner)
    clientes = Cliente.objects.filter(user=owner)
    fornecedores = Fornecedor.objects.filter(user=owner)

    analise = AnaliseConcorrencia.objects.get_or_create(user=owner)[0]

    concorrentes_p = pontuacao_ext_concorrentes(concorrentes)
    clientes_p = pontuacao_ext_clientes(clientes)
    fornecedor_p = pontuacao_ext_fornecedor(fornecedores)

    porcentagem_sobrevivencia = len(respostas) * (30/len(questoes))
    if pontos_respostas > 0:
        porcentagem_sobrevivencia += pontos_respostas * (70/len(questoes))
    dicio_retorno = {'porcentagem_sobrevivencia': int(porcentagem_sobrevivencia),
                     'concorrencia': concorrentes_p,
                     'clientes': clientes_p,
                     'fornecedores': fornecedor_p}
    return render(request, 'graficos/diagnostico_amb_ext.html', dicio_retorno)

@login_required
@is_allowed
def diagnostico_amb_int(request, user):
    # Objetos do banco de dados
    owner = get_object_or_404(User, username=user)
    dre = Dre.objects.all().filter(user=owner).order_by('-ano_exercicio')[0]

    total_preenchimento = 0
    total_smile_points = 0

    # Verifica objetivos de receitas
    # Espera-se um range de -3/3 smiles points
    try:
        objetivo = ObjetivoReceitas.objects.get(dre_base=dre)
        analise_objetivo = AnaliseObjetivoReceitas.objects.get(objetivo_receitas_base=objetivo)
        total_preenchimento += 1
        total_smile_points += calcula_smile_points(analise_objetivo.smile_receita_bruta)
        total_smile_points += calcula_smile_points(analise_objetivo.smile_crescimento_quatro)
        total_smile_points += calcula_smile_points(analise_objetivo.smile_crescimento)
    except:
        pass

    # Verifica objetivos de rentabilidade
    # Espera-se um range de -6/6 smile points
    try:
        objetivo = ObjetivoRentabilidade.objects.get(dre_base=dre)
        analise_objetivo = AnaliseObjetivoRentabilidade.objects.get(objetivo_rentabilidade_base=objetivo)
        total_preenchimento += 1
        total_smile_points += calcula_smile_points(analise_objetivo.smile_lucro_liquido)
        total_smile_points += calcula_smile_points(analise_objetivo.smile_rentabilidade_media)
        total_smile_points += calcula_smile_points(analise_objetivo.smile_rentabilidade_ultimo)
        total_smile_points += calcula_smile_points(analise_objetivo.smile_rentabilidade_comparada)
        total_smile_points += calcula_smile_points(analise_objetivo.smile_ebitda_medio)
        total_smile_points += calcula_smile_points(analise_objetivo.smile_ebitda_ultimo)
    except:
        pass

    # Verifica objetivos de endividamento
    # Espera-se um range de -3/3 smiles points
    try:
        objetivo = ObjetivoEndividamentos.objects.get(dre_base=dre)
        analise_objetivo = AnaliseObjetivoEndividamento.objects.get(objetivo_endividamento_base=objetivo)
        total_preenchimento += 1
        total_smile_points += calcula_smile_points(smile_divida)
        total_smile_points += calcula_smile_points(smile_taxa_divida_lucro)
        total_smile_points += calcula_smile_points(smile_inadimplencia)
    except:
        pass

    porcentagem_financeiro = 1
    porcentagem_financeiro += 9 * total_preenchimento
    if total_smile_points > 0:
        porcentagem_financeiro += 6 * total_smile_points

    questoes = Questao.objects.all()
    respostas = []
    pontos_respostas = 0
    for questao in questoes:
        try:
            resposta = Resposta.objects.get(questao=questao, user=owner)
            respostas.append(resposta)
            if resposta.resposta == 'Sim':
                pontos_respostas += 1
            elif resposta.resposta == 'Não':
                pontos_respostas -= 1
            else:
                pass
        except:
            pass
    porcentagem_sobrevivencia = len(respostas) * (30/len(questoes))
    if pontos_respostas > 0:
        porcentagem_sobrevivencia += pontos_respostas * (70/len(questoes))

    p_s = 0
    if porcentagem_sobrevivencia < 30:
        p_s = porcentagem_sobrevivencia
    elif porcentagem_sobrevivencia < 70:
        p_s = porcentagem_sobrevivencia - 30
    else:
        p_s = porcentagem_sobrevivencia - 70

    pf = 0
    if porcentagem_financeiro < 30:
        pf = porcentagem_financeiro
    elif porcentagem_financeiro < 70:
        pf = porcentagem_financeiro - 30
    else:
        pf = porcentagem_financeiro - 70

    dicio_retorno = {'porcentagem_sobrevivencia': int(porcentagem_sobrevivencia), 'porcentagem_financeiro': porcentagem_financeiro, 'ps': p_s, 'pf': pf}
    return render(request, 'graficos/diagnostico_amb_int.html', dicio_retorno)
