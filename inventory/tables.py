import django_tables2 as tables 
from .models import Supplier

class SupplierTable(tables.Table):
    class Meta:
        model = Supplier
        fields = ['name', 'code']
