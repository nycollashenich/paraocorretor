from typing import Any
from django.views.generic import TemplateView
from .models import Corretor

class IndexView(TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs: Any):
        context = super(IndexView, self).get_context_data(**kwargs)
        context ['corretor'] = Corretor.objects.all()
        return context

