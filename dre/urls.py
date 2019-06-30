from dre import views
from django.urls import path

app_name = 'dre'

urlpatterns = [
    path('<user>/', views.list, name='list'),
    path('<user>/add/', views.create, name='add'),
    path('<user>/<ano>/', views.detail, name='detail'),
    path('<user>/<ano>/edit/', views.edit, name='edit'),
    path('<user>/<ano>/delete/', views.delete, name='delete'),
    path('<user>/api/<ano>/', views.api_save, name='api_save')
]
