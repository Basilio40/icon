from swot.models import Concorrente, AnaliseConcorrencia, Cliente, Fornecedor, AnalisesMacro
from swot.utils import *
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