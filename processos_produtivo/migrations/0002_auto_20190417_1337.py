# Generated by Django 2.1.7 on 2019-04-17 16:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('processos_produtivo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='avaliacaoprocessos',
            name='reclamacoes_clientes',
        ),
        migrations.RemoveField(
            model_name='processos',
            name='reclamacoes_clientes',
        ),
    ]
