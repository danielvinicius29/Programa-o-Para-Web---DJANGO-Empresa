# Generated by Django 4.0.4 on 2022-06-08 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0002_produto_codigo_do_produto_produto_estoque_atual_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='produto',
            old_name='preco',
            new_name='preco_de_compra',
        ),
        migrations.AddField(
            model_name='produto',
            name='preco_de_venda',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
