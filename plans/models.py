from django.db import models

# Create your models here.
class PlansModel(models.Model):
    plan_name = models.CharField(max_length=50)
    data_rollover = models.CharField(max_length=50)
    sms_per_day = models.CharField(max_length=50)
    amazon_prime = models.BooleanField(default=False)
    price = models.CharField(max_length=50, default='00.0')