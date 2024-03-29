# Generated by Django 2.1.7 on 2019-04-15 07:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vendas',
            old_name='contatos_proativos',
            new_name='carteira_de_clientes_ativa',
        ),
        migrations.RenameField(
            model_name='vendas',
            old_name='assertividade_de_propostas',
            new_name='notas_fiscais_emitidas',
        ),
        migrations.RenameField(
            model_name='vendas',
            old_name='fatia_de_mercado',
            new_name='propostas_enviadas_no_ano',
        ),
        migrations.RemoveField(
            model_name='vendas',
            name='aumento_de_vendas',
        ),
        migrations.RemoveField(
            model_name='vendas',
            name='clientes_potenciais',
        ),
        migrations.RemoveField(
            model_name='vendas',
            name='market_share',
        ),
        migrations.RemoveField(
            model_name='vendas',
            name='nivel_de_satisfacao',
        ),
        migrations.RemoveField(
            model_name='vendas',
            name='novos_clientes',
        ),
        migrations.RemoveField(
            model_name='vendas',
            name='propostas_enviadas',
        ),
        migrations.RemoveField(
            model_name='vendas',
            name='qtd_produtos_servicos_vendidos',
        ),
        migrations.RemoveField(
            model_name='vendas',
            name='reclamacoes_no_ano',
        ),
        migrations.RemoveField(
            model_name='vendas',
            name='reclamacoes_qtd_vendida',
        ),
        migrations.RemoveField(
            model_name='vendas',
            name='retencao_de_clientes',
        ),
        migrations.RemoveField(
            model_name='vendas',
            name='satisfacao_do_cliente',
        ),
        migrations.RemoveField(
            model_name='vendas',
            name='ticket_medio',
        ),
    ]
