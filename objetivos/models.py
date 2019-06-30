from django.db import models

# Create your models here.
class ObjetivoReceitas(models.Model):
    percentage = models.FloatField(default=1.0)
    dre_base = models.OneToOneField('dre.Dre', on_delete=models.CASCADE, related_name='objetivoreceitas')

    class Meta:
        verbose_name = 'Objetivo de Receita'
        verbose_name_plural = 'Objetivos de Receitas'

    def __str__(self):
        return 'Objetivo de receita com base no dre ' + str(self.dre_base)

class AnaliseObjetivoReceitas(models.Model):
    SMILE_CHOICES = (
        ('Ruim', 'Ruim'),
        ('Bom', 'Bom'),
        ('Neutro', 'Neutro')
    )
    objetivo_receitas_base = models.OneToOneField(ObjetivoReceitas, on_delete=models.CASCADE, related_name='objetivoreceitas')
    smile_receita_bruta = models.CharField(max_length=6, choices=SMILE_CHOICES, default='Neutro')
    smile_crescimento_quatro = models.CharField(max_length=6, choices=SMILE_CHOICES, default='Neutro')
    smile_crescimento = models.CharField(max_length=6, choices=SMILE_CHOICES, default='Neutro')

    class Meta:
        verbose_name = 'Análise de Objetivo de Receita'
        verbose_name_plural = 'Análises de Objetivos de Receitas'

    def __str__(self):
        return 'Análise do ' + str(self.objetivo_receitas_base)

class ObjetivoRentabilidade(models.Model):
    rentabilidade_percentage = models.FloatField(default=0.05)
    ebitda_percentage = models.FloatField(default=1.00)
    dre_base = models.OneToOneField('dre.Dre', on_delete=models.CASCADE, related_name='ojetivorentabilidade')

    class Meta:
        verbose_name = 'Objetivo de Rentabilidade'
        verbose_name_plural = 'Objetivos de Rentabilidade'

    def __str__(self):
        return 'Objetivo de rentabilidade com base no dre ' + str(self.dre_base)

class AnaliseObjetivoRentabilidade(models.Model):
    SMILE_CHOICES = (
        ('Ruim', 'Ruim'),
        ('Bom', 'Bom'),
        ('Neutro', 'Neutro')
    )
    objetivo_rentabilidade_base = models.OneToOneField(ObjetivoRentabilidade, on_delete=models.CASCADE, related_name='objetivorentabilidade')
    smile_lucro_liquido = models.CharField(max_length=6, choices=SMILE_CHOICES, default='Neutro')
    smile_rentabilidade_media = models.CharField(max_length=6, choices=SMILE_CHOICES, default='Neutro')
    smile_rentabilidade_ultimo = models.CharField(max_length=6, choices=SMILE_CHOICES, default='Neutro')
    smile_rentabilidade_comparada = models.CharField(max_length=6, choices=SMILE_CHOICES, default='Neutro')
    smile_ebitda_medio = models.CharField(max_length=6, choices=SMILE_CHOICES, default='Neutro')
    smile_ebitda_ultimo = models.CharField(max_length=6, choices=SMILE_CHOICES, default='Neutro')

    class Meta:
        verbose_name = 'Análise de Objetivo de Rentabilidade'
        verbose_name_plural = 'Análises de Objetivos de Rentabilidade'

    def __str__(self):
        return 'Análise do ' + str(self.objetivo_rentabilidade_base)

class ObjetivoEndividamento(models.Model):
    inadimplencia_percentage = models.FloatField(default=1.00)
    divida_percentage = models.FloatField(default=1.00)
    dre_base = models.OneToOneField('dre.Dre', on_delete=models.CASCADE, related_name='ojetivoendividamento')

    class Meta:
        verbose_name = 'Objetivo de Endividamento'
        verbose_name_plural = 'Objetivos de Endividamento'

    def __str__(self):
        return 'Objetivo de endividamento com base no dre ' + str(self.dre_base)

class AnaliseObjetivoEndividamento(models.Model):
    SMILE_CHOICES = (
        ('Ruim', 'Ruim'),
        ('Bom', 'Bom'),
        ('Neutro', 'Neutro')
    )
    objetivo_endividamento_base = models.OneToOneField(ObjetivoEndividamento, on_delete=models.CASCADE, related_name='objetivoendividamento')
    smile_divida = models.CharField(max_length=6, choices=SMILE_CHOICES, default='Neutro')
    smile_taxa_divida_lucro = models.CharField(max_length=6, choices=SMILE_CHOICES, default='Neutro')
    smile_inadimplencia = models.CharField(max_length=6, choices=SMILE_CHOICES, default='Neutro')

    class Meta:
        verbose_name = 'Análise de Objetivo de Endividamento'
        verbose_name_plural = 'Análises de Objetivos de Endividamento'

    def __str__(self):
        return 'Análise do ' + str(self.objetivo_endividamento_base)

class ObjetivoCusto(models.Model):
    dre_base = models.OneToOneField('dre.Dre', on_delete=models.CASCADE, related_name='ojetivocusto')
    despesas_com_pessoal = models.FloatField(default=1.0)
    despesas_administrativas = models.FloatField(default=1.0)
    despesas_ocupacao = models.FloatField(default=1.0)
    despesas_logistica = models.FloatField(default=1.0)
    despesas_vendas = models.FloatField(default=1.0)
    despesas_viagens = models.FloatField(default=1.0)
    despesas_servicos_pj = models.FloatField(default=1.0)
    despesas_tributarias = models.FloatField(default=1.0)
    despesas_financeiras = models.FloatField(default=1.0)
    depreciacao_amortizacao = models.FloatField(default=1.0)
    class Meta:
        verbose_name = 'Objetivo de Custo'
        verbose_name_plural = 'Objetivos de Custo'

    def __str__(self):
        return 'Objetivo de custo com base no dre ' + str(self.dre_base)

class ObjetivoCustoMensal(models.Model):
    objetivo_custo_base = models.ForeignKey(ObjetivoCusto, on_delete=models.CASCADE)
    mes = models.IntegerField()
    despesas_com_pessoal = models.FloatField(default=1.0)
    despesas_administrativas = models.FloatField(default=1.0)
    despesas_ocupacao = models.FloatField(default=1.0)
    despesas_logistica = models.FloatField(default=1.0)
    despesas_vendas = models.FloatField(default=1.0)
    despesas_viagens = models.FloatField(default=1.0)
    despesas_servicos_pj = models.FloatField(default=1.0)
    despesas_tributarias = models.FloatField(default=1.0)
    despesas_financeiras = models.FloatField(default=1.0)
    depreciacao_amortizacao = models.FloatField(default=1.0)
    class Meta:
        verbose_name = 'Objetivo de Custo Mensal'
        verbose_name_plural = 'Objetivos de Custo Mensal'

    def __str__(self):
        return 'Objetivo de custos mensal do mês ' + str(self.mes) + ' do DRE ' + str(self.objetivo_custo_base.dre_base)
