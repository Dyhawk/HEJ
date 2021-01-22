from django.db import models
from django.conf import settings
from django.utils import timezone
import datetime

# Create your models here.
class Task(models.Model):
    assign_by = models.ForeignKey(settings.AUTH_USER_MODEL, 
                                related_name='assigned_by',
                                on_delete=models.CASCADE)
    assign_to = models.ForeignKey(settings.AUTH_USER_MODEL,
                                related_name='assigned_to',
                                on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    body = models.TextField(blank=True, null=True)
    STATUS_CHOICE = (
        ('NOT', 'NOT STARTED'),
        ('INP', 'IN PROGRESS'),
        ('COM', 'COMPLETED')
    )
    status = models.CharField(max_length=3, choices=STATUS_CHOICE, default='NOT')
    created_date = models.DateTimeField(db_index=True, default=datetime.datetime.now)
    completed_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return str(self.title)
    