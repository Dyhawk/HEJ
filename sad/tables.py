import django_tables2 as tables 
from .models import CustomsInventory, UploadedSales

class CustomsInventoryTable(tables.Table):
    class Meta:
        model = CustomsInventory
        fields = ['sku', 'tariff', 'quantity', 'description',\
            'weight', 'cost', 'office', 'doc_type', 'doc_number',\
            'year', 'line', 'country']

class UploadedSalesTable(tables.Table):
    class Meta:
        model = UploadedSales
        fields = ['first_name', 'last_name', 'rec_number', \
            'sku', 'quantity', 'status']