import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from .models import Cliente, Servico, Material


class DashboardView(LoginRequiredMixin, TemplateView):
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
class ClienteListView(LoginRequiredMixin, ListView):
	model = Cliente
	template_name = 'gestao/cliente_list.html'
	context_object_name = 'clientes'


class ClienteCreateView(LoginRequiredMixin, CreateView):
	model = Cliente
	template_name = 'gestao/cliente_form.html'
	fields = ['nome', 'telefone', 'email', 'endereco']
	success_url = reverse_lazy('cliente_list')


class ClienteUpdateView(LoginRequiredMixin, UpdateView):
	model = Cliente
	template_name = 'gestao/cliente_form.html'  # Reaproveitamos o mesmo HTML do Create!
	fields = ['nome', 'telefone', 'email', 'endereco']
	success_url = reverse_lazy('cliente_list')


class ClienteDeleteView(LoginRequiredMixin, DeleteView):
	model = Cliente
	template_name = 'gestao/cliente_confirm_delete.html'
	success_url = reverse_lazy('cliente_list')


# CRUD SERVIÇOS
class ServicoListView(LoginRequiredMixin, ListView):
	model = Servico
	template_name = 'gestao/servico_list.html'
	context_object_name = 'servicos'

	def get_queryset(self):
		# Pega a lista padrão com todos os serviços
		queryset = super().get_queryset()

		# Verifica se na URL tem algo como "?status=PEND"
		status_filter = self.request.GET.get('status')
		if status_filter:
			# Filtra a lista pelo status recebido
			queryset = queryset.filter(status=status_filter)

		return queryset


class ServicoCreateView(LoginRequiredMixin, CreateView):
	model = Servico
	template_name = 'gestao/servico_form.html'
	# Campos que vão aparecer no formulário
	fields = ['cliente', 'tipo', 'descricao', 'data_agendada', 'status', 'valor_mao_de_obra']
	success_url = reverse_lazy('servico_list')


class ServicoUpdateView(LoginRequiredMixin, UpdateView):
	model = Servico
	template_name = 'gestao/servico_form.html'
	fields = ['cliente', 'tipo', 'descricao', 'data_agendada', 'status', 'valor_mao_de_obra']
	success_url = reverse_lazy('servico_list')


class ServicoDeleteView(LoginRequiredMixin, DeleteView):
	model = Servico
	template_name = 'gestao/servico_confirm_delete.html'
	success_url = reverse_lazy('servico_list')


# CRUD MATERIAIS
class MaterialListView(LoginRequiredMixin, ListView):
	model = Material
	template_name = 'gestao/material_list.html'
	context_object_name = 'materiais'


class MaterialCreateView(LoginRequiredMixin, CreateView):
	model = Material
	template_name = 'gestao/material_form.html'
	fields = ['nome', 'custo_unitario', 'estoque_atual']
	success_url = reverse_lazy('material_list')


class MaterialUpdateView(LoginRequiredMixin, UpdateView):
	model = Material
	template_name = 'gestao/material_form.html'
	fields = ['nome', 'custo_unitario', 'estoque_atual']
	success_url = reverse_lazy('material_list')


class MaterialDeleteView(LoginRequiredMixin, DeleteView):
	model = Material
	template_name = 'gestao/material_confirm_delete.html'
	success_url = reverse_lazy('material_list')
