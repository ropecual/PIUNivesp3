from django.contrib import admin
from .models import Cliente, Material, Servico

admin.site.register(Cliente)
admin.site.register(Material)
admin.site.register(Servico)