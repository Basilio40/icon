from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, redirect
from accounts.forms import RegisterForm, EmpresaRegisterForm
from .models import Empresa
from django.contrib.auth import logout
from .decorators import redirect_if_logged_in

@redirect_if_logged_in
def register(request):
    template_name = 'accounts/register.html'
    form = RegisterForm(request.POST or None)
    empresa_form = EmpresaRegisterForm(request.POST or None)

    if form.is_valid() and empresa_form.is_valid():
        form.save()
        empresa = Empresa.objects.create(user=form.instance, cnpj=empresa_form['cnpj'].value())
        messages.success(request, 'Usuário cadastrado com sucesso!')
        return redirect(settings.LOGIN_URL)

    return render(request, template_name, {'form': form, 'empresa_form': empresa_form})

def logout(request):
    logout(request)
    return HttpResponseRedirect('/')
