from django.db import models

class ItemDeMenu(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='imagens_menu/')
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    categoria = models.ManyToManyField('Categoria',related_name='item')
    quantidade = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return self.nome
        
class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome
        
class ModeloPedido(models.Model):
    data_criado = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=7,decimal_places=2)
    itens = models.ManyToManyField('ItemDeMenu',related_name='pedido',blank=True)
    nome = models.CharField(max_length=50, blank=True)
    email = models.CharField(max_length=50, blank=True)
    qtd = models.PositiveIntegerField(default=1)
    pago = models.BooleanField(default=False)
    retirado = models.BooleanField(default=False)
    
    def __str__ (self):
        return f'Pedido: {self.data_criado.strftime("%b %d %I: %M %p")}'