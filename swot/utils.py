def calcula_competitividade(valor):
    if valor == 'Sou melhor':
        return 2
    elif valor == 'Sou igual':
        return 1
    else:
        return 0

def calcula_competitividade_cliente(valor):
    if valor == 'Eu Encanto':
        return 2
    elif valor == 'Eu Atendo':
        return 1
    else:
        return 0

def calcula_competitividade_fornecedor(valor):
    if valor == 'Me Encanta':
        return 2
    elif valor == 'Me Atende':
        return 1
    else:
        return 0