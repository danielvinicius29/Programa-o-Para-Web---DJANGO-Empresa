from django.db import models

class NotasFiscai(models.Model):
    Numero_NFE = models.CharField(max_length=100)
    Nome_Emissor = models.CharField(max_length=100)
    Emissor_CNPJ = models.CharField(max_length=18)
    Nome_Destinatario = models.CharField(max_length=100)
    Destinatario_CPF_ou_CNPJ = models.CharField(max_length=18)
    Produto = models.CharField(max_length=100)
    Valor = models.SmallIntegerField()
    

    def __str__(self):
        return self.Numero_NFE
