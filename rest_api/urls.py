from django.urls import path

from rest_api import views
from . import views

urlpatterns = [
    path('list-all', views.ListPlansView.as_view())
]
