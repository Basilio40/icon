# Generated by Django 2.1.7 on 2019-04-08 02:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Dre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ano_exercicio', models.PositiveSmallIntegerField()),
                ('receita_servico', models.FloatField()),
                ('receita_produto', models.FloatField()),
                ('outras_receitas', models.FloatField()),
                ('imposto_sobre_receitas', models.FloatField()),
                ('custo_das_mercadorias_vendidas', models.FloatField(default=1.0)),
                ('custo_dos_produtos_industrializados', models.FloatField(default=1.0)),
                ('despesas_com_pessoal', models.FloatField(default=1.0)),
                ('despesas_administrativas', models.FloatField()),
                ('despesas_ocupacao', models.FloatField()),
                ('despesas_logistica', models.FloatField()),
                ('despesas_vendas', models.FloatField()),
                ('despesas_viagens', models.FloatField()),
                ('despesas_servicos_pj', models.FloatField()),
                ('despesas_tributarias', models.FloatField()),
                ('receitas_financeiras', models.FloatField(default=1.0)),
                ('despesas_financeiras', models.FloatField(default=1.0)),
                ('alienacao_ativo_fixo', models.FloatField(default=1.0)),
                ('despesas_indedutiveis', models.FloatField(default=1.0)),
                ('irpj_e_csll', models.FloatField(default=1.0)),
                ('depreciacao_amortizacao', models.FloatField()),
                ('equivalente_patrimonial', models.FloatField()),
                ('restituicao_correcao_monetaria', models.FloatField()),
                ('endividamento', models.FloatField()),
                ('inadimplencia', models.FloatField()),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Demonstração do Resultado do Exercício',
                'verbose_name_plural': 'Demonstrações do Resultado do Exercício',
            },
        ),
        migrations.AlterUniqueTogether(
            name='dre',
            unique_together={('user', 'ano_exercicio')},
        ),
    ]