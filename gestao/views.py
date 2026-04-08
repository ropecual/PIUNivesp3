import json

from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.db import transaction, models
from django.db.models import Count, Q, Sum
from django.forms import inlineformset_factory
from .models import Cliente, Servico, Material, ServicoMaterial
from .forms import ServicoForm


class DashboardView(LoginRequiredMixin, TemplateView):
	template_name = 'gestao/dashboard.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

		contagens = Servico.objects.aggregate(
			pendentes=Count('id', filter=Q(status='PEND')),
			aprovados=Count('id', filter=Q(status='APROV')),
			concluidos=Count('id', filter=Q(status='CONC')),
			cancelados=Count('id', filter=Q(status='CANC')),
			receita_mao_obra=Sum('valor_mao_de_obra', filter=Q(status='CONC'))
		)

		materiais_custo = ServicoMaterial.objects.filter(servico__status='CONC').aggregate(
			total=Sum(models.F('quantidade') * models.F('material__custo_unitario'))
		)['total'] or 0

		receita_mao_obra = contagens['receita_mao_obra'] or 0

		# Dados dos Cards
		context['total_clientes'] = Cliente.objects.count()
		context['total_servicos_pendentes'] = contagens['pendentes']
		context['total_servicos_concluidos'] = contagens['concluidos']
		
		context['receita_total'] = receita_mao_obra + materiais_custo
		context['custo_materiais'] = materiais_custo

		# --- DADOS PARA O GRÁFICO (Análise de Dados) ---
		labels = ['Pendentes', 'Aprovados', 'Concluídos', 'Cancelados']
		dados = [
			contagens['pendentes'],
			contagens['aprovados'],
			contagens['concluidos'],
			contagens['cancelados'],
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


ServicoMaterialFormSet = inlineformset_factory(
	Servico, ServicoMaterial, fields=('material', 'quantidade'), extra=1, can_delete=True
)

class ServicoCreateView(LoginRequiredMixin, CreateView):
	model = Servico
	template_name = 'gestao/servico_form.html'
	form_class = ServicoForm
	success_url = reverse_lazy('servico_list')

	def get_context_data(self, **kwargs):
		data = super().get_context_data(**kwargs)
		if self.request.POST:
			data['materiais'] = ServicoMaterialFormSet(self.request.POST)
		else:
			data['materiais'] = ServicoMaterialFormSet()
		return data

	def form_valid(self, form):
		context = self.get_context_data()
		materiais = context['materiais']
		with transaction.atomic():
			self.object = form.save()
			if materiais.is_valid():
				materiais.instance = self.object
				materiais.save()
		return super().form_valid(form)


class ServicoUpdateView(LoginRequiredMixin, UpdateView):
	model = Servico
	template_name = 'gestao/servico_form.html'
	form_class = ServicoForm
	success_url = reverse_lazy('servico_list')

	def get_context_data(self, **kwargs):
		data = super().get_context_data(**kwargs)
		if self.request.POST:
			data['materiais'] = ServicoMaterialFormSet(self.request.POST, instance=self.object)
		else:
			data['materiais'] = ServicoMaterialFormSet(instance=self.object)
		return data

	def form_valid(self, form):
		context = self.get_context_data()
		materiais = context['materiais']
		with transaction.atomic():
			self.object = form.save()
			if materiais.is_valid():
				materiais.instance = self.object
				materiais.save()
		return super().form_valid(form)


class ServicoDeleteView(LoginRequiredMixin, DeleteView):
	model = Servico
	template_name = 'gestao/servico_confirm_delete.html'
	success_url = reverse_lazy('servico_list')


class ServicoConcluirView(LoginRequiredMixin, View):
	def post(self, request, pk):
		servico = get_object_or_404(Servico, pk=pk)
		if servico.status != 'CONC':
			servico.status = 'CONC'
			servico.save()
		return redirect('servico_list')


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
