from django import forms
from .models import Servico

class ServicoForm(forms.ModelForm):
    class Meta:
        model = Servico
        fields = ['cliente', 'tipo', 'descricao', 'data_agendada', 'status', 'valor_mao_de_obra']
        widgets = {
            'data_agendada': forms.DateTimeInput(
                attrs={'type': 'datetime-local'},
                format='%Y-%m-%dT%H:%M'
            ),
        }
