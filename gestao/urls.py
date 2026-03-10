from django.urls import path
from .views import DashboardView

urlpatterns = [
    # A rota vazia '' agora chama a Classe DashboardView
    path('', DashboardView.as_view(), name='dashboard'),
]