from django.http import HttpResponseRedirect
from functools import wraps
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied

def redirect_if_logged_in(func):
    @wraps(func)
    def decorator(request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect('/')
        return func(request, *args, **kwargs)
    return decorator

def is_allowed(func: object) -> object:
    """
    Decorator que verifica se o usuário tem permissões sobre aquele objeto.
    """
    @wraps(func)
    def decorator(request, user, *args, **kwargs):
        if request.user.is_authenticated:
            owner = get_object_or_404(User, username=user)
            if request.user == owner:
                return func(request, user, *args, **kwargs)
            elif request.user in owner.empresas.allowed_users.all():
                return func(request, user, *args, **kwargs)
            else:
                raise PermissionDenied
        else:
            return HttpResponseRedirect(reverse('accounts:login'))
        return HttpResponseForbidden()
    return decorator
