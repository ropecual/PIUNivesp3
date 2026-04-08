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

	@property
	def custo_materiais(self):
		return sum(sm.quantidade * sm.material.custo_unitario for sm in self.materiais_usados.all())

	@property
	def valor_total(self):
		return self.valor_mao_de_obra + self.custo_materiais

	def save(self, *args, **kwargs):
		if self.pk:
			try:
				old_instance = Servico.objects.get(pk=self.pk)
				old_status = old_instance.status
				# Deduce only when changing TO CONC. 
				# If it goes back from CONC to other status, we should probably restock, but we'll stick to simple deduction on first CONC state.
				if old_status != 'CONC' and self.status == 'CONC':
					for sm in self.materiais_usados.all():
						m = sm.material
						m.estoque_atual -= sm.quantidade
						m.save(update_fields=['estoque_atual'])
			except Servico.DoesNotExist:
				pass
		super().save(*args, **kwargs)


class ServicoMaterial(models.Model):
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE, related_name='materiais_usados')
    material = models.ForeignKey(Material, on_delete=models.PROTECT)
    quantidade = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantidade}x {self.material.nome} no Serv {self.servico.id}"

    @property
    def custo_total(self):
        return self.quantidade * self.material.custo_unitario