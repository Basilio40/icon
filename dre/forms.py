from django.forms import ModelForm
from dre.models import Dre
from crispy_forms.helper import FormHelper

class DreForm(ModelForm):

    class Meta:
        model = Dre
        fields = ['ano_exercicio',
                'receita_servico',
                'receita_produto',
                'outras_receitas',
                #'deducoes_receitas',
                'imposto_sobre_receitas',
                #'custo_fixo',
                #'custo_fixo_folha',
                #'custo_fixo_material',
                'custo_das_mercadorias_vendidas',
                'custo_dos_produtos_industrializados',
                'despesas_com_pessoal',
                'despesas_administrativas',
                'despesas_ocupacao',
                'despesas_logistica',
                'despesas_vendas',
                'despesas_viagens',
                'despesas_servicos_pj',
                'despesas_tributarias',
                #'despesas_operacionais',
                #'despesas_folha',
                'despesas_financeiras',
                'receitas_financeiras',
                'despesas_indedutiveis',
                'alienacao_ativo_fixo',
                'irpj_e_csll',
                'depreciacao_amortizacao',
                'equivalente_patrimonial',
                'restituicao_correcao_monetaria',
                'endividamento',
                'inadimplencia',
                ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['ano_exercicio'].widget.attrs['readonly'] = True
