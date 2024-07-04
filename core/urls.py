from django.urls import path
from .views import IndexView, ImovelDetailView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('descricaoimovel/<int:pk>', ImovelDetailView.as_view(), name='descricaoimovel'),
]

