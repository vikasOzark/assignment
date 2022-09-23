from gettext import install
from django.shortcuts import render, redirect
from . import models
from . import plans_collector
# Create your views here.
def load_plan(request):
    plan = plans_collector.plan()
    # converting dict object to list
    plan_obj = list(plan.items())

    for plan in range(len(plan_obj)):
        instance = plan_obj[plan]
        # converting tuple to list
        instance = list(instance)[1]

        prime = False
        if instance[3] == 'YES':
            prime = True
        
        plans_db = models.PlansModel(
            plan_name = 'Monthly rental of',
            data_rollover = instance[0],
            sms_per_day = instance[1],
            amazon_prime = prime,
            price = instance[4]
        )
        plans_db.save()
    return redirect('index')

def index(request):
    plans = models.PlansModel.objects.all()
    
    template_name = 'plans/index.html'
    return render(request, template_name, {'plans': plans})