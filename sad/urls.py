from django.urls import path
from sad import views

urlpatterns = [
    path('customs_inventory', views.CustomsInventoryListView.as_view(),
    name='customs_inventory'),
    path('download_xml', views.download_created_xml, name='winjewel_xml_download'),
    path('upload_entry_file/<int:pk>/', views.upload_winjewel_entry, 
    name='winjewel_file_upload'),
    path('upload_asycuda_file', views.upload_asycude_xml, name='asycuda_file_upload'),
    path('post_to_inventory', views.download_asycuda_xml, name='post_to_inventory'),
    path('upload_sales', views.upload_winjewel_sales, name='upload_sales' ),
    path('submit_sales', views.submit_sales, name='submit_sales'),
]