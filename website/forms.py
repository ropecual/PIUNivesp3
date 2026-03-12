from django import forms
from gestao.models import Cliente

class ContatoForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'telefone', 'email', 'endereco']
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Seu Nome'}),
            'telefone': forms.TextInput(attrs={'placeholder': 'WhatsApp'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Seu Email'}),
            'endereco': forms.TextInput(attrs={'placeholder': 'Endereço'}),
        }
