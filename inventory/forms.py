from django import forms
from .models import Catalogue, Entry, Inventory
from django.shortcuts import get_object_or_404


class DateInput(forms.DateInput):
    input_type = 'date'

class CatalogueForm(forms.ModelForm):
    class Meta:
        model = Catalogue
        fields = ['sku', 'description', 'department', 'retail',\
         'introduced', 'supplier']
        widgets = {'introduced': DateInput()}

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['batch_ID', 'shipment_type', 'location', 'warehousing', 'invoice_number',\
            'cost', 'cif', 'supplier', 'shipper', 'awb', 'invoice_date']
        widgets = {'invoice_date': DateInput()}

class InventoryForm(forms.ModelForm):
    
    class Meta:
        model = Inventory
        fields = ['sku', 'cost', 'quantity', 'tariff', 'country', 'internalsku', 'entry']
        widgets = {'entry': forms.HiddenInput(),
                    'internalsku': forms.HiddenInput()}


    def __init__(self, sup_id, *args, **kwargs):
        super(InventoryForm, self).__init__(*args, **kwargs)
        self.fields['sku'].queryset = Catalogue.objects.filter(supplier=sup_id)

class ItemUpdateForm(forms.ModelForm):

    class Meta:
        model = Inventory
        fields = ['sku', 'quantity','cost','serial', 'tariff', 'country']

    def __init__(self, sup_id, *args, **kwargs):
        super(ItemUpdateForm, self).__init__(*args, **kwargs)
        self.fields['sku'].queryset = Catalogue.objects.filter(supplier=sup_id)

        



