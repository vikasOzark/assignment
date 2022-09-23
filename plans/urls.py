from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('plans-load/', views.load_plan, name='plans-load'),
]
