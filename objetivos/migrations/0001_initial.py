# Generated by Django 2.1.7 on 2019-04-08 02:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dre', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnaliseObjetivoEndividamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('smile_divida', models.CharField(choices=[('Ruim', 'Ruim'), ('Bom', 'Bom'), ('Neutro', 'Neutro')], default='Neutro', max_length=6)),
                ('smile_taxa_divida_lucro', models.CharField(choices=[('Ruim', 'Ruim'), ('Bom', 'Bom'), ('Neutro', 'Neutro')], default='Neutro', max_length=6)),
                ('smile_inadimplencia', models.CharField(choices=[('Ruim', 'Ruim'), ('Bom', 'Bom'), ('Neutro', 'Neutro')], default='Neutro', max_length=6)),
            ],
            options={
                'verbose_name': 'Análise de Objetivo de Endividamento',
                'verbose_name_plural': 'Análises de Objetivos de Endividamento',
            },
        ),
        migrations.CreateModel(
            name='AnaliseObjetivoReceitas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('smile_receita_bruta', models.CharField(choices=[('Ruim', 'Ruim'), ('Bom', 'Bom'), ('Neutro', 'Neutro')], default='Neutro', max_length=6)),
                ('smile_crescimento_quatro', models.CharField(choices=[('Ruim', 'Ruim'), ('Bom', 'Bom'), ('Neutro', 'Neutro')], default='Neutro', max_length=6)),
                ('smile_crescimento', models.CharField(choices=[('Ruim', 'Ruim'), ('Bom', 'Bom'), ('Neutro', 'Neutro')], default='Neutro', max_length=6)),
            ],
            options={
                'verbose_name': 'Análise de Objetivo de Receita',
                'verbose_name_plural': 'Análises de Objetivos de Receitas',
            },
        ),
        migrations.CreateModel(
            name='AnaliseObjetivoRentabilidade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('smile_lucro_liquido', models.CharField(choices=[('Ruim', 'Ruim'), ('Bom', 'Bom'), ('Neutro', 'Neutro')], default='Neutro', max_length=6)),
                ('smile_rentabilidade_media', models.CharField(choices=[('Ruim', 'Ruim'), ('Bom', 'Bom'), ('Neutro', 'Neutro')], default='Neutro', max_length=6)),
                ('smile_rentabilidade_ultimo', models.CharField(choices=[('Ruim', 'Ruim'), ('Bom', 'Bom'), ('Neutro', 'Neutro')], default='Neutro', max_length=6)),
                ('smile_rentabilidade_comparada', models.CharField(choices=[('Ruim', 'Ruim'), ('Bom', 'Bom'), ('Neutro', 'Neutro')], default='Neutro', max_length=6)),
                ('smile_ebitda_medio', models.CharField(choices=[('Ruim', 'Ruim'), ('Bom', 'Bom'), ('Neutro', 'Neutro')], default='Neutro', max_length=6)),
                ('smile_ebitda_ultimo', models.CharField(choices=[('Ruim', 'Ruim'), ('Bom', 'Bom'), ('Neutro', 'Neutro')], default='Neutro', max_length=6)),
            ],
            options={
                'verbose_name': 'Análise de Objetivo de Rentabilidade',
                'verbose_name_plural': 'Análises de Objetivos de Rentabilidade',
            },
        ),
        migrations.CreateModel(
            name='ObjetivoCusto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('despesas_com_pessoal', models.FloatField(default=1.0)),
                ('despesas_administrativas', models.FloatField(default=1.0)),
                ('despesas_ocupacao', models.FloatField(default=1.0)),
                ('despesas_logistica', models.FloatField(default=1.0)),
                ('despesas_vendas', models.FloatField(default=1.0)),
                ('despesas_viagens', models.FloatField(default=1.0)),
                ('despesas_servicos_pj', models.FloatField(default=1.0)),
                ('despesas_tributarias', models.FloatField(default=1.0)),
                ('despesas_financeiras', models.FloatField(default=1.0)),
                ('depreciacao_amortizacao', models.FloatField(default=1.0)),
                ('dre_base', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='ojetivocusto', to='dre.Dre')),
            ],
            options={
                'verbose_name': 'Objetivo de Custo',
                'verbose_name_plural': 'Objetivos de Custo',
            },
        ),
        migrations.CreateModel(
            name='ObjetivoCustoMensal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mes', models.IntegerField()),
                ('despesas_com_pessoal', models.FloatField(default=1.0)),
                ('despesas_administrativas', models.FloatField(default=1.0)),
                ('despesas_ocupacao', models.FloatField(default=1.0)),
                ('despesas_logistica', models.FloatField(default=1.0)),
                ('despesas_vendas', models.FloatField(default=1.0)),
                ('despesas_viagens', models.FloatField(default=1.0)),
                ('despesas_servicos_pj', models.FloatField(default=1.0)),
                ('despesas_tributarias', models.FloatField(default=1.0)),
                ('despesas_financeiras', models.FloatField(default=1.0)),
                ('depreciacao_amortizacao', models.FloatField(default=1.0)),
                ('objetivo_custo_base', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='objetivos.ObjetivoCusto')),
            ],
            options={
                'verbose_name': 'Objetivo de Custo Mensal',
                'verbose_name_plural': 'Objetivos de Custo Mensal',
            },
        ),
        migrations.CreateModel(
            name='ObjetivoEndividamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inadimplencia_percentage', models.FloatField(default=1.0)),
                ('divida_percentage', models.FloatField(default=1.0)),
                ('dre_base', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='ojetivoendividamento', to='dre.Dre')),
            ],
            options={
                'verbose_name': 'Objetivo de Endividamento',
                'verbose_name_plural': 'Objetivos de Endividamento',
            },
        ),
        migrations.CreateModel(
            name='ObjetivoReceitas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('percentage', models.FloatField(default=1.0)),
                ('dre_base', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='objetivoreceitas', to='dre.Dre')),
            ],
            options={
                'verbose_name': 'Objetivo de Receita',
                'verbose_name_plural': 'Objetivos de Receitas',
            },
        ),
        migrations.CreateModel(
            name='ObjetivoRentabilidade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rentabilidade_percentage', models.FloatField(default=0.05)),
                ('ebitda_percentage', models.FloatField(default=1.0)),
                ('dre_base', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='ojetivorentabilidade', to='dre.Dre')),
            ],
            options={
                'verbose_name': 'Objetivo de Rentabilidade',
                'verbose_name_plural': 'Objetivos de Rentabilidade',
            },
        ),
        migrations.AddField(
            model_name='analiseobjetivorentabilidade',
            name='objetivo_rentabilidade_base',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='objetivorentabilidade', to='objetivos.ObjetivoRentabilidade'),
        ),
        migrations.AddField(
            model_name='analiseobjetivoreceitas',
            name='objetivo_receitas_base',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='objetivoreceitas', to='objetivos.ObjetivoReceitas'),
        ),
        migrations.AddField(
            model_name='analiseobjetivoendividamento',
            name='objetivo_endividamento_base',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='objetivoendividamento', to='objetivos.ObjetivoEndividamento'),
        ),
    ]
