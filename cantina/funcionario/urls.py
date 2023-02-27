from django.urls import path
from .views import Dashboard, DetalhesPedido

urlpatterns = [
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
    path('pedidos/<int:pk>/', DetalhesPedido.as_view(), name='detalhes-do-pedido')
]