from typing import Any
from django.views.generic import TemplateView, DetailView
from .models import Corretor, Imovel

class IndexView(TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs: Any):
        context = super(IndexView, self).get_context_data(**kwargs)
        context ['corretor'] = Corretor.objects.all()
        context ['imovel'] = Imovel.objects.all()
        return context

class ImovelDetailView(DetailView):
    model = Imovel
    template_name = 'descricaoimovel.html'
    context_object_name = 'imovel'