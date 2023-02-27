from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.utils.timezone import datetime
from cliente.models import ModeloPedido

class Dashboard(LoginRequiredMixin, UserPassesTestMixin, View):
    def get(self, request, *args, **kwargs):
        #Data Atual
        hoje = datetime.today()
        pedidos = ModeloPedido.objects.filter(
            data_criado__year=hoje.year, data_criado__month=hoje.month, data_criado__day=hoje.day)
        
        #Adicionar o preço dos pedidos, ver se o pedido já foi retirado
        pedidos_nao_retirados = []
        renda_total = 0
        for pedido in pedidos:
            renda_total+=pedido.price
            
            if not pedido.retirado:
                pedidos_nao_retirados.append(pedido)
        
        #Passar renda total e número de pedidos ao template
        context = {
            'pedidos': pedidos_nao_retirados,
            'renda_total': renda_total,
            'total_pedidos': len(pedidos)
        }
        
        return render(request, 'funcionario/dashboard.html', context)
        
    def test_func(self):
        return self.request.user.groups.filter(name='Funcionário').exists()
        
class DetalhesPedido(LoginRequiredMixin, UserPassesTestMixin, View):
    def get(self,request, pk, *args, **kwargs):
        pedido = ModeloPedido.objects.get(pk=pk)
        context = {
            'pedido':pedido
        }
        
        return render(request, 'funcionario/detalhes-pedido.html',context)
        
    def post(self,request,pk,*args,**kwargs):
        pedido = ModeloPedido.objects.get(pk=pk)
        pedido.retirado = True
        pedido.save()
        
        context = {
            'pedido': pedido
        }
        
        return render(request,'funcionario/detalhes-pedido.html',context)
        
    def post(self,request,pk,*args,**kwargs):
        pedido = ModeloPedido.objects.get(pk=pk)
        pedido.pago = True
        pedido.save()
        
        context = {
            'pedido': pedido
        }
        
        return render(request,'funcionario/detalhes-pedido.html',context)
        
    def test_func(self):
        return self.request.user.groups.filter(name='Funcionário').exists()