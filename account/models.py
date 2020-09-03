from django.db import models
from django.conf import settings

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    nic = models.PositiveIntegerField(blank=True, null=True)
    paye = models.CharField(max_length=4, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    date_hired = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/',
                              blank=True)

    def __str__(self):
        return f'Profile for user {self.user.username}'