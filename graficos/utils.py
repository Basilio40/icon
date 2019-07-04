from swot.models import Concorrente, AnaliseConcorrencia, Cliente, Fornecedor, AnalisesMacro
from objetivos.models import *
from vendas.models import *
from swot.utils import *
from processos_produtivo.models import *
from pessoa.models import *

def calcula_smile_points(smile):
    if smile == "Ruim":
        return -1
    elif smile == "Bom":
        return 1
    else:
        return 0

def pontuacao_ext_concorrentes(concorrentes):
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
    return competitividade['media']

def pontuacao_ext_clientes(clientes):
    competitividade = {'preco': 0, 'qualidade': 0, 'entrega': 0, 'inovacao': 0, 'portifolio': 0}
    for cliente in clientes:
        competitividade['preco'] += calcula_competitividade_cliente(cliente.preco)
        competitividade['qualidade'] += calcula_competitividade_cliente(cliente.qualidade)
        competitividade['entrega'] += calcula_competitividade_cliente(cliente.entrega)
        competitividade['inovacao'] += calcula_competitividade_cliente(cliente.inovacao)
        competitividade['portifolio'] += calcula_competitividade_cliente(cliente.portifolio)
    competitividade_media = 0.0
    for i in competitividade:
        try:
            competitividade[i] = (competitividade[i] / (len(clientes)*2))*100
            competitividade_media += competitividade[i]
        except:
            pass
    competitividade['media'] = competitividade_media / 5
    return competitividade['media']

def pontuacao_ext_fornecedor(fornecedores):
    competitividade = {'preco': 0, 'qualidade': 0, 'entrega': 0, 'inovacao': 0, 'portifolio': 0}
    for fornecedor in fornecedores:
        competitividade['preco'] += calcula_competitividade_fornecedor(fornecedor.preco)
        competitividade['qualidade'] += calcula_competitividade_fornecedor(fornecedor.qualidade)
        competitividade['entrega'] += calcula_competitividade_fornecedor(fornecedor.entrega)
        competitividade['inovacao'] += calcula_competitividade_fornecedor(fornecedor.inovacao)
        competitividade['portifolio'] += calcula_competitividade_fornecedor(fornecedor.portifolio)
    competitividade_media = 0.0
    for i in competitividade:
        try:
            competitividade[i] = (competitividade[i] / (len(fornecedores)*2))*100
            competitividade_media += competitividade[i]
        except:
            pass
    competitividade['media'] = competitividade_media / 5
    return competitividade['media']

def pontuacao_macro_ambiente(analise):
    pontuacao = 0
    p_objetivo = 0
    p_ameaca = 0
    for i in range(1, 6):
        p = 0
        p = eval("(get_p(analise.objetivo_"+ str(i) + "_atratividade) + get_p(analise.objetivo_" + str(i) +"_probabilidade)) / 2")
        p_objetivo += p
        p = eval("(get_p(analise.ameaca_"+ str(i) + "_relevancia) + get_p(analise.ameaca_" + str(i) +"_probabilidade)) / 2")
        p_ameaca += p
    p_objetivo = p_objetivo * 10
    p_ameaca = p_ameaca * 10
    pontuacao = (p_objetivo + p_ameaca)/2
    return pontuacao

def get_p(choice):
	if choice == 'Cima':
		return 2
	elif choice == 'Meio':
		return 1
	else:
		return 0

def pontuacao_ext(owner):
    concorrentes = Concorrente.objects.filter(user=owner)
    clientes = Cliente.objects.filter(user=owner)
    fornecedores = Fornecedor.objects.filter(user=owner)
    analise_macro = AnalisesMacro.objects.get_or_create(user=owner)[0]

    concorrentes_p = pontuacao_ext_concorrentes(concorrentes)
    clientes_p = pontuacao_ext_clientes(clientes)
    fornecedor_p = pontuacao_ext_fornecedor(fornecedores)
    analise_p = pontuacao_macro_ambiente(analise_macro)

    return (concorrentes_p + clientes_p + fornecedor_p + analise_p)/4

def porcent_fin(dre):
    # Verifica objetivos de receitas
    # Espera-se um range de -3/3 smiles points
    total_smile_points = 0
    total_preenchimento = 0
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
    return porcentagem_financeiro

def porcen_vend(owner):
    vendas = Vendas.objects.all().filter(user=owner).order_by('-ano_exercicio')[0]
    avaliacao = AvaliacaoVendas.objects.get(vendas=vendas)
    values = ['carteira_de_clientes_ativa', 'novos_clientes_no_ano', 'propostas_enviadas_no_ano', 'propostas_aprovadas_no_ano', 'notas_fiscais_emitidas', 'clientes_fidelizados', 'reclamacoes_clientes', 'clientes_perdidos']
    total = 50
    for v in values:
    	total = total + 50/8 * eval("calcula_smile_points(avaliacao."+v+")")
    return int(total)

def porcen_process(owner):
    processos = Processos.objects.all().filter(user=owner).order_by('-ano_exercicio')[0]
    avaliacao = AvaliacaoProcessos.objects.get(processos=processos)
    values = ['funcionarios','volume_produzido_no_ano','capacidade_produzida','refugo_retrabalho','custos_garantia', 'entregas_no_prazo','valor_do_estoque']
    total = 50
    for v in values:
    	total = total + 50/7 * eval("calcula_smile_points(avaliacao."+v+")")
    return int(total)

def porcen_pessoa(owner):
    pessoas = Pessoas.objects.all().filter(user=owner).order_by('-ano_exercicio')[0]
    avaliacao = AvaliacaoPessoas.objects.get(pessoas=pessoas)
    values = ['nivel_competencias','funcionarios_antigos','rotatividade','absenteismo','engajamento','retencao']
    total = 50
    for v in values:
    	total = total + 50/6 * eval("calcula_smile_points(avaliacao."+v+")")
    return int(total)