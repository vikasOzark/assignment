# Generated by Django 4.1.1 on 2022-09-21 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PlansModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan_name', models.CharField(max_length=50)),
                ('data_rollover', models.CharField(max_length=50)),
                ('sms_per_day', models.CharField(max_length=50)),
                ('amazon_prime', models.BooleanField(default=False)),
            ],
        ),
    ]