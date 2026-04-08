from django.urls import path
from .views import DashboardView, ClienteListView, ClienteCreateView, ClienteUpdateView, ClienteDeleteView, \
	ServicoListView, ServicoCreateView, ServicoUpdateView, ServicoDeleteView, ServicoConcluirView, \
	MaterialListView, MaterialCreateView, MaterialUpdateView, MaterialDeleteView

urlpatterns = [
	# A rota vazia '' agora chama a Classe DashboardView
	path('', DashboardView.as_view(), name='dashboard'),

	# Clientes
	path('clientes/', ClienteListView.as_view(), name='cliente_list'),
	path('clientes/novo/', ClienteCreateView.as_view(), name='cliente_novo'),
	path('clientes/<int:pk>/editar/', ClienteUpdateView.as_view(), name='cliente_editar'),
	path('clientes/<int:pk>/excluir/', ClienteDeleteView.as_view(), name='cliente_excluir'),

	# Serviços
	path('servicos/', ServicoListView.as_view(), name='servico_list'),
	path('servicos/novo/', ServicoCreateView.as_view(), name='servico_novo'),
	path('servicos/<int:pk>/editar/', ServicoUpdateView.as_view(), name='servico_editar'),
	path('servicos/<int:pk>/excluir/', ServicoDeleteView.as_view(), name='servico_excluir'),
	path('servicos/<int:pk>/concluir/', ServicoConcluirView.as_view(), name='servico_concluir'),

	# Materiais
	path('materiais/', MaterialListView.as_view(), name='material_list'),
	path('materiais/novo/', MaterialCreateView.as_view(), name='material_novo'),
	path('materiais/<int:pk>/editar/', MaterialUpdateView.as_view(), name='material_editar'),
	path('materiais/<int:pk>/excluir/', MaterialDeleteView.as_view(), name='material_excluir'),
]
