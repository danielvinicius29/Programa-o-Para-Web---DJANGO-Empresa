from django.db import models

class Produto(models.Model):
    nome_do_produto = models.CharField(max_length=100)
    codigo_do_produto = models.CharField(max_length=100)
    preco_de_compra = models.FloatField()
    preco_de_venda = models.FloatField()
    estoque_atual = models.SmallIntegerField()

    def __str__(self):
        return self.nome_do_produto
