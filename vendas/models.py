from django.db import models
from django.contrib.auth.models import User

class Vendas(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    ano_exercicio = models.PositiveSmallIntegerField()
    carteira_de_clientes_ativa = models.FloatField()
    novos_clientes_no_ano = models.FloatField()
    propostas_enviadas_no_ano = models.FloatField()
    propostas_aprovadas_no_ano = models.FloatField ()
    notas_fiscais_emitidas = models.FloatField(default=1.0)
    clientes_fidelizados = models.FloatField()
    reclamacoes_clientes = models.FloatField()
    clientes_perdidos = models.FloatField()

    class Meta:
        verbose_name = 'Analise de Vendas'
        verbose_name_plural = 'Analises de Vendas'
        # Um usuário não pode ter 2 dres do mesmo ano
        unique_together = (("user", "ano_exercicio"),)

    def __str__(self):
        return 'Painel_desempenho_vendas' + str(self.ano_exercicio)

class AvaliacaoVendas(models.Model):
    SMILE_CHOICES = (
        ('Ruim', 'Ruim'),
        ('Bom', 'Bom'),
        ('Neutro', 'Neutro')
    )
    vendas = models.OneToOneField(Vendas, on_delete=models.CASCADE)
    carteira_de_clientes_ativa = models.CharField(max_length=6, choices=SMILE_CHOICES, default='Neutro')
    novos_clientes_no_ano = models.CharField(max_length=6, choices=SMILE_CHOICES, default='Neutro')
    propostas_enviadas_no_ano = models.CharField(max_length=6, choices=SMILE_CHOICES, default='Neutro')
    propostas_aprovadas_no_ano = models.CharField(max_length=6, choices=SMILE_CHOICES, default='Neutro')
    notas_fiscais_emitidas = models.CharField(max_length=6, choices=SMILE_CHOICES, default='Neutro')
    clientes_fidelizados = models.CharField(max_length=6, choices=SMILE_CHOICES, default='Neutro')
    reclamacoes_clientes = models.CharField(max_length=6, choices=SMILE_CHOICES, default='Neutro')
    clientes_perdidos = models.CharField(max_length=6, choices=SMILE_CHOICES, default='Neutro')

    class Meta:
        verbose_name = 'Avaliação da Analise de Vendas'
        verbose_name_plural = 'Avaliações das Analises de Vendas'

    def __str__(self):
        return 'Avaliação - Painel_desempenho_vendas' + str(self.vendas.ano_exercicio)
