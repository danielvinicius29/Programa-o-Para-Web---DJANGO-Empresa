# Generated by Django 4.0.4 on 2022-06-08 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nome_ou_Razao_Social', models.CharField(max_length=100)),
                ('endereco', models.CharField(max_length=100)),
                ('Cidade', models.CharField(max_length=100)),
                ('Estado', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('CPF_ou_CNPJ', models.CharField(max_length=18)),
            ],
        ),
    ]
