from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

# Create your models here.

class Empresa(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='empresas')
    allowed_users = models.ManyToManyField(User, blank=True)
    cnpj = models.CharField(max_length=20, unique=True, blank=True, validators=[RegexValidator('^[0-9]{2}\.?[0-9]{3}\.?[0-9]{3}\/?[0-9]{4}\-?[0-9]{2}$', message="Insira um CNPJ válido.")])
