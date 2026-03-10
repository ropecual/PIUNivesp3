import json

from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from .models import Cliente, Servico


class DashboardView(TemplateView):
	template_name = 'gestao/dashboard.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

		# Dados dos Cards
		context['total_clientes'] = Cliente.objects.count()
		context['total_servicos_pendentes'] = Servico.objects.filter(status='PEND').count()
		context['total_servicos_concluidos'] = Servico.objects.filter(status='CONC').count()

		# --- DADOS PARA O GRÁFICO (Análise de Dados) ---
		labels = ['Pendentes', 'Aprovados', 'Concluídos', 'Cancelados']
		dados = [
			Servico.objects.filter(status='PEND').count(),
			Servico.objects.filter(status='APROV').count(),
			Servico.objects.filter(status='CONC').count(),
			Servico.objects.filter(status='CANC').count(),
		]

		# Convertendo para JSON para o JavaScript conseguir ler no HTML
		context['labels_grafico'] = json.dumps(labels)
		context['dados_grafico'] = json.dumps(dados)

		return context


# CRUD CLIENTES
class ClienteListView(ListView):
	model = Cliente
	template_name = 'gestao/cliente_list.html'
	context_object_name = 'clientes'


class ClienteCreateView(CreateView):
	model = Cliente
	template_name = 'gestao/cliente_form.html'
	fields = ['nome', 'telefone', 'email', 'endereco']
	success_url = reverse_lazy('cliente_list')

class ClienteUpdateView(UpdateView):
	model = Cliente
	template_name = 'gestao/cliente_form.html'  # Reaproveitamos o mesmo HTML do Create!
	fields = ['nome', 'telefone', 'email', 'endereco']
	success_url = reverse_lazy('cliente_list')

class ClienteDeleteView(DeleteView):
	model = Cliente
	template_name = 'gestao/cliente_confirm_delete.html'
	success_url = reverse_lazy('cliente_list')


# CRUD SERVIÇOS
class ServicoListView(ListView):
	model = Servico
	template_name = 'gestao/servico_list.html'
	context_object_name = 'servicos'

class ServicoCreateView(CreateView):
	model = Servico
	template_name = 'gestao/servico_form.html'
	# Campos que vão aparecer no formulário
	fields = ['cliente', 'tipo', 'descricao', 'data_agendada', 'status', 'valor_mao_de_obra']
	success_url = reverse_lazy('servico_list')

class ServicoUpdateView(UpdateView):
	model = Servico
	template_name = 'gestao/servico_form.html'
	fields = ['cliente', 'tipo', 'descricao', 'data_agendada', 'status', 'valor_mao_de_obra']
	success_url = reverse_lazy('servico_list')

class ServicoDeleteView(DeleteView):
	model = Servico
	template_name = 'gestao/servico_confirm_delete.html'
	success_url = reverse_lazy('servico_list')
