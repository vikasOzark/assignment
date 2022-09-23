from django.shortcuts import render
from . import serializers
from rest_framework.generics import ListAPIView
from plans import models

# Create your views here.

class ListPlansView(ListAPIView):
    serializer_class = serializers.PlansSerializer
    queryset = models.PlansModel.objects.all()