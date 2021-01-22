import django_filters
from .models import Supplier

class SupplierFilter(django_filters.FilterSet):
    #ame = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Supplier
        fields = {'name': ['icontains'],
        'code': ['icontains'],}
