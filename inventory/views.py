from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from .forms import CatalogueForm, EntryForm, InventoryForm, ItemUpdateForm
from django.urls import reverse_lazy
from . models import Catalogue, Inventory, Supplier, Tariff, \
                        Department, Entry, Shipper, ShipmentType, Country
# from django import forms
from braces.views import LoginRequiredMixin, \
                        PermissionRequiredMixin
from inventory.tools import internal_sku, totals
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
class CatalogueListView(LoginRequiredMixin, ListView):
    model = Catalogue
    template_name = 'inventory/catalogue/cat_list.html'

class SupplierListView(LoginRequiredMixin, ListView):
    model = Supplier
    template_name = 'inventory/catalogue/sup_list.html'

class ShipmentTypeCreateView(LoginRequiredMixin, CreateView):
    model = ShipmentType
    fields = '__all__'
    template_name = 'inventory/catalogue/form.html'

class ShipmentTypeListView(LoginRequiredMixin, ListView):
    model = ShipmentType
    template_name = 'inventory/catalogue/ShipmentType_list.html'

class TariffListView(LoginRequiredMixin, ListView):
    model = Tariff
    template_name = 'inventory/catalogue/tariff_list.html'

class DepartmentListView(LoginRequiredMixin, ListView):
    model = Department
    template_name = 'inventory/catalogue/dept_list.html'

class ShipperListView(LoginRequiredMixin, ListView):
    model = Shipper
    template_name = 'inventory/catalogue/shipper_list.html'

class SupplierCreateView(LoginRequiredMixin, CreateView):
    model = Supplier
    fields = '__all__'
    template_name = 'inventory/catalogue/form.html'

class ShipperCreateView(LoginRequiredMixin, CreateView):
    model = Shipper
    fields = '__all__'
    template_name = 'inventory/catalogue/form.html'

class TariffCreateView(LoginRequiredMixin, CreateView):
    model = Tariff
    fields = '__all__'
    template_name = 'inventory/catalogue/form.html'

class DepartmentCreateView(LoginRequiredMixin, CreateView):
    model = Department
    fields = '__all__'
    template_name = 'inventory/catalogue/form.html'

class CatalogueCreateView(LoginRequiredMixin, CreateView):
    model = Catalogue
    form_class = CatalogueForm
    template_name = 'inventory/catalogue/form.html'

class EntryCreateView(LoginRequiredMixin, CreateView):
    model = Entry
    form_class = EntryForm
    template_name = 'inventory/entry/entry_form.html'
    success_url = reverse_lazy('entry_list')

class EntryListView(LoginRequiredMixin, ListView):
    model = Entry
    template_name = 'inventory/entry/entry_list.html'

class EntryUpdateView(LoginRequiredMixin, UpdateView):
    model = Entry
    fields = ['supplier','shipment_type','weight', 'items']
    template_name = 'inventory/entry/entry_update_form.html'
    success_url = reverse_lazy('entry_list')

# complete delete view
class EntryDeleteView(LoginRequiredMixin, DeleteView):
    model = Entry
    

class InventoryListView(LoginRequiredMixin, ListView):
    model = Inventory
    template_name = 'inventory/list.html'

# complete delete view
class ItemDeleteView(LoginRequiredMixin, DeleteView):
    model = Inventory
    success_url = reverse_lazy('entry_list')


@login_required
def create_inventory_view(request, pk):
    batch_id = pk
    entry = get_object_or_404(Entry, batch_ID=batch_id)
    sup_id = entry.supplier.id
    sup_num = entry.supplier.code
    entry_id = entry.id
    entry_cost = entry.cost
    form = InventoryForm(sup_id)
    inv_list = Inventory.objects.filter(entry=entry_id)
    total = totals(entry_cost, inv_list)
    # context = {'entry': entry, 'form':form, 'inv_list':inv_list, 'total':total}
    if request.method == 'POST':
        try:
            cost = request.POST['cost']
            sku = get_object_or_404(Catalogue, id=request.POST['sku'])
            quantity = request.POST['quantity']
            tariff = get_object_or_404(Tariff, id=request.POST['tariff'])
            country = get_object_or_404(Country, id=request.POST['country'])
            sku_value = internal_sku(sup_num)
            entry = entry
        except:
            messages.error(request, 'Please check your form inputs.')

        if int(quantity) > 0:
            if type(cost)==float or int:
                data = Inventory(sku=sku, cost=cost, quantity=quantity, 
                tariff=tariff, country=country, internalsku=sku_value, 
                entry=entry)
                data.save()
                inv_list = Inventory.objects.filter(entry=entry_id)
            else:
                messages.error(request,\
                    'The information entered is not valid \
                    please review.')
        else:
            messages.error(request,\
                'The quantity entered must be greater than 1')
    else:
        form = InventoryForm(sup_id)
    inv_list = Inventory.objects.filter(entry=entry_id)
    total = totals(entry_cost, inv_list)
    context = {'entry': entry, 'form':form, 'inv_list':inv_list, 'total':total}
    return render(request, 'inventory/entry/inventory_form.html', context)

@login_required
def item_update_view(request, pk):
    item_id = pk
    item = get_object_or_404(Inventory, id=item_id)
    sup_id = item.entry.supplier.id
    data = {'quantity': item.quantity, 'country': item.country,
            'tariff': item.tariff, 'cost': item.cost, 'sku':item.sku }
    form = ItemUpdateForm(sup_id, request.POST or None, initial=data)
    context ={'item': item, 'form':form}
    if request.method == 'POST':
        try:
            item.cost = request.POST['cost']
            item.quantity = request.POST['quantity']
            item.tariff = get_object_or_404(Tariff, id=request.POST['tariff'])
            item.country = get_object_or_404(Country, id=request.POST['country'])
            item.serial = request.POST['serial']
        except:
            messages.error(request, 'Please check your form inputs.')
        if int(item.quantity) > 0:
            if type(item.cost)==float or int:
                item.save()
                return redirect("add_inventory", pk=item.entry.batch_ID)
            else:
                messages.error(request,\
                    'The information entered is not valid \
                    please review.')
        else:
            messages.error(request,\
                'The quantity entered must be greater than 1')
    else:
        form = ItemUpdateForm
    return render(request, 'inventory/entry/inventory_update_form.html', context)