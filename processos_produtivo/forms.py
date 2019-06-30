from django.forms import ModelForm
from dre.models import Processo
from crispy_forms.helper import FormHelper

class ProcessoForm(ModelForm):

    class Meta:
        model = Vendas
        fields = ['ano_exercicio' ,
                'funcionarios' ,
                'volume_produzido_no_ano' ,
                'capacidade_produzida' ,
                'refugo_retrabalho',
                'custos_garantia' ,
                'entregas_no_prazo' ,
                'valor_do_estoque' ,
                ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['ano_exercicio'].widget.attrs['readonly'] = True