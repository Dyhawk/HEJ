from django.db import models
from django.conf import settings

# Create your models here.
def get_directory_path(instance, filename):
    return 'user/{0}/{1}/{2}'.format(instance.user.id,
            instance.user.username,filename)

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    nic = models.PositiveIntegerField(blank=True, null=True)
    paye = models.CharField(max_length=4, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    date_hired = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to=get_directory_path, blank=True)

    def __str__(self):
        return f'Profile for user {self.user.username}'

class BankInfo(models.Model):
    bank_name = models.CharField(max_length=25)

    def __str__(self):
        return self.bank_name


class Bank(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                                 on_delete=models.CASCADE)
    bank_name = models.ForeignKey(BankInfo, on_delete=models.CASCADE)
    bank_account_number = models.CharField(max_length=50, 
                                            blank=True, null=True)
    description = models.CharField(max_length=20)

    def __str__(self):
        return self.bank_account_number + self.description


class PayScale(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, 
                                on_delete=models.CASCADE)
    monthly = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return str(self.monthly)