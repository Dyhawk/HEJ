# Generated by Django 3.0.5 on 2020-04-30 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0007_auto_20200424_2226'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='serialized',
            field=models.BooleanField(default=True),
        ),
    ]