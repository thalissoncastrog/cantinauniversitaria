import json
from django.shortcuts import render, redirect
from django.views import View
from django.db.models import Q #Busca do Menu
from django.core.mail import send_mail
from .models import ItemDeMenu, Categoria, ModeloPedido

class Indice(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'cliente/indice.html')
        
class Sobre (View):
    def get(self, request, *args, **kwargs):
        return render(request, 'cliente/sobre.html')
        
class Pedido (View):
    def get(self,request,*args,**kwargs):
        #Retornar cada item de cada categoria
        bebidas = ItemDeMenu.objects.filter(categoria__nome__contains='Bebida')
        doces = ItemDeMenu.objects.filter(categoria__nome__contains='Doce')
        salgados = ItemDeMenu.objects.filter(categoria__nome__contains='Salgado')
        #Passar a um contexto
        context = {
            'bebidas': bebidas,
            'doces': doces,
            'salgados': salgados
        }
        #renderizar modelo
        return render(request, 'cliente/pedido.html',context)
        
    def post(self, request, *args, **kwargs):
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        
        itens_pedido = {
            'itens': []
        }
        
        itens = request.POST.getlist('itens[]')
        
        #Verificar se o usuário não está fazendo pedido que não contém itens
        if not itens:
            return render(request,'cliente/pedido_vazio.html')
        
        for item in itens:
            item_de_menu = ItemDeMenu.objects.get(pk=int(item))
            dados_item = {
                'id': item_de_menu.pk,
                'nome': item_de_menu.nome,
                'preco': item_de_menu.preco,
                'quantidade':item_de_menu.quantidade
            }
            
            #Verificação de Estoque
            if item_de_menu.quantidade < 1:
                return render(request,'cliente/sem_estoque.html', {'item': item_de_menu})
            
            else:
                item_de_menu.quantidade-=1
                item_de_menu.save()
            
            itens_pedido['itens'].append(dados_item)
            
            preco = 0
            ids_item = []
            
        for item in itens_pedido['itens']:
            preco += item['preco']
            ids_item.append(item['id'])
                
        pedido = ModeloPedido.objects.create(price=preco,nome=nome,email=email)
        pedido.itens.add(*ids_item)
        
        #Enviar E-mail ao usuário quando finalizar pedido
        body = ('Agradecemos pelo seu pedido! Sua comida está sendo prepara. Em 5 minutos, você pode descer para a cantina.\n'
            f'Total do Pedido: R$ {preco}\n')
        
        
        send_mail(
            'Agradecemos por enviar seu pedido!',
            body,
            'exemplo@testes.com',
            [email],
            fail_silently=False
        )
            
        context = {
            'itens': itens_pedido['itens'],
            'preco': preco
        }
        
        return redirect('confirmar-pedido',pk=pedido.pk)
        
class ConfirmarPedido(View):
    def get(self, request, pk, *args, **kwargs):
        pedido = ModeloPedido.objects.get(pk=pk)
        
        context = {
            'pk': pedido.pk,
            'itens': pedido.itens,
            'preco': pedido.price
        }

        return render(request, 'cliente/confirmar_pedido.html',context)
        
    def post(self, request, pk, *args, **kwargs):
        data = json.loads(request.body)
        if data['pago']:
            pedido = ModeloPedido.objects.get(pk=pk)
            pedido.pago = True
            pedido.save()
        return redirect(confirmar-pagamento)
        
class ConfirmarPagamento(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'cliente/confirmacao_pagamento.html')
        
class Menu(View):
    def get(self,request, *args, **kwargs):
        itens_de_menu = ItemDeMenu.objects.all()
        
        context = {
            'itens_de_menu': itens_de_menu
        }
        
        return render (request,'cliente/menu.html', context)
        
class BuscaMenu(View):
    def get(self, request, *args, **kwargs):
        query = self.request.GET.get("q")
        
        itens_de_menu = ItemDeMenu.objects.filter(
            Q(nome__icontains=query) | 
            Q(preco__icontains=query) | 
            Q(descricao__icontains=query)
        )
        
        context = {
            'itens_de_menu': itens_de_menu
        }
        
        return render(request,'cliente/menu.html', context)