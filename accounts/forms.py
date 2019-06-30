from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Empresa
from django.core.validators import RegexValidator

class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class EmpresaRegisterForm(forms.Form):
    cnpj = forms.CharField(min_length=14, max_length=20, required=False, validators=[RegexValidator('^[0-9]{2}\.?[0-9]{3}\.?[0-9]{3}\/?[0-9]{4}\-?[0-9]{2}$', message="Insira um CNPJ válido.")])

    def clean_cnpj(self):
        cnpj = self.cleaned_data['cnpj']
        cnpj = cnpj.replace('.', '').replace('/', '').replace('-', '')
        num_itens = Empresa.objects.filter(cnpj=cnpj).count()
        if num_itens != 0:
            raise forms.ValidationError("Já existe uma conta com esse CNPJ.")
        return cnpj
