from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import *
from accounts.decorators import is_allowed
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@login_required
@is_allowed
def mapa_estrategico(request, user):

    return render(request, 'mapa_estrategico.html')
