import django_filters
from .models import CustomsInventory, UploadedSales

class CustomsInventoryFilter(django_filters.FilterSet):
    class Meta:
        model = CustomsInventory
        fields = {'doc_number': ['icontains'], 'sku':['icontains'],
                'year':['icontains']}

class UploadedSalesFilter(django_filters.FilterSet):
    class Meta:
        model = UploadedSales
        fields = {'rec_num':['icontains']}