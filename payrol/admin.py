from django.contrib import admin
from .models import EarningsType, Earnings, WageDetails, WageInfo

# Register your models here.
@admin.register(EarningsType)
class EarningsTypeAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Earnings)
class Earnings(admin.ModelAdmin):
    list_display = ['earnings_type', 'amount']

@admin.register(WageInfo)
class WageInfoAdmin(admin.ModelAdmin):
    list_display = ['wage_name']

@admin.register(WageDetails)
class WageDetailsAdmin(admin.ModelAdmin):
    list_display = ['wage_name', 'staff_member', 'net_pay']