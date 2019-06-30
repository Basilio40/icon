from swot.models import Concorrente, AnaliseConcorrencia, Cliente, Fornecedor
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