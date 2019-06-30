from django.forms import ModelForm
from .models import Pessoas
from crispy_forms.helper import FormHelper

class PessoasForm(ModelForm):

    class Meta:
        model = Pessoas
        fields = ['ano_exercicio',
                'funcionarios_antigos',
                'rotatividade',
                'absenteismo'
                ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['ano_exercicio'].widget.attrs['readonly'] = True