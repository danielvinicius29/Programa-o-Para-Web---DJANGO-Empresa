# Generated by Django 4.0.4 on 2022-06-08 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='codigo_do_produto',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='produto',
            name='estoque_atual',
            field=models.SmallIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='produto',
            name='preco',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
