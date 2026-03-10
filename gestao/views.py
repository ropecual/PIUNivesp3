from django.views.generic import TemplateView
from .models import Cliente, Servico


class DashboardView(TemplateView):
	template_name = 'gestao/dashboard.html'

	def get_context_data(self, **kwargs):
		# Pega o contexto padrão da classe pai
		context = super().get_context_data(**kwargs)

		# Aqui fazemos a "Análise de Dados" básica para o Dashboard
		context['total_clientes'] = Cliente.objects.count()
		context['total_servicos_pendentes'] = Servico.objects.filter(status='PEND').count()
		context['total_servicos_concluidos'] = Servico.objects.filter(status='CONC').count()

		return context