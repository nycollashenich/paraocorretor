from django.contrib import admin
from .models import Corretor, Imovel

@admin.register(Corretor)
class CorretorAdmin(admin.ModelAdmin):
    list_display = ['nome', 'idade', 'profissao', 'imagem']

@admin.register(Imovel)
class ImovelAdmin(admin.ModelAdmin):
    list_display = ['rua_avenida', 'preco', 'cidade', 'imagem']