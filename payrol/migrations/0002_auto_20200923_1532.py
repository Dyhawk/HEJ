# Generated by Django 3.0.5 on 2020-09-23 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payrol', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wagedetails',
            name='net_pay',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True),
        ),
    ]
