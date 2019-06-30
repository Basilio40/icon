from django.db import models
from django.contrib.auth.models import User

class Dre(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    ano_exercicio = models.PositiveSmallIntegerField()
    receita_servico = models.FloatField()
    receita_produto = models.FloatField()
    outras_receitas = models.FloatField()
    #deducoes_receitas = models.FloatField()
    imposto_sobre_receitas = models.FloatField()
    custo_das_mercadorias_vendidas = models.FloatField(default=1.0)
    custo_dos_produtos_industrializados = models.FloatField(default=1.0)
    #despesas_operacionais = models.FloatField ()
    despesas_com_pessoal = models.FloatField(default=1.0)
    despesas_administrativas = models.FloatField()
    #despesas_comunicacao = models.FloatField()
    despesas_ocupacao = models.FloatField()
    #despesas_escritorio = models.FloatField()
    despesas_logistica = models.FloatField()
    despesas_vendas = models.FloatField()
    despesas_viagens = models.FloatField()
    despesas_servicos_pj = models.FloatField()
    despesas_tributarias = models.FloatField()
    #despesas_folha = models.FloatField()
    receitas_financeiras = models.FloatField(default=1.0)
    despesas_financeiras = models.FloatField(default=1.0)

    alienacao_ativo_fixo = models.FloatField(default=1.0)
    despesas_indedutiveis = models.FloatField(default=1.0)

    irpj_e_csll = models.FloatField(default=1.0)

    depreciacao_amortizacao = models.FloatField()
    equivalente_patrimonial = models.FloatField()
    #despesas_nao_operacionais = models.FloatField()
    restituicao_correcao_monetaria = models.FloatField()
    endividamento = models.FloatField()
    inadimplencia = models.FloatField()

    class Meta:
        verbose_name = 'Demonstração do Resultado do Exercício'
        verbose_name_plural = 'Demonstrações do Resultado do Exercício'
        # Um usuário não pode ter 2 dres do mesmo ano
        unique_together = (("user", "ano_exercicio"),)

    def __str__(self):
        return 'Demonstração do Resultado do Exercício do ano de ' + str(self.ano_exercicio)


