# Generated by Django 3.0.5 on 2020-04-09 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_auto_20200403_1449'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventory',
            name='approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='inventory',
            name='batch',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='inventory',
            name='consignment',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tariff',
            name='surcharge',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='supplier',
            name='code',
            field=models.CharField(max_length=3, unique=True),
        ),
    ]
