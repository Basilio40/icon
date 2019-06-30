from django.urls import path
#from django.contrib.auth.views import login, logout
#from django.core.urlresolvers import reverse_lazy
from django.conf.urls import url
from accounts.views import register
from django.contrib.auth import views as auth_views
from django.contrib.auth import views as RegisterForm
from django.contrib.auth import views as LoginView
from django.contrib.auth import views as LogoutinView

app_name = 'accounts'

urlpatterns = [
    path('login/',auth_views.LoginView.as_view(
        template_name='login.html',
        redirect_authenticated_user=True,
        extra_context={
            'next': '/graficos/inicial/user/',
        },
    ),name="login",),
    path('logout/',auth_views.LogoutView.as_view(template_name='index.html'), name="logout"),
    path('cadastre-se/', register,name='register' ),
]
