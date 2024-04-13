from django.urls import path
from .views import BancoList, ConsultaBanco, page

urlpatterns = [
    path('api/banks/', BancoList.as_view(), name='bancos-list'),
    path('api/banks/<int:codigo>/', ConsultaBanco.as_view(), name='consultar_banco'),
    path('', page, name='index')
]
