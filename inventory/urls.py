from django.urls import path, include
from . import views
from django_filters.views import object_filter

# app_name = 'inventory'

urlpatterns = [
    path('catalogue/list', views.CatalogueListView.as_view(),
    name='catalogue_list'),
    path('catalogue/add', views.CatalogueCreateView.as_view(),
    name='add_catalogue'),
    path('entry/create', views.EntryCreateView.as_view(), 
    name='add_entry'),
    path('entry/list', views.EntryListView.as_view(),
    name='entry_list'),
    path('shipper/add', views.ShipperCreateView.as_view(),
    name='add_shipper'),
    path('shipper/list', views.ShipperListView.as_view(),
    name='shipper_list'),
    path('supplier/add', views.SupplierCreateView.as_view(),
    name='add_supplier'),
    path('entry/Shipment_type', views.ShipmentTypeCreateView.as_view(),
    name='add_shipment_type'),
    path('entry/shipment_type_list', views.ShipmentTypeListView.as_view(),
    name='shipment_type_list'),
    path('supplier/list', views.SupplierListView.as_view(),
    name='supplier_list'),
    path('tariff/add', views.TariffCreateView.as_view(),
    name='add_tariff'),
    path('tariff/list', views.TariffListView.as_view(),
    name='tariff_list'),
    path('department/list', views.DepartmentListView.as_view(),
    name='department_list'),
    path('department/add', views.DepartmentCreateView.as_view(),
    name='add_department'),
    path('entry/update_entry/<int:pk>', views.EntryUpdateView.as_view(),
    name='entry_update'),
    path('entry/add_inventory/<int:pk>/', views.create_inventory_view,
    name='add_inventory'),
    path('inventory/list', views.InventoryListView.as_view(), 
    name='inventory_list'),
    path('entry/update_item/<int:pk>', views.item_update_view,
    name='item_update'),
    path('item/delete/<int:pk>/', views.ItemDeleteView.as_view(),
    name='item_delete'),
    path('entry/delete/<int:pk>', views.EntryDeleteView.as_view(), 
    name='entry_delete'),

]