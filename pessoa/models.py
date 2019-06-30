from django.db import models
from django.contrib.auth.models import User

class Pessoas(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    ano_exercicio = models.PositiveSmallIntegerField()
    funcionarios_antigos = models.FloatField()
    rotatividade = models.FloatField()
    absenteismo = models.FloatField()

    class Meta:
        verbose_name = 'Analise de Pessoas'
        verbose_name_plural = 'Analises de Pessoas'
        # Um usuário não pode ter 2 dres do mesmo ano
        unique_together = (("user", "ano_exercicio"),)

    def __str__(self):
        return 'Painel_desempenho_pessoas' + str(self.ano_exercicio)

class AvaliacaoPessoas(models.Model):
    SMILE_CHOICES = (
        ('Ruim', 'Ruim'),
        ('Bom', 'Bom'),
        ('Neutro', 'Neutro')
    )
    pessoas = models.OneToOneField(Pessoas, on_delete=models.CASCADE)
    nivel_competencias = models.CharField(max_length=6, choices=SMILE_CHOICES, default='Neutro')
    funcionarios_antigos = models.CharField(max_length=6, choices=SMILE_CHOICES, default='Neutro')
    rotatividade = models.CharField(max_length=6, choices=SMILE_CHOICES, default='Neutro')
    absenteismo = models.CharField(max_length=6, choices=SMILE_CHOICES, default='Neutro')
    engajamento = models.CharField(max_length=6, choices=SMILE_CHOICES, default='Neutro')
    retencao = models.CharField(max_length=6, choices=SMILE_CHOICES, default='Neutro')


    class Meta:
        verbose_name = 'Avaliação da Analise de Pessoas'
        verbose_name_plural = 'Avaliações das Analises de Pessoas'

    def __str__(self):
        return 'Avaliação - Painel_desempenho_pessoas' + str(self.pessoas.ano_exercicio)



class Competencias(models.Model):
    AVALIACAO_CHOICES = (
        ('Plena', 'Plena'),
        ('Parcial', 'Parcial'),
        ('Deficiente', 'Deficiente')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    competencia = models.CharField(max_length=64)
    categoria = models.CharField(default='Parcial', max_length=12, choices=AVALIACAO_CHOICES)


    class Meta:
        verbose_name = 'Competencia'
        verbose_name_plural = 'Competencias'
        # Um usuário não pode ter 2 concorrentes iguais
        unique_together = (("user", "competencia"),)

    def __str__(self):
        return 'Competencia {} do {}.'.format(self.competencia, self.user)

class Engajamento( models.Model ):
    AVALIACAO_CHOICES = (
        ('Excelente', 'Excelente'),
        ('Bom', 'Bom'),
        ('Baixa', 'Baixa'),
        ('Ruim', 'Ruim')
    )
    user = models.ForeignKey ( User, on_delete=models.CASCADE, default=1 )
    engajamento = models.CharField ( max_length=64 )
    categoria = models.CharField ( default='Baixa', max_length=12, choices=AVALIACAO_CHOICES )

    class Meta:
        verbose_name = 'Engajamento'
        verbose_name_plural = 'Engajamentos'
        # Um usuário não pode ter 2 concorrentes iguais
        unique_together = (("user", "engajamento"),)

    def __str__(self):
        return 'Engajamento {} do {}.'.format (self.engajamento, self.user)

class Retencao( models.Model ):
    AVALIACAO_CHOICES = (
        ('Implantado e Eficaz', 'Implantado e Eficaz'),
        ('Implantado e Parcial', 'Implantado e Parcial'),
        ('Em implantação', 'Em implantação'),
        ('Não implantado', 'Não implantado')
    )
    user = models.ForeignKey ( User, on_delete=models.CASCADE, default=1 )
    retencao = models.CharField ( max_length=64 )
    categoria = models.CharField ( default='Em implantação', max_length=12, choices=AVALIACAO_CHOICES )

    class Meta:
        verbose_name = 'Retencao'
        verbose_name_plural = 'Retencoes'
        # Um usuário não pode ter 2 concorrentes iguais
        unique_together = (("user", "retencao"),)

    def __str__(self):
        return 'Retencao {} do {}.'.format (self.retencao, self.user)