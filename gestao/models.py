from django.db import models


class Cliente(models.Model):
	nome = models.CharField(max_length=100)
	telefone = models.CharField(max_length=20, help_text="WhatsApp")
	email = models.EmailField(blank=True, null=True)
	endereco = models.CharField(max_length=200)
	data_cadastro = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.nome


class Material(models.Model):
	nome = models.CharField(max_length=100)
	custo_unitario = models.DecimalField(max_digits=10, decimal_places=2)
	estoque_atual = models.IntegerField(default=0)

	def __str__(self):
		return self.nome


class Servico(models.Model):
	TIPO_CHOICES = [
		('INST', 'Instalação'),
		('HIG', 'Higienização'),
		('MAN', 'Manutenção'),
	]
	STATUS_CHOICES = [
		('PEND', 'Pendente/Orçamento'),
		('APROV', 'Aprovado'),
		('CONC', 'Concluído'),
		('CANC', 'Cancelado'),
	]

	cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
	tipo = models.CharField(max_length=4, choices=TIPO_CHOICES)
	descricao = models.TextField(help_text="Detalhes do serviço ou problema relatado")
	data_agendada = models.DateTimeField(blank=True, null=True)
	status = models.CharField(max_length=5, choices=STATUS_CHOICES, default='PEND')
	valor_mao_de_obra = models.DecimalField(max_digits=10, decimal_places=2, default=0)
	criado_em = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.get_tipo_display()} - {self.cliente.nome}"