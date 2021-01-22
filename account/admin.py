from django.contrib import admin
from .models import Profile, BankInfo, Bank, PayScale

# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'nic', 'paye', 'date_hired']

@admin.register(BankInfo)
class BankInfoAdmin(admin.ModelAdmin):
    list_display = ['bank_name']

@admin.register(Bank)
class Bank(admin.ModelAdmin):
    list_display = ['user', 'bank_name', 'bank_account_number', 'description']

@admin.register(PayScale)
class PayScaleAdmin(admin.ModelAdmin):
    list_display = ['user', 'monthly']