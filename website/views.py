from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import ContatoForm
from gestao.models import Cliente

class LandingPageView(CreateView):
    model = Cliente
    form_class = ContatoForm
    template_name = 'website/landing_page.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        messages.success(self.request, 'Sua solicitação foi enviada com sucesso! Entraremos em contato em breve.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Houve um erro no envio. Verifique os dados e tente novamente.')
        return super().form_invalid(form)
