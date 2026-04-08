from django.contrib import admin
from .models import Cliente, Material, Servico, ServicoMaterial

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['nome', 'telefone', 'email', 'data_cadastro']
    search_fields = ['nome', 'telefone', 'email']
    list_filter = ['data_cadastro']

@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ['nome', 'custo_unitario', 'estoque_atual']
    search_fields = ['nome']

class ServicoMaterialInline(admin.TabularInline):
    model = ServicoMaterial
    extra = 1

@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ['id', 'cliente', 'tipo', 'status', 'data_agendada']
    list_filter = ['status', 'tipo', 'data_agendada']
    search_fields = ['cliente__nome', 'descricao']
    inlines = [ServicoMaterialInline]