def select_smile(destaque):
    """
    Função que gera um selectpicker com o smile em evidência.
    """
    payload = []
    if destaque == 'Neutro':
        payload.append("""<option value='Neutro' data-content="<i class='far fa-flushed' style='font-size:24px;color:yellow'></i>"></option>""")
    elif destaque == 'Bom':
        payload.append("""<option value='Bom' data-content="<i class='far fa-grin-alt' style='font-size:24px;color:green'></i>"></option>""")
    else:
        payload.append("""<option value='Ruim' data-content="<i class='far fa-angry' style='font-size:24px;color:red'></i>"></option>""")
    order = ['Neutro', 'Bom', 'Ruim']
    for i in order:
        if i == destaque:
            pass
        elif i == 'Neutro':
            payload.append("""<option value='Neutro' data-content="<i class='far fa-flushed' style='font-size:24px;color:yellow'></i> "></option>""")
        elif i == 'Bom':
            payload.append("""<option value='Bom' data-content="<i class='far fa-grin-alt' style='font-size:24px;color:green'></i>"></option>""")
        else:
            payload.append("""<option value='Ruim' data-content="<i class='far fa-angry' style='font-size:24px;color:red'></i>"></option>""")

    return payload

def calcula_campos_dinamicos(dre):
    dre_list = {}
    receita_bruta = dre.receita_servico + dre.receita_produto + dre.outras_receitas
    dre_list['receita_bruta'] = receita_bruta

    despesas_operacionais = dre.despesas_administrativas + dre.despesas_com_pessoal + dre.despesas_ocupacao + dre.despesas_logistica + dre.despesas_vendas + dre.despesas_viagens + dre.despesas_servicos_pj + dre.despesas_tributarias + dre.depreciacao_amortizacao

    receita_liquida = receita_bruta - dre.imposto_sobre_receitas
    dre_list['receita_liquida'] = receita_liquida

    custo_total = dre.custo_das_mercadorias_vendidas + dre.custo_dos_produtos_industrializados
    dre_list['custo_total'] = custo_total

    lucro_bruto = receita_liquida - custo_total
    dre_list['lucro_bruto'] = lucro_bruto

    

    rdd = dre.endividamento * 0.058
    dre_list['rdd'] = rdd
    
    
    lucro_operacional = lucro_bruto + dre.receitas_financeiras - dre.despesas_financeiras - despesas_operacionais
    dre_list['lucro_operacional'] = lucro_operacional

    lucro_liquido = lucro_operacional - dre.despesas_indedutiveis + dre.alienacao_ativo_fixo
    dre_list['lucro_liquido'] = lucro_liquido

    ebitda = dre.receitas_financeiras + lucro_operacional + dre.imposto_sobre_receitas - dre.depreciacao_amortizacao
    dre_list['ebitda'] = ebitda

    ebit = ebitda - dre.depreciacao_amortizacao
    dre_list['ebit'] = ebit

    rentabilidade = (lucro_liquido/receita_bruta) * 100
    dre_list['rentabilidade'] = rentabilidade

    return dre_list
