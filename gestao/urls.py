from django.urls import path
from .views import DashboardView, ClienteListView, ClienteCreateView

urlpatterns = [
	# A rota vazia '' agora chama a Classe DashboardView
	path('', DashboardView.as_view(), name='dashboard'),
	path('clientes/', ClienteListView.as_view(), name='cliente_list'),
	path('clientes/novo/', ClienteCreateView.as_view(), name='cliente_novo'),
]
