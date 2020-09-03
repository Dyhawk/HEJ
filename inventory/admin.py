from django.contrib import admin
from .models import Catalogue, Inventory, Supplier, Stone, Department, \
                    Tariff

# Register your models here.
@admin.register(Catalogue)
class CatalogueAdmin(admin.ModelAdmin):
    list_display = ['sku', 'description', 'retail', 'active', 'supplier',\
        'department', 'introduced']

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ['name', 'code']

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ['sku', 'internalsku', 'cost', 'tariff', 'quantity']

@admin.register(Tariff)
class TariffAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'description']

@admin.register(Stone)
class StoneAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']