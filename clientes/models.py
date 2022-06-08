from django.db import models

class Cliente(models.Model):
    Nome_ou_Razao_Social = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    Cidade = models.CharField(max_length=100)
    Estado = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    Telefone = models.CharField(max_length=11)
    CPF_ou_CNPJ = models.CharField(max_length=18)

    def __str__(self):
        return self.Nome_ou_Razao_Social
