from django.contrib import admin
from .models import Corretor

@admin.register(Corretor)
class CorretorAdmin(admin.ModelAdmin):
    list_display = ['nome', 'idade', 'profissao', 'imagem']