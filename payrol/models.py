from django.db import models
from account.models import BankInfo, PayScale
from django.conf import settings
import datetime

# Create your models here.
class WageInfo(models.Model):
    wage_name = models.CharField(max_length=20)
    created_date = models.DateTimeField(db_index=True,
                                        default=datetime.datetime.now)

    def __str__(self):
        return self.wage_name

class EarningsType(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class DeductionType(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name

class WageDetails(models.Model):
    wage_name = models.ForeignKey(WageInfo, 
                                on_delete=models.CASCADE)
    staff_member = models.ForeignKey(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    net_pay = models.DecimalField(max_digits=7, decimal_places=2,
                                blank=True, null=True)

    def __str__(self):
        return self.staff_member + str(self.net_pay)
    
class Earnings(models.Model):
    record = models.ForeignKey(WageDetails,on_delete=models.CASCADE)
    earnings_type = models.ForeignKey(EarningsType, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return self.earnings_type + str(self.amount)

class Deductions(models.Model):
    record = models.ForeignKey(WageDetails,on_delete=models.CASCADE)
    deduction_type = models.ForeignKey(DeductionType, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return self.deduction_type + str(self.amount)