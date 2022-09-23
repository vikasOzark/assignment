from rest_framework import serializers
from plans import models 

class PlansSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PlansModel
        fields = '__all__'