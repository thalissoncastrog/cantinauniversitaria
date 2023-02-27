"""
URL configuration for cantina project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from cliente.views import Indice, Sobre, Menu, BuscaMenu, Pedido, ConfirmarPedido, ConfirmarPagamento

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('allauth.urls')),
    path('funcionario/',include('funcionario.urls')),
    path('', Indice.as_view(), name = 'indice'),
    path('sobre/', Sobre.as_view(), name = 'sobre'),
    path('menu/', Menu.as_view(), name='menu'),
    path('menu/busca/',BuscaMenu.as_view(),name='busca-menu'),
    path('pedido/', Pedido.as_view(), name='pedido'),
    path('confirmar-pedido/<int:pk>',ConfirmarPedido.as_view(),name='confirmar-pedido'),
    path('confirmar-pagamento/',ConfirmarPagamento.as_view(),name='confirmar-pagamento')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
