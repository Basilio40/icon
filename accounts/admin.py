from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Empresa

# Register your models here.

class EmpresaInline(admin.StackedInline):
    model = Empresa
    can_delete = False
    verbose_name = 'Empresa'
    verbose_name_plural = 'Empresas'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (EmpresaInline,)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
