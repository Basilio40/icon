from django.db import models
from django.contrib.auth.models import User

class Processos(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    ano_exercicio = models.PositiveSmallIntegerField()
    funcionarios = models.FloatField()
    volume_produzido_no_ano = models.FloatField()
    capacidade_produzida = models.FloatField()
    refugo_retrabalho = models.FloatField ()
    custos_garantia = models.FloatField(default=1.0)
    entregas_no_prazo = models.FloatField()
    valor_do_estoque = models.FloatField()

    class Meta:
        verbose_name = 'Analise de Processos'
        verbose_name_plural = 'Analises de Processos'
        # Um usuário não pode ter 2 dres do mesmo ano
        unique_together = (("user", "ano_exercicio"),)

    def __str__(self):
        return 'painel_desempenho_processos_produtivos' + str(self.ano_exercicio)

class AvaliacaoProcessos(models.Model):
    SMILE_CHOICES = (
        ('Ruim', 'Ruim'),
        ('Bom', 'Bom'),
        ('Neutro', 'Neutro')
    )
    processos = models.OneToOneField(Processos, on_delete=models.CASCADE)
    funcionarios = models.CharField(max_length=6, choices=SMILE_CHOICES, default='Neutro')
    volume_produzido_no_ano = models.CharField(max_length=6, choices=SMILE_CHOICES, default='Neutro')
    capacidade_produzida = models.CharField(max_length=6, choices=SMILE_CHOICES, default='Neutro')
    refugo_retrabalho = models.CharField(max_length=6, choices=SMILE_CHOICES, default='Neutro')
    custos_garantia = models.CharField(max_length=6, choices=SMILE_CHOICES, default='Neutro')
    entregas_no_prazo = models.CharField(max_length=6, choices=SMILE_CHOICES, default='Neutro')
    valor_do_estoque = models.CharField(max_length=6, choices=SMILE_CHOICES, default='Neutro')

    class Meta:
        verbose_name = 'Avaliação da Analise de Processos'
        verbose_name_plural = 'Avaliações das Analises de Processos'

    def __str__(self):
        return 'Avaliação - painel_desempenho_processos_produtivos' + str(self.processos.ano_exercicio)

