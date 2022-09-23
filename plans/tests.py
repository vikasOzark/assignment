from re import L
from django.test import TestCase
import plans_collector
# Create your tests here.
# plan = plans_collector.plan()
l = ('1 plan', ['40 GB', '100', 'Unlimited', 'N/A', '399'])

for i in enumerate(l):
    print(i[1][0])

l = list(l)
print(l[1][0])