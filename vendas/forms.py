from django.forms import ModelForm
from dre.models import Vendas
from crispy_forms.helper import FormHelper

class VendasForm(ModelForm):

    class Meta:
        model = Vendas
        fields = ['ano_exercicio' ,
                'carteira_de_clientes_ativa' ,
                'novos_clientes_no_ano' ,
                'propostas_enviadas_no_ano' ,
                'notas_fiscais_emitidas',
                'clientes_fidelizados' ,
                'reclamacoes_clientes' ,
                'clientes_perdidos' ,
                ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['ano_exercicio'].widget.attrs['readonly'] = True