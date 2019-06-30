from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Questao(models.Model):
    texto = models.TextField()

    class Meta:
        verbose_name = 'Questão do swot'
        verbose_name_plural = 'Questões do swot'

    def __str__(self):
        return 'Questão do swot: {}'.format(self.texto)

class Resposta(models.Model):
    RESPOSTA_CHOICES = (
        ('Sim', 'Sim'),
        ('+/-', '+/-'),
        ('Não', 'Não')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    questao = models.ForeignKey(Questao, on_delete=models.CASCADE, default=1)
    resposta = models.CharField(default='+/-', max_length=3, choices=RESPOSTA_CHOICES)

    class Meta:
        verbose_name = 'Resposta do swot'
        verbose_name_plural = 'Respostas do swot'
        # Um usuário não pode ter 2 repostas para a mesma pergunta
        unique_together = (("user", "questao"),)

    def __str__(self):
        return 'Resposta de {} para a {}'.format(self.user, self.questao)

class Concorrente(models.Model):
    AVALIACAO_CHOICES = (
        ('Sou melhor', 'Sou melhor'),
        ('Sou igual', 'Sou igual'),
        ('Sou inferior', 'Sou inferior')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    concorrente = models.CharField(max_length=64)
    preco = models.CharField(default='Sou igual', max_length=12, choices=AVALIACAO_CHOICES)
    qualidade = models.CharField(default='Sou igual', max_length=12, choices=AVALIACAO_CHOICES)
    entrega = models.CharField(default='Sou igual', max_length=12, choices=AVALIACAO_CHOICES)
    inovacao = models.CharField(default='Sou igual', max_length=12, choices=AVALIACAO_CHOICES)
    portifolio = models.CharField(default='Sou igual', max_length=12, choices=AVALIACAO_CHOICES)

    class Meta:
        verbose_name = 'Concorrente'
        verbose_name_plural = 'Concorrentes'
        # Um usuário não pode ter 2 concorrentes iguais
        unique_together = (("user", "concorrente"),)

    def __str__(self):
        return 'Concorrente {} do {}.'.format(self.concorrente, self.user)

class AnaliseConcorrencia(models.Model):
    SETAS_CHOICE = (
        ('Cima', 'Cima'),
        ('Meio', 'Meio'),
        ('Baixo', 'Baixo')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='analiseconcorrencia')

    # Objetivos
    objetivo_1 = models.CharField(default='Aumento de Receitas', max_length=64, choices=(
        ('Aumento de Receitas', 'Aumento de Receitas'),
        ('Lançar Novos Produto/Serviços', 'Lançar Novos Produto/Serviços'),
        ('Aumentar Fatia de Mercado', 'Aumentar Fatia de Mercado'),
        ('Soluções Customizadas', 'Soluções Customizadas'),
        ('Gerar inovação na empresa', 'Gerar inovação na empresa'),
        ('Oferecer novos produtos', 'Oferecer novos produtos'),
        ('Regularização da empresa', 'Regularização da empresa'),
        ('Melhorar Governança e Compliance', 'Melhorar Governança e Compliance'),
        ('Customização de Produtos e Serviços', 'Customização de Produtos e Serviços'),
        ('Segmentação de Clientes', 'Segmentação de Clientes'),
        ('Atender Público por faixa etária', 'Atender Público por faixa etária'),
        ('Produtos customizados para idosos', 'Produtos customizados para idosos'),
        ('Produtos customizados para jovens', 'Produtos customizados para jovens')
    ))
    objetivo_2 = models.CharField(default='Gerar inovação na empresa', max_length=64, choices=(
        ('Aumento de Receitas', 'Aumento de Receitas'),
        ('Lançar Novos Produto/Serviços', 'Lançar Novos Produto/Serviços'),
        ('Aumentar Fatia de Mercado', 'Aumentar Fatia de Mercado'),
        ('Soluções Customizadas', 'Soluções Customizadas'),
        ('Gerar inovação na empresa', 'Gerar inovação na empresa'),
        ('Oferecer novos produtos', 'Oferecer novos produtos'),
        ('Regularização da empresa', 'Regularização da empresa'),
        ('Melhorar Governança e Compliance', 'Melhorar Governança e Compliance'),
        ('Customização de Produtos e Serviços', 'Customização de Produtos e Serviços'),
        ('Segmentação de Clientes', 'Segmentação de Clientes'),
        ('Atender Público por faixa etária', 'Atender Público por faixa etária'),
        ('Produtos customizados para idosos', 'Produtos customizados para idosos'),
        ('Produtos customizados para jovens', 'Produtos customizados para jovens')
    ))
    objetivo_3 = models.CharField(default='Regularização da empresa', max_length=64, choices=(
        ('Aumento de Receitas', 'Aumento de Receitas'),
        ('Lançar Novos Produto/Serviços', 'Lançar Novos Produto/Serviços'),
        ('Aumentar Fatia de Mercado', 'Aumentar Fatia de Mercado'),
        ('Soluções Customizadas', 'Soluções Customizadas'),
        ('Gerar inovação na empresa', 'Gerar inovação na empresa'),
        ('Oferecer novos produtos', 'Oferecer novos produtos'),
        ('Regularização da empresa', 'Regularização da empresa'),
        ('Melhorar Governança e Compliance', 'Melhorar Governança e Compliance'),
        ('Customização de Produtos e Serviços', 'Customização de Produtos e Serviços'),
        ('Segmentação de Clientes', 'Segmentação de Clientes'),
        ('Atender Público por faixa etária', 'Atender Público por faixa etária'),
        ('Produtos customizados para idosos', 'Produtos customizados para idosos'),
        ('Produtos customizados para jovens', 'Produtos customizados para jovens')
    ))
    objetivo_4 = models.CharField(default='Customização de Produtos e Serviços', max_length=64, choices=(
        ('Aumento de Receitas', 'Aumento de Receitas'),
        ('Lançar Novos Produto/Serviços', 'Lançar Novos Produto/Serviços'),
        ('Aumentar Fatia de Mercado', 'Aumentar Fatia de Mercado'),
        ('Soluções Customizadas', 'Soluções Customizadas'),
        ('Gerar inovação na empresa', 'Gerar inovação na empresa'),
        ('Oferecer novos produtos', 'Oferecer novos produtos'),
        ('Regularização da empresa', 'Regularização da empresa'),
        ('Melhorar Governança e Compliance', 'Melhorar Governança e Compliance'),
        ('Customização de Produtos e Serviços', 'Customização de Produtos e Serviços'),
        ('Segmentação de Clientes', 'Segmentação de Clientes'),
        ('Atender Público por faixa etária', 'Atender Público por faixa etária'),
        ('Produtos customizados para idosos', 'Produtos customizados para idosos'),
        ('Produtos customizados para jovens', 'Produtos customizados para jovens')
    ))
    objetivo_5 = models.CharField(default='Atender Público por faixa etária', max_length=64, choices=(
        ('Aumento de Receitas', 'Aumento de Receitas'),
        ('Lançar Novos Produto/Serviços', 'Lançar Novos Produto/Serviços'),
        ('Aumentar Fatia de Mercado', 'Aumentar Fatia de Mercado'),
        ('Soluções Customizadas', 'Soluções Customizadas'),
        ('Gerar inovação na empresa', 'Gerar inovação na empresa'),
        ('Oferecer novos produtos', 'Oferecer novos produtos'),
        ('Regularização da empresa', 'Regularização da empresa'),
        ('Melhorar Governança e Compliance', 'Melhorar Governança e Compliance'),
        ('Customização de Produtos e Serviços', 'Customização de Produtos e Serviços'),
        ('Segmentação de Clientes', 'Segmentação de Clientes'),
        ('Atender Público por faixa etária', 'Atender Público por faixa etária'),
        ('Produtos customizados para idosos', 'Produtos customizados para idosos'),
        ('Produtos customizados para jovens', 'Produtos customizados para jovens')
    ))

    objetivo_1_atratividade = models.CharField(default='Meio', max_length=5, choices=SETAS_CHOICE)
    objetivo_1_probabilidade = models.CharField(default='Meio', max_length=5, choices=SETAS_CHOICE)
    objetivo_2_atratividade = models.CharField(default='Meio', max_length=5, choices=SETAS_CHOICE)
    objetivo_2_probabilidade = models.CharField(default='Meio', max_length=5, choices=SETAS_CHOICE)
    objetivo_3_atratividade = models.CharField(default='Meio', max_length=5, choices=SETAS_CHOICE)
    objetivo_3_probabilidade = models.CharField(default='Meio', max_length=5, choices=SETAS_CHOICE)
    objetivo_4_atratividade = models.CharField(default='Meio', max_length=5, choices=SETAS_CHOICE)
    objetivo_4_probabilidade = models.CharField(default='Meio', max_length=5, choices=SETAS_CHOICE)
    objetivo_5_atratividade = models.CharField(default='Meio', max_length=5, choices=SETAS_CHOICE)
    objetivo_5_probabilidade = models.CharField(default='Meio', max_length=5, choices=SETAS_CHOICE)

    # Ameaças
    ameaca_1 = models.CharField(default='Aumento de Receitas', max_length=64, choices=(
        ('Necessidade de Investimentos', 'Necessidade de Investimentos'),
        ('Aumento da Concorrencia', 'Aumento da Concorrencia'),
        ('Aumento de Custos', 'Aumento de Custos'),
        ('Necessidade de Investimentos', 'Necessidade de Investimentos'),
        ('Obsolecencia de Produtos/Serviços', 'Obsolecencia de Produtos/Serviços'),
        ('Multas', 'Multas'),
        ('Perda de Mercado', 'Perda de Mercado'),
        ('Obsolescência de Produtos/Serviços', 'Obsolescência de Produtos/Serviços'),
        ('Perda de Clientes', 'Perda de Clientes'),
        ('Perda de mercado', 'Perda de mercado'),
        ('Obsolescência de Produtos/Serviços', 'Obsolescência de Produtos/Serviços')
    ))

    ameaca_2 = models.CharField(default='Aumento de Receitas', max_length=64, choices=(
        ('Necessidade de Investimentos', 'Necessidade de Investimentos'),
        ('Aumento da Concorrencia', 'Aumento da Concorrencia'),
        ('Aumento de Custos', 'Aumento de Custos'),
        ('Necessidade de Investimentos', 'Necessidade de Investimentos'),
        ('Obsolecencia de Produtos/Serviços', 'Obsolecencia de Produtos/Serviços'),
        ('Multas', 'Multas'),
        ('Perda de Mercado', 'Perda de Mercado'),
        ('Obsolescência de Produtos/Serviços', 'Obsolescência de Produtos/Serviços'),
        ('Perda de Clientes', 'Perda de Clientes'),
        ('Perda de mercado', 'Perda de mercado'),
        ('Obsolescência de Produtos/Serviços', 'Obsolescência de Produtos/Serviços')
    ))

    ameaca_3 = models.CharField(default='Aumento de Receitas', max_length=64, choices=(
        ('Necessidade de Investimentos', 'Necessidade de Investimentos'),
        ('Aumento da Concorrencia', 'Aumento da Concorrencia'),
        ('Aumento de Custos', 'Aumento de Custos'),
        ('Necessidade de Investimentos', 'Necessidade de Investimentos'),
        ('Obsolecencia de Produtos/Serviços', 'Obsolecencia de Produtos/Serviços'),
        ('Multas', 'Multas'),
        ('Perda de Mercado', 'Perda de Mercado'),
        ('Obsolescência de Produtos/Serviços', 'Obsolescência de Produtos/Serviços'),
        ('Perda de Clientes', 'Perda de Clientes'),
        ('Perda de mercado', 'Perda de mercado'),
        ('Obsolescência de Produtos/Serviços', 'Obsolescência de Produtos/Serviços')
    ))

    ameaca_4 = models.CharField(default='Aumento de Receitas', max_length=64, choices=(
        ('Necessidade de Investimentos', 'Necessidade de Investimentos'),
        ('Aumento da Concorrencia', 'Aumento da Concorrencia'),
        ('Aumento de Custos', 'Aumento de Custos'),
        ('Necessidade de Investimentos', 'Necessidade de Investimentos'),
        ('Obsolecencia de Produtos/Serviços', 'Obsolecencia de Produtos/Serviços'),
        ('Multas', 'Multas'),
        ('Perda de Mercado', 'Perda de Mercado'),
        ('Obsolescência de Produtos/Serviços', 'Obsolescência de Produtos/Serviços'),
        ('Perda de Clientes', 'Perda de Clientes'),
        ('Perda de mercado', 'Perda de mercado'),
        ('Obsolescência de Produtos/Serviços', 'Obsolescência de Produtos/Serviços')
    ))

    ameaca_5 = models.CharField(default='Aumento de Receitas', max_length=64, choices=(
        ('Necessidade de Investimentos', 'Necessidade de Investimentos'),
        ('Aumento da Concorrencia', 'Aumento da Concorrencia'),
        ('Aumento de Custos', 'Aumento de Custos'),
        ('Necessidade de Investimentos', 'Necessidade de Investimentos'),
        ('Obsolecencia de Produtos/Serviços', 'Obsolecencia de Produtos/Serviços'),
        ('Multas', 'Multas'),
        ('Perda de Mercado', 'Perda de Mercado'),
        ('Obsolescência de Produtos/Serviços', 'Obsolescência de Produtos/Serviços'),
        ('Perda de Clientes', 'Perda de Clientes'),
        ('Perda de mercado', 'Perda de mercado'),
        ('Obsolescência de Produtos/Serviços', 'Obsolescência de Produtos/Serviços')
    ))

    ameaca_1_relevancia = models.CharField(default='Meio', max_length=5, choices=SETAS_CHOICE)
    ameaca_1_probabilidade = models.CharField(default='Meio', max_length=5, choices=SETAS_CHOICE)
    ameaca_2_relevancia = models.CharField(default='Meio', max_length=5, choices=SETAS_CHOICE)
    ameaca_2_probabilidade = models.CharField(default='Meio', max_length=5, choices=SETAS_CHOICE)
    ameaca_3_relevancia = models.CharField(default='Meio', max_length=5, choices=SETAS_CHOICE)
    ameaca_3_probabilidade = models.CharField(default='Meio', max_length=5, choices=SETAS_CHOICE)
    ameaca_4_relevancia = models.CharField(default='Meio', max_length=5, choices=SETAS_CHOICE)
    ameaca_4_probabilidade = models.CharField(default='Meio', max_length=5, choices=SETAS_CHOICE)
    ameaca_5_relevancia = models.CharField(default='Meio', max_length=5, choices=SETAS_CHOICE)
    ameaca_5_probabilidade = models.CharField(default='Meio', max_length=5, choices=SETAS_CHOICE)

    class Meta:
        verbose_name = 'Análise da concorrência'
        verbose_name_plural = 'Análises da concorrência'

    def __str__(self):
        return 'Análise da concorrência de {}.'.format(self.user)


# CLIENTES #

class Cliente(models.Model):
    AVALIACAO_CHOICES = (
        ('Eu Encanto', 'Eu Encanto'),
        ('Eu Atendo', 'Eu Atendo'),
        ('Eu Decepciono', 'Eu Decepciono')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    clientes = models.CharField(max_length=64)
    preco = models.CharField(default='Eu Atendo', max_length=12, choices=AVALIACAO_CHOICES)
    qualidade = models.CharField(default='Eu Atendo', max_length=12, choices=AVALIACAO_CHOICES)
    entrega = models.CharField(default='Eu Atendo', max_length=12, choices=AVALIACAO_CHOICES)
    inovacao = models.CharField(default='Eu Atendo', max_length=12, choices=AVALIACAO_CHOICES)
    portifolio = models.CharField(default='Eu Atendo', max_length=12, choices=AVALIACAO_CHOICES)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        # Um usuário não pode ter 2 concorrentes iguais
        #unique_together = (("user", "Cliente"),)

    def __str__(self):
        return 'Cliente {} do {}.'.format(self.clientes, self.user)

class AnaliseClientes(models.Model):
    SETAS_CHOICE = (
        ('Cima', 'Cima'),
        ('Meio', 'Meio'),
        ('Baixo', 'Baixo')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='analiseclientes')

    # Objetivos
    objetivo_1 = models.CharField(default='Aumento de Receitas', max_length=64, choices=(
        ('Aumento de Receitas', 'Aumento de Receitas'),
        ('Lançar Novos Produto/Serviços', 'Lançar Novos Produto/Serviços'),
        ('Aumentar Fatia de Mercado', 'Aumentar Fatia de Mercado'),
        ('Soluções Customizadas', 'Soluções Customizadas'),
        ('Gerar inovação na empresa', 'Gerar inovação na empresa'),
        ('Oferecer novos produtos', 'Oferecer novos produtos'),
        ('Regularização da empresa', 'Regularização da empresa'),
        ('Melhorar Governança e Compliance', 'Melhorar Governança e Compliance'),
        ('Customização de Produtos e Serviços', 'Customização de Produtos e Serviços'),
        ('Segmentação de Clientes', 'Segmentação de Clientes'),
        ('Atender Público por faixa etária', 'Atender Público por faixa etária'),
        ('Produtos customizados para idosos', 'Produtos customizados para idosos'),
        ('Produtos customizados para jovens', 'Produtos customizados para jovens')
    ))
    objetivo_2 = models.CharField(default='Gerar inovação na empresa', max_length=64, choices=(
        ('Aumento de Receitas', 'Aumento de Receitas'),
        ('Lançar Novos Produto/Serviços', 'Lançar Novos Produto/Serviços'),
        ('Aumentar Fatia de Mercado', 'Aumentar Fatia de Mercado'),
        ('Soluções Customizadas', 'Soluções Customizadas'),
        ('Gerar inovação na empresa', 'Gerar inovação na empresa'),
        ('Oferecer novos produtos', 'Oferecer novos produtos'),
        ('Regularização da empresa', 'Regularização da empresa'),
        ('Melhorar Governança e Compliance', 'Melhorar Governança e Compliance'),
        ('Customização de Produtos e Serviços', 'Customização de Produtos e Serviços'),
        ('Segmentação de Clientes', 'Segmentação de Clientes'),
        ('Atender Público por faixa etária', 'Atender Público por faixa etária'),
        ('Produtos customizados para idosos', 'Produtos customizados para idosos'),
        ('Produtos customizados para jovens', 'Produtos customizados para jovens')
    ))
    objetivo_3 = models.CharField(default='Regularização da empresa', max_length=64, choices=(
        ('Aumento de Receitas', 'Aumento de Receitas'),
        ('Lançar Novos Produto/Serviços', 'Lançar Novos Produto/Serviços'),
        ('Aumentar Fatia de Mercado', 'Aumentar Fatia de Mercado'),
        ('Soluções Customizadas', 'Soluções Customizadas'),
        ('Gerar inovação na empresa', 'Gerar inovação na empresa'),
        ('Oferecer novos produtos', 'Oferecer novos produtos'),
        ('Regularização da empresa', 'Regularização da empresa'),
        ('Melhorar Governança e Compliance', 'Melhorar Governança e Compliance'),
        ('Customização de Produtos e Serviços', 'Customização de Produtos e Serviços'),
        ('Segmentação de Clientes', 'Segmentação de Clientes'),
        ('Atender Público por faixa etária', 'Atender Público por faixa etária'),
        ('Produtos customizados para idosos', 'Produtos customizados para idosos'),
        ('Produtos customizados para jovens', 'Produtos customizados para jovens')
    ))
    objetivo_4 = models.CharField(default='Customização de Produtos e Serviços', max_length=64, choices=(
        ('Aumento de Receitas', 'Aumento de Receitas'),
        ('Lançar Novos Produto/Serviços', 'Lançar Novos Produto/Serviços'),
        ('Aumentar Fatia de Mercado', 'Aumentar Fatia de Mercado'),
        ('Soluções Customizadas', 'Soluções Customizadas'),
        ('Gerar inovação na empresa', 'Gerar inovação na empresa'),
        ('Oferecer novos produtos', 'Oferecer novos produtos'),
        ('Regularização da empresa', 'Regularização da empresa'),
        ('Melhorar Governança e Compliance', 'Melhorar Governança e Compliance'),
        ('Customização de Produtos e Serviços', 'Customização de Produtos e Serviços'),
        ('Segmentação de Clientes', 'Segmentação de Clientes'),
        ('Atender Público por faixa etária', 'Atender Público por faixa etária'),
        ('Produtos customizados para idosos', 'Produtos customizados para idosos'),
        ('Produtos customizados para jovens', 'Produtos customizados para jovens')
    ))
    objetivo_5 = models.CharField(default='Atender Público por faixa etária', max_length=64, choices=(
        ('Aumento de Receitas', 'Aumento de Receitas'),
        ('Lançar Novos Produto/Serviços', 'Lançar Novos Produto/Serviços'),
        ('Aumentar Fatia de Mercado', 'Aumentar Fatia de Mercado'),
        ('Soluções Customizadas', 'Soluções Customizadas'),
        ('Gerar inovação na empresa', 'Gerar inovação na empresa'),
        ('Oferecer novos produtos', 'Oferecer novos produtos'),
        ('Regularização da empresa', 'Regularização da empresa'),
        ('Melhorar Governança e Compliance', 'Melhorar Governança e Compliance'),
        ('Customização de Produtos e Serviços', 'Customização de Produtos e Serviços'),
        ('Segmentação de Clientes', 'Segmentação de Clientes'),
        ('Atender Público por faixa etária', 'Atender Público por faixa etária'),
        ('Produtos customizados para idosos', 'Produtos customizados para idosos'),
        ('Produtos customizados para jovens', 'Produtos customizados para jovens')
    ))

    objetivo_1_atratividade = models.CharField(default='Meio', max_length=5, choices=SETAS_CHOICE)
    objetivo_1_probabilidade = models.CharField(default='Meio', max_length=5, choices=SETAS_CHOICE)
    objetivo_2_atratividade = models.CharField(default='Meio', max_length=5, choices=SETAS_CHOICE)
    objetivo_2_probabilidade = models.CharField(default='Meio', max_length=5, choices=SETAS_CHOICE)
    objetivo_3_atratividade = models.CharField(default='Meio', max_length=5, choices=SETAS_CHOICE)
    objetivo_3_probabilidade = models.CharField(default='Meio', max_length=5, choices=SETAS_CHOICE)
    objetivo_4_atratividade = models.CharField(default='Meio', max_length=5, choices=SETAS_CHOICE)
    objetivo_4_probabilidade = models.CharField(default='Meio', max_length=5, choices=SETAS_CHOICE)
    objetivo_5_atratividade = models.CharField(default='Meio', max_length=5, choices=SETAS_CHOICE)
    objetivo_5_probabilidade = models.CharField(default='Meio', max_length=5, choices=SETAS_CHOICE)

    # Ameaças
    ameaca_1 = models.CharField(default='Aumento de Receitas', max_length=64, choices=(
        ('Necessidade de Investimentos', 'Necessidade de Investimentos'),
        ('Aumento da Concorrencia', 'Aumento da Concorrencia'),
        ('Aumento de Custos', 'Aumento de Custos'),
        ('Necessidade de Investimentos', 'Necessidade de Investimentos'),
        ('Obsolecencia de Produtos/Serviços', 'Obsolecencia de Produtos/Serviços'),
        ('Multas', 'Multas'),
        ('Perda de Mercado', 'Perda de Mercado'),
        ('Obsolescência de Produtos/Serviços', 'Obsolescência de Produtos/Serviços'),
        ('Perda de Clientes', 'Perda de Clientes'),
        ('Perda de mercado', 'Perda de mercado'),
        ('Obsolescência de Produtos/Serviços', 'Obsolescência de Produtos/Serviços')
    ))

    ameaca_2 = models.CharField(default='Aumento de Receitas', max_length=64, choices=(
        ('Necessidade de Investimentos', 'Necessidade de Investimentos'),
        ('Aumento da Concorrencia', 'Aumento da Concorrencia'),
        ('Aumento de Custos', 'Aumento de Custos'),
        ('Necessidade de Investimentos', 'Necessidade de Investimentos'),
        ('Obsolecencia de Produtos/Serviços', 'Obsolecencia de Produtos/Serviços'),
        ('Multas', 'Multas'),
        ('Perda de Mercado', 'Perda de Mercado'),
        ('Obsolescência de Produtos/Serviços', 'Obsolescência de Produtos/Serviços'),
        ('Perda de Clientes', 'Perda de Clientes'),
        ('Perda de mercado', 'Perda de mercado'),
        ('Obsolescência de Produtos/Serviços', 'Obsolescência de Produtos/Serviços')
    ))

    ameaca_3 = models.CharField(default='Aumento de Receitas', max_length=64, choices=(
        ('Necessidade de Investimentos', 'Necessidade de Investimentos'),
        ('Aumento da Concorrencia', 'Aumento da Concorrencia'),
        ('Aumento de Custos', 'Aumento de Custos'),
        ('Necessidade de Investimentos', 'Necessidade de Investimentos'),
        ('Obsolecencia de Produtos/Serviços', 'Obsolecencia de Produtos/Serviços'),
        ('Multas', 'Multas'),
        ('Perda de Mercado', 'Perda de Mercado'),
        ('Obsolescência de Produtos/Serviços', 'Obsolescência de Produtos/Serviços'),
        ('Perda de Clientes', 'Perda de Clientes'),
        ('Perda de mercado', 'Perda de mercado'),
        ('Obsolescência de Produtos/Serviços', 'Obsolescência de Produtos/Serviços')
    ))

    ameaca_4 = models.CharField(default='Aumento de Receitas', max_length=64, choices=(
        ('Necessidade de Investimentos', 'Necessidade de Investimentos'),
        ('Aumento da Concorrencia', 'Aumento da Concorrencia'),
        ('Aumento de Custos', 'Aumento de Custos'),
        ('Necessidade de Investimentos', 'Necessidade de Investimentos'),
        ('Obsolecencia de Produtos/Serviços', 'Obsolecencia de Produtos/Serviços'),
        ('Multas', 'Multas'),
        ('Perda de Mercado', 'Perda de Mercado'),
        ('Obsolescência de Produtos/Serviços', 'Obsolescência de Produtos/Serviços'),
        ('Perda de Clientes', 'Perda de Clientes'),
        ('Perda de mercado', 'Perda de mercado'),
        ('Obsolescência de Produtos/Serviços', 'Obsolescência de Produtos/Serviços')
    ))

    ameaca_5 = models.CharField(default='Aumento de Receitas', max_length=64, choices=(
        ('Necessidade de Investimentos', 'Necessidade de Investimentos'),
        ('Aumento da Concorrencia', 'Aumento da Concorrencia'),
        ('Aumento de Custos', 'Aumento de Custos'),
        ('Necessidade de Investimentos', 'Necessidade de Investimentos'),
        ('Obsolecencia de Produtos/Serviços', 'Obsolecencia de Produtos/Serviços'),
        ('Multas', 'Multas'),
        ('Perda de Mercado', 'Perda de Mercado'),
        ('Obsolescência de Produtos/Serviços', 'Obsolescência de Produtos/Serviços'),
        ('Perda de Clientes', 'Perda de Clientes'),
        ('Perda de mercado', 'Perda de mercado'),
        ('Obsolescência de Produtos/Serviços', 'Obsolescência de Produtos/Serviços')
    ))

    ameaca_1_relevancia = models.CharField(default='Meio', max_length=5, choices=SETAS_CHOICE)
    ameaca_1_probabilidade = models.CharField(default='Meio', max_length=5, choices=SETAS_CHOICE)
    ameaca_2_relevancia = models.CharField(default='Meio', max_length=5, choices=SETAS_CHOICE)
    ameaca_2_probabilidade = models.CharField(default='Meio', max_length=5, choices=SETAS_CHOICE)
    ameaca_3_relevancia = models.CharField(default='Meio', max_length=5, choices=SETAS_CHOICE)
    ameaca_3_probabilidade = models.CharField(default='Meio', max_length=5, choices=SETAS_CHOICE)
    ameaca_4_relevancia = models.CharField(default='Meio', max_length=5, choices=SETAS_CHOICE)
    ameaca_4_probabilidade = models.CharField(default='Meio', max_length=5, choices=SETAS_CHOICE)
    ameaca_5_relevancia = models.CharField(default='Meio', max_length=5, choices=SETAS_CHOICE)
    ameaca_5_probabilidade = models.CharField(default='Meio', max_length=5, choices=SETAS_CHOICE)

    class Meta:
        verbose_name = 'Análise da clientes'
        verbose_name_plural = 'Análises da clientes'

    def __str__(self):
        return 'Análise de clientes de {}.'.format(self.user)

#FORNECEDORES#

class Fornecedor(models.Model):
    AVALIACAO_CHOICES = (
        ('Me Encanta', 'Me Encanta'),
        ('Me Atende', 'Me Atende'),
        ('Me Decepciona', 'Me Decepciona')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    fornecedor = models.CharField(max_length=64)
    preco = models.CharField(default='Me Atende', max_length=12, choices=AVALIACAO_CHOICES)
    qualidade = models.CharField(default='Me Atende', max_length=12, choices=AVALIACAO_CHOICES)
    entrega = models.CharField(default='Me Atende', max_length=12, choices=AVALIACAO_CHOICES)
    inovacao = models.CharField(default='Me Atende', max_length=12, choices=AVALIACAO_CHOICES)
    portifolio = models.CharField(default='Me Atende', max_length=12, choices=AVALIACAO_CHOICES)

    class Meta:
        verbose_name = 'Fornecedor'
        verbose_name_plural = 'Fornecedores'
        # Um usuário não pode ter 2 concorrentes iguais
        #unique_together = (("user", "cliente"),)

    def __str__(self):
        return 'Fornecedores {} do {}.'.format(self.fornecedor, self.user)

class AnaliseFornecedores(models.Model):
    SETAS_CHOICE = (
        ('Cima', 'Cima'),
        ('Meio', 'Meio'),
        ('Baixo', 'Baixo')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='analisefornecedores')

    # Objetivos
    objetivo_1 = models.CharField(default='Aumento de Receitas', max_length=64, choices=(
        ('Aumento de Receitas', 'Aumento de Receitas'),
        ('Lançar Novos Produto/Serviços', 'Lançar Novos Produto/Serviços'),
        ('Aumentar Fatia de Mercado', 'Aumentar Fatia de Mercado'),
        ('Soluções Customizadas', 'Soluções Customizadas'),
        ('Gerar inovação na empresa', 'Gerar inovação na empresa'),
        ('Oferecer novos produtos', 'Oferecer novos produtos'),
        ('Regularização da empresa', 'Regularização da empresa'),
        ('Melhorar Governança e Compliance', 'Melhorar Governança e Compliance'),
        ('Customização de Produtos e Serviços', 'Customização de Produtos e Serviços'),
        ('Segmentação de Clientes', 'Segmentação de Clientes'),
        ('Atender Público por faixa etária', 'Atender Público por faixa etária'),
        ('Produtos customizados para idosos', 'Produtos customizados para idosos'),
        ('Produtos customizados para jovens', 'Produtos customizados para jovens')
    ))
    objetivo_2 = models.CharField(default='Gerar inovação na empresa', max_length=64, choices=(
        ('Aumento de Receitas', 'Aumento de Receitas'),
        ('Lançar Novos Produto/Serviços', 'Lançar Novos Produto/Serviços'),
        ('Aumentar Fatia de Mercado', 'Aumentar Fatia de Mercado'),
        ('Soluções Customizadas', 'Soluções Customizadas'),
        ('Gerar inovação na empresa', 'Gerar inovação na empresa'),
        ('Oferecer novos produtos', 'Oferecer novos produtos'),
        ('Regularização da empresa', 'Regularização da empresa'),
        ('Melhorar Governança e Compliance', 'Melhorar Governança e Compliance'),
        ('Customização de Produtos e Serviços', 'Customização de Produtos e Serviços'),
        ('Segmentação de Clientes', 'Segmentação de Clientes'),
        ('Atender Público por faixa etária', 'Atender Público por faixa etária'),
        ('Produtos customizados para idosos', 'Produtos customizados para idosos'),
        ('Produtos customizados para jovens', 'Produtos customizados para jovens')
    ))
    objetivo_3 = models.CharField(default='Regularização da empresa', max_length=64, choices=(
        ('Aumento de Receitas', 'Aumento de Receitas'),
        ('Lançar Novos Produto/Serviços', 'Lançar Novos Produto/Serviços'),
        ('Aumentar Fatia de Mercado', 'Aumentar Fatia de Mercado'),
        ('Soluções Customizadas', 'Soluções Customizadas'),
        ('Gerar inovação na empresa', 'Gerar inovação na empresa'),
        ('Oferecer novos produtos', 'Oferecer novos produtos'),
        ('Regularização da empresa', 'Regularização da empresa'),
        ('Melhorar Governança e Compliance', 'Melhorar Governança e Compliance'),
        ('Customização de Produtos e Serviços', 'Customização de Produtos e Serviços'),
        ('Segmentação de Clientes', 'Segmentação de Clientes'),
        ('Atender Público por faixa etária', 'Atender Público por faixa etária'),
        ('Produtos customizados para idosos', 'Produtos customizados para idosos'),
        ('Produtos customizados para jovens', 'Produtos customizados para jovens')
    ))
    objetivo_4 = models.CharField(default='Customização de Produtos e Serviços', max_length=64, choices=(
        ('Aumento de Receitas', 'Aumento de Receitas'),
        ('Lançar Novos Produto/Serviços', 'Lançar Novos Produto/Serviços'),
        ('Aumentar Fatia de Mercado', 'Aumentar Fatia de Mercado'),
        ('Soluções Customizadas', 'Soluções Customizadas'),
        ('Gerar inovação na empresa', 'Gerar inovação na empresa'),
        ('Oferecer novos produtos', 'Oferecer novos produtos'),
        ('Regularização da empresa', 'Regularização da empresa'),
        ('Melhorar Governança e Compliance', 'Melhorar Governança e Compliance'),
        ('Customização de Produtos e Serviços', 'Customização de Produtos e Serviços'),
        ('Segmentação de Clientes', 'Segmentação de Clientes'),
        ('Atender Público por faixa etária', 'Atender Público por faixa etária'),
        ('Produtos customizados para idosos', 'Produtos customizados para idosos'),
        ('Produtos customizados para jovens', 'Produtos customizados para jovens')
    ))
    objetivo_5 = models.CharField(default='Atender Público por faixa etária', max_length=64, choices=(
        ('Aumento de Receitas', 'Aumento de Receitas'),
        ('Lançar Novos Produto/Serviços', 'Lançar Novos Produto/Serviços'),
        ('Aumentar Fatia de Mercado', 'Aumentar Fatia de Mercado'),
        ('Soluções Customizadas', 'Soluções Customizadas'),
        ('Gerar inovação na empresa', 'Gerar inovação na empresa'),
        ('Oferecer novos produtos', 'Oferecer novos produtos'),
        ('Regularização da empresa', 'Regularização da empresa'),
        ('Melhorar Governança e Compliance', 'Melhorar Governança e Compliance'),
        ('Customização de Produtos e Serviços', 'Customização de Produtos e Serviços'),
        ('Segmentação de Clientes', 'Segmentação de Clientes'),
        ('Atender Público por faixa etária', 'Atender Público por faixa etária'),
        ('Produtos customizados para idosos', 'Produtos customizados para idosos'),
        ('Produtos customizados para jovens', 'Produtos customizados para jovens')
    ))

    objetivo_1_atratividade = models.CharField(default='Meio', max_length=5, choices=SETAS_CHOICE)
    objetivo_1_probabilidade = models.CharField(default='Meio', max_length=5, choices=SETAS_CHOICE)
    objetivo_2_atratividade = models.CharField(default='Meio', max_length=5, choices=SETAS_CHOICE)
    objetivo_2_probabilidade = models.CharField(default='Meio', max_length=5, choices=SETAS_CHOICE)
    objetivo_3_atratividade = models.CharField(default='Meio', max_length=5, choices=SETAS_CHOICE)
    objetivo_3_probabilidade = models.CharField(default='Meio', max_length=5, choices=SETAS_CHOICE)
    objetivo_4_atratividade = models.CharField(default='Meio', max_length=5, choices=SETAS_CHOICE)
    objetivo_4_probabilidade = models.CharField(default='Meio', max_length=5, choices=SETAS_CHOICE)
    objetivo_5_atratividade = models.CharField(default='Meio', max_length=5, choices=SETAS_CHOICE)
    objetivo_5_probabilidade = models.CharField(default='Meio', max_length=5, choices=SETAS_CHOICE)

    # Ameaças
    ameaca_1 = models.CharField(default='Aumento de Receitas', max_length=64, choices=(
        ('Necessidade de Investimentos', 'Necessidade de Investimentos'),
        ('Aumento da Concorrencia', 'Aumento da Concorrencia'),
        ('Aumento de Custos', 'Aumento de Custos'),
        ('Necessidade de Investimentos', 'Necessidade de Investimentos'),
        ('Obsolecencia de Produtos/Serviços', 'Obsolecencia de Produtos/Serviços'),
        ('Multas', 'Multas'),
        ('Perda de Mercado', 'Perda de Mercado'),
        ('Obsolescência de Produtos/Serviços', 'Obsolescência de Produtos/Serviços'),
        ('Perda de Clientes', 'Perda de Clientes'),
        ('Perda de mercado', 'Perda de mercado'),
        ('Obsolescência de Produtos/Serviços', 'Obsolescência de Produtos/Serviços')
    ))

    ameaca_2 = models.CharField(default='Aumento de Receitas', max_length=64, choices=(
        ('Necessidade de Investimentos', 'Necessidade de Investimentos'),
        ('Aumento da Concorrencia', 'Aumento da Concorrencia'),
        ('Aumento de Custos', 'Aumento de Custos'),
        ('Necessidade de Investimentos', 'Necessidade de Investimentos'),
        ('Obsolecencia de Produtos/Serviços', 'Obsolecencia de Produtos/Serviços'),
        ('Multas', 'Multas'),
        ('Perda de Mercado', 'Perda de Mercado'),
        ('Obsolescência de Produtos/Serviços', 'Obsolescência de Produtos/Serviços'),
        ('Perda de Clientes', 'Perda de Clientes'),
        ('Perda de mercado', 'Perda de mercado'),
        ('Obsolescência de Produtos/Serviços', 'Obsolescência de Produtos/Serviços')
    ))

    ameaca_3 = models.CharField(default='Aumento de Receitas', max_length=64, choices=(
        ('Necessidade de Investimentos', 'Necessidade de Investimentos'),
        ('Aumento da Concorrencia', 'Aumento da Concorrencia'),
        ('Aumento de Custos', 'Aumento de Custos'),
        ('Necessidade de Investimentos', 'Necessidade de Investimentos'),
        ('Obsolecencia de Produtos/Serviços', 'Obsolecencia de Produtos/Serviços'),
        ('Multas', 'Multas'),
        ('Perda de Mercado', 'Perda de Mercado'),
        ('Obsolescência de Produtos/Serviços', 'Obsolescência de Produtos/Serviços'),
        ('Perda de Clientes', 'Perda de Clientes'),
        ('Perda de mercado', 'Perda de mercado'),
        ('Obsolescência de Produtos/Serviços', 'Obsolescência de Produtos/Serviços')
    ))

    ameaca_4 = models.CharField(default='Aumento de Receitas', max_length=64, choices=(
        ('Necessidade de Investimentos', 'Necessidade de Investimentos'),
        ('Aumento da Concorrencia', 'Aumento da Concorrencia'),
        ('Aumento de Custos', 'Aumento de Custos'),
        ('Necessidade de Investimentos', 'Necessidade de Investimentos'),
        ('Obsolecencia de Produtos/Serviços', 'Obsolecencia de Produtos/Serviços'),
        ('Multas', 'Multas'),
        ('Perda de Mercado', 'Perda de Mercado'),
        ('Obsolescência de Produtos/Serviços', 'Obsolescência de Produtos/Serviços'),
        ('Perda de Clientes', 'Perda de Clientes'),
        ('Perda de mercado', 'Perda de mercado'),
        ('Obsolescência de Produtos/Serviços', 'Obsolescência de Produtos/Serviços')
    ))

    ameaca_5 = models.CharField(default='Aumento de Receitas', max_length=64, choices=(
        ('Necessidade de Investimentos', 'Necessidade de Investimentos'),
        ('Aumento da Concorrencia', 'Aumento da Concorrencia'),
        ('Aumento de Custos', 'Aumento de Custos'),
        ('Necessidade de Investimentos', 'Necessidade de Investimentos'),
        ('Obsolecencia de Produtos/Serviços', 'Obsolecencia de Produtos/Serviços'),
        ('Multas', 'Multas'),
        ('Perda de Mercado', 'Perda de Mercado'),
        ('Obsolescência de Produtos/Serviços', 'Obsolescência de Produtos/Serviços'),
        ('Perda de Clientes', 'Perda de Clientes'),
        ('Perda de mercado', 'Perda de mercado'),
        ('Obsolescência de Produtos/Serviços', 'Obsolescência de Produtos/Serviços')
    ))

    ameaca_1_relevancia = models.CharField(default='Meio', max_length=5, choices=SETAS_CHOICE)
    ameaca_1_probabilidade = models.CharField(default='Meio', max_length=5, choices=SETAS_CHOICE)
    ameaca_2_relevancia = models.CharField(default='Meio', max_length=5, choices=SETAS_CHOICE)
    ameaca_2_probabilidade = models.CharField(default='Meio', max_length=5, choices=SETAS_CHOICE)
    ameaca_3_relevancia = models.CharField(default='Meio', max_length=5, choices=SETAS_CHOICE)
    ameaca_3_probabilidade = models.CharField(default='Meio', max_length=5, choices=SETAS_CHOICE)
    ameaca_4_relevancia = models.CharField(default='Meio', max_length=5, choices=SETAS_CHOICE)
    ameaca_4_probabilidade = models.CharField(default='Meio', max_length=5, choices=SETAS_CHOICE)
    ameaca_5_relevancia = models.CharField(default='Meio', max_length=5, choices=SETAS_CHOICE)
    ameaca_5_probabilidade = models.CharField(default='Meio', max_length=5, choices=SETAS_CHOICE)

    class Meta:
        verbose_name = 'Análise de fornecedor'
        verbose_name_plural = 'Análises de fornecedores'

    def __str__(self):
        return 'Análise de fornecedores de {}.'.format(self.user)

    #MACRO#

class Macro ( models.Model ):
    AVALIACAO_CHOICES = (
        ('Me Encanta', 'Me Encanta'),
        ('Me Atende', 'Me Atende'),
        ('Me Decepciona', 'Me Decepciona')
    )
    user = models.ForeignKey ( User, on_delete=models.CASCADE, default=1 )
    macro = models.CharField ( max_length=64 )
    preco = models.CharField ( default='Me Atende', max_length=12, choices=AVALIACAO_CHOICES )
    qualidade = models.CharField ( default='Me Atende', max_length=12, choices=AVALIACAO_CHOICES )
    entrega = models.CharField ( default='Me Atende', max_length=12, choices=AVALIACAO_CHOICES )
    inovacao = models.CharField ( default='Me Atende', max_length=12, choices=AVALIACAO_CHOICES )
    portifolio = models.CharField ( default='Me Atende', max_length=12, choices=AVALIACAO_CHOICES )

    class Meta:
        verbose_name = 'Macro'
        verbose_name_plural = 'Macros'
        # Um usuário não pode ter 2 concorrentes iguais
        # unique_together = (("user", "cliente"),)

    def __str__(self):
        return 'Macros {} do {}.'.format ( self.macro, self.user )


class AnalisesMacro ( models.Model ):
    SETAS_CHOICE = (
        ('Cima', 'Cima'),
        ('Meio', 'Meio'),
        ('Baixo', 'Baixo')
    )
    user = models.OneToOneField ( User, on_delete=models.CASCADE, related_name='analisesmacro' )

    # Objetivos
    objetivo_1 = models.CharField ( default='Aumento de Receitas', max_length=64, choices=(
        ('Aumento de Receitas', 'Aumento de Receitas'),
        ('Lançar Novos Produto/Serviços', 'Lançar Novos Produto/Serviços'),
        ('Aumentar Fatia de Mercado', 'Aumentar Fatia de Mercado'),
        ('Soluções Customizadas', 'Soluções Customizadas'),
        ('Gerar inovação na empresa', 'Gerar inovação na empresa'),
        ('Oferecer novos produtos', 'Oferecer novos produtos'),
        ('Regularização da empresa', 'Regularização da empresa'),
        ('Melhorar Governança e Compliance', 'Melhorar Governança e Compliance'),
        ('Customização de Produtos e Serviços', 'Customização de Produtos e Serviços'),
        ('Segmentação de Clientes', 'Segmentação de Clientes'),
        ('Atender Público por faixa etária', 'Atender Público por faixa etária'),
        ('Produtos customizados para idosos', 'Produtos customizados para idosos'),
        ('Produtos customizados para jovens', 'Produtos customizados para jovens')
    ) )
    objetivo_2 = models.CharField ( default='Gerar inovação na empresa', max_length=64, choices=(
        ('Aumento de Receitas', 'Aumento de Receitas'),
        ('Lançar Novos Produto/Serviços', 'Lançar Novos Produto/Serviços'),
        ('Aumentar Fatia de Mercado', 'Aumentar Fatia de Mercado'),
        ('Soluções Customizadas', 'Soluções Customizadas'),
        ('Gerar inovação na empresa', 'Gerar inovação na empresa'),
        ('Oferecer novos produtos', 'Oferecer novos produtos'),
        ('Regularização da empresa', 'Regularização da empresa'),
        ('Melhorar Governança e Compliance', 'Melhorar Governança e Compliance'),
        ('Customização de Produtos e Serviços', 'Customização de Produtos e Serviços'),
        ('Segmentação de Clientes', 'Segmentação de Clientes'),
        ('Atender Público por faixa etária', 'Atender Público por faixa etária'),
        ('Produtos customizados para idosos', 'Produtos customizados para idosos'),
        ('Produtos customizados para jovens', 'Produtos customizados para jovens')
    ) )
    objetivo_3 = models.CharField ( default='Regularização da empresa', max_length=64, choices=(
        ('Aumento de Receitas', 'Aumento de Receitas'),
        ('Lançar Novos Produto/Serviços', 'Lançar Novos Produto/Serviços'),
        ('Aumentar Fatia de Mercado', 'Aumentar Fatia de Mercado'),
        ('Soluções Customizadas', 'Soluções Customizadas'),
        ('Gerar inovação na empresa', 'Gerar inovação na empresa'),
        ('Oferecer novos produtos', 'Oferecer novos produtos'),
        ('Regularização da empresa', 'Regularização da empresa'),
        ('Melhorar Governança e Compliance', 'Melhorar Governança e Compliance'),
        ('Customização de Produtos e Serviços', 'Customização de Produtos e Serviços'),
        ('Segmentação de Clientes', 'Segmentação de Clientes'),
        ('Atender Público por faixa etária', 'Atender Público por faixa etária'),
        ('Produtos customizados para idosos', 'Produtos customizados para idosos'),
        ('Produtos customizados para jovens', 'Produtos customizados para jovens')
    ) )
    objetivo_4 = models.CharField ( default='Customização de Produtos e Serviços', max_length=64, choices=(
        ('Aumento de Receitas', 'Aumento de Receitas'),
        ('Lançar Novos Produto/Serviços', 'Lançar Novos Produto/Serviços'),
        ('Aumentar Fatia de Mercado', 'Aumentar Fatia de Mercado'),
        ('Soluções Customizadas', 'Soluções Customizadas'),
        ('Gerar inovação na empresa', 'Gerar inovação na empresa'),
        ('Oferecer novos produtos', 'Oferecer novos produtos'),
        ('Regularização da empresa', 'Regularização da empresa'),
        ('Melhorar Governança e Compliance', 'Melhorar Governança e Compliance'),
        ('Customização de Produtos e Serviços', 'Customização de Produtos e Serviços'),
        ('Segmentação de Clientes', 'Segmentação de Clientes'),
        ('Atender Público por faixa etária', 'Atender Público por faixa etária'),
        ('Produtos customizados para idosos', 'Produtos customizados para idosos'),
        ('Produtos customizados para jovens', 'Produtos customizados para jovens')
    ) )
    objetivo_5 = models.CharField ( default='Atender Público por faixa etária', max_length=64, choices=(
        ('Aumento de Receitas', 'Aumento de Receitas'),
        ('Lançar Novos Produto/Serviços', 'Lançar Novos Produto/Serviços'),
        ('Aumentar Fatia de Mercado', 'Aumentar Fatia de Mercado'),
        ('Soluções Customizadas', 'Soluções Customizadas'),
        ('Gerar inovação na empresa', 'Gerar inovação na empresa'),
        ('Oferecer novos produtos', 'Oferecer novos produtos'),
        ('Regularização da empresa', 'Regularização da empresa'),
        ('Melhorar Governança e Compliance', 'Melhorar Governança e Compliance'),
        ('Customização de Produtos e Serviços', 'Customização de Produtos e Serviços'),
        ('Segmentação de Clientes', 'Segmentação de Clientes'),
        ('Atender Público por faixa etária', 'Atender Público por faixa etária'),
        ('Produtos customizados para idosos', 'Produtos customizados para idosos'),
        ('Produtos customizados para jovens', 'Produtos customizados para jovens')
    ) )

    objetivo_1_atratividade = models.CharField ( default='Meio', max_length=5, choices=SETAS_CHOICE )
    objetivo_1_probabilidade = models.CharField ( default='Meio', max_length=5, choices=SETAS_CHOICE )
    objetivo_2_atratividade = models.CharField ( default='Meio', max_length=5, choices=SETAS_CHOICE )
    objetivo_2_probabilidade = models.CharField ( default='Meio', max_length=5, choices=SETAS_CHOICE )
    objetivo_3_atratividade = models.CharField ( default='Meio', max_length=5, choices=SETAS_CHOICE )
    objetivo_3_probabilidade = models.CharField ( default='Meio', max_length=5, choices=SETAS_CHOICE )
    objetivo_4_atratividade = models.CharField ( default='Meio', max_length=5, choices=SETAS_CHOICE )
    objetivo_4_probabilidade = models.CharField ( default='Meio', max_length=5, choices=SETAS_CHOICE )
    objetivo_5_atratividade = models.CharField ( default='Meio', max_length=5, choices=SETAS_CHOICE )
    objetivo_5_probabilidade = models.CharField ( default='Meio', max_length=5, choices=SETAS_CHOICE )

    # Ameaças
    ameaca_1 = models.CharField ( default='Aumento de Receitas', max_length=64, choices=(
        ('Necessidade de Investimentos', 'Necessidade de Investimentos'),
        ('Aumento da Concorrencia', 'Aumento da Concorrencia'),
        ('Aumento de Custos', 'Aumento de Custos'),
        ('Necessidade de Investimentos', 'Necessidade de Investimentos'),
        ('Obsolecencia de Produtos/Serviços', 'Obsolecencia de Produtos/Serviços'),
        ('Multas', 'Multas'),
        ('Perda de Mercado', 'Perda de Mercado'),
        ('Obsolescência de Produtos/Serviços', 'Obsolescência de Produtos/Serviços'),
        ('Perda de Clientes', 'Perda de Clientes'),
        ('Perda de mercado', 'Perda de mercado'),
        ('Obsolescência de Produtos/Serviços', 'Obsolescência de Produtos/Serviços')
    ) )

    ameaca_2 = models.CharField ( default='Aumento de Receitas', max_length=64, choices=(
        ('Necessidade de Investimentos', 'Necessidade de Investimentos'),
        ('Aumento da Concorrencia', 'Aumento da Concorrencia'),
        ('Aumento de Custos', 'Aumento de Custos'),
        ('Necessidade de Investimentos', 'Necessidade de Investimentos'),
        ('Obsolecencia de Produtos/Serviços', 'Obsolecencia de Produtos/Serviços'),
        ('Multas', 'Multas'),
        ('Perda de Mercado', 'Perda de Mercado'),
        ('Obsolescência de Produtos/Serviços', 'Obsolescência de Produtos/Serviços'),
        ('Perda de Clientes', 'Perda de Clientes'),
        ('Perda de mercado', 'Perda de mercado'),
        ('Obsolescência de Produtos/Serviços', 'Obsolescência de Produtos/Serviços')
    ) )

    ameaca_3 = models.CharField ( default='Aumento de Receitas', max_length=64, choices=(
        ('Necessidade de Investimentos', 'Necessidade de Investimentos'),
        ('Aumento da Concorrencia', 'Aumento da Concorrencia'),
        ('Aumento de Custos', 'Aumento de Custos'),
        ('Necessidade de Investimentos', 'Necessidade de Investimentos'),
        ('Obsolecencia de Produtos/Serviços', 'Obsolecencia de Produtos/Serviços'),
        ('Multas', 'Multas'),
        ('Perda de Mercado', 'Perda de Mercado'),
        ('Obsolescência de Produtos/Serviços', 'Obsolescência de Produtos/Serviços'),
        ('Perda de Clientes', 'Perda de Clientes'),
        ('Perda de mercado', 'Perda de mercado'),
        ('Obsolescência de Produtos/Serviços', 'Obsolescência de Produtos/Serviços')
    ) )

    ameaca_4 = models.CharField ( default='Aumento de Receitas', max_length=64, choices=(
        ('Necessidade de Investimentos', 'Necessidade de Investimentos'),
        ('Aumento da Concorrencia', 'Aumento da Concorrencia'),
        ('Aumento de Custos', 'Aumento de Custos'),
        ('Necessidade de Investimentos', 'Necessidade de Investimentos'),
        ('Obsolecencia de Produtos/Serviços', 'Obsolecencia de Produtos/Serviços'),
        ('Multas', 'Multas'),
        ('Perda de Mercado', 'Perda de Mercado'),
        ('Obsolescência de Produtos/Serviços', 'Obsolescência de Produtos/Serviços'),
        ('Perda de Clientes', 'Perda de Clientes'),
        ('Perda de mercado', 'Perda de mercado'),
        ('Obsolescência de Produtos/Serviços', 'Obsolescência de Produtos/Serviços')
    ) )

    ameaca_5 = models.CharField ( default='Aumento de Receitas', max_length=64, choices=(
        ('Necessidade de Investimentos', 'Necessidade de Investimentos'),
        ('Aumento da Concorrencia', 'Aumento da Concorrencia'),
        ('Aumento de Custos', 'Aumento de Custos'),
        ('Necessidade de Investimentos', 'Necessidade de Investimentos'),
        ('Obsolecencia de Produtos/Serviços', 'Obsolecencia de Produtos/Serviços'),
        ('Multas', 'Multas'),
        ('Perda de Mercado', 'Perda de Mercado'),
        ('Obsolescência de Produtos/Serviços', 'Obsolescência de Produtos/Serviços'),
        ('Perda de Clientes', 'Perda de Clientes'),
        ('Perda de mercado', 'Perda de mercado'),
        ('Obsolescência de Produtos/Serviços', 'Obsolescência de Produtos/Serviços')
    ) )

    ameaca_1_relevancia = models.CharField ( default='Meio', max_length=5, choices=SETAS_CHOICE )
    ameaca_1_probabilidade = models.CharField ( default='Meio', max_length=5, choices=SETAS_CHOICE )
    ameaca_2_relevancia = models.CharField ( default='Meio', max_length=5, choices=SETAS_CHOICE )
    ameaca_2_probabilidade = models.CharField ( default='Meio', max_length=5, choices=SETAS_CHOICE )
    ameaca_3_relevancia = models.CharField ( default='Meio', max_length=5, choices=SETAS_CHOICE )
    ameaca_3_probabilidade = models.CharField ( default='Meio', max_length=5, choices=SETAS_CHOICE )
    ameaca_4_relevancia = models.CharField ( default='Meio', max_length=5, choices=SETAS_CHOICE )
    ameaca_4_probabilidade = models.CharField ( default='Meio', max_length=5, choices=SETAS_CHOICE )
    ameaca_5_relevancia = models.CharField ( default='Meio', max_length=5, choices=SETAS_CHOICE )
    ameaca_5_probabilidade = models.CharField ( default='Meio', max_length=5, choices=SETAS_CHOICE )

    class Meta:
        verbose_name = 'Análise de macro'
        verbose_name_plural = 'Análises de macro'

    def __str__(self):
        return 'Análise de macro de {}.'.format ( self.user )

