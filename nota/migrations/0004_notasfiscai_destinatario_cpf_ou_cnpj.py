# Generated by Django 4.0.4 on 2022-06-08 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nota', '0003_notasfiscai_valor'),
    ]

    operations = [
        migrations.AddField(
            model_name='notasfiscai',
            name='Destinatario_CPF_ou_CNPJ',
            field=models.CharField(default=0, max_length=18),
            preserve_default=False,
        ),
    ]