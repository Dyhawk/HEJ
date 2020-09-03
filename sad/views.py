from django.shortcuts import render
from .forms import UploadFileForm, AsycudaFileForm, UploadSalesForm
from sad.tools.tools import handle_uploaded_file, \
    gather_data, handle_uploaded_xml, handle_uploaded_sales
from django.contrib import messages
from sad.tools import items, xmlTemplate
from sad.models import CustomsInventory, UploadedSales
from django.contrib.auth.decorators import login_required
import math

# Create your views here.
@login_required
def upload_winjewel_entry(request, pk):
    form = UploadFileForm
    sad = False
    gather_data(pk)
    name, AWB = gather_data(pk)[0], gather_data(pk)[1]
    if request.method == 'POST':
        if form.is_valid:
            weight, itemNum = request.POST['weight'], request.POST['itemNum']
            try:
                fileUploaded = request.FILES['file']
                fileUploaded = str(fileUploaded)
                ext = ['.txt', 'csv']
            except:
                form = UploadFileForm
            try:
                weight, itemNum = float(weight), int(itemNum)
                if itemNum <= 0:
                    raise ValueError
                if fileUploaded.endswith(tuple(ext)):
                    form = handle_uploaded_file(request.FILES['file'], weight,\
                        name, itemNum, AWB)
                    request.session['data'] = form
                    request.session['name'] = name
                    sad = True
                else:
                    raise ValueError
            except:
                messages.error(request,'There is an error. Please review \
                the data you have entered:')
                form = UploadFileForm
                sad = False

    return render(request, 'sad/upload_winjewel_file.html', {'form': form, 'sad': sad,})

@login_required
def download_created_xml(request):
    record = []
    files = []
    name = request.session['name']
    content = request.session['data']
    for item in content:
        line = items.Item(item[0], item[1], item[2], item[3],item[4], item[5],\
         item[6],item[7], item[8])
        record.append(line)
    numFiles = math.ceil(len(record)/ 299.00)
    numItems = int(math.ceil(len(record)/numFiles))
    inter = numItems
    starter = 0
    while numFiles > 0:
        itemList = record[starter:numItems]
        starter = numItems
        numItems = numItems + inter
        files.append(itemList)
        numFiles -= 1
        output_file = xmlTemplate.new_xml(files, name)
    return output_file

@login_required
def upload_asycude_xml(request):
    form = AsycudaFileForm
    sad = False
    if request.method == 'POST':
        if form.is_valid:
            fileUploaded = request.FILES['xml_file']
            fileUploaded = str(fileUploaded)
            ext = 'xml'
            if fileUploaded.endswith(ext):
                form = handle_uploaded_xml(request.FILES['xml_file'])
                sad = True
                request.session['xml_data'] = form
            else:
                messages.error(request, 'There is a problem with the file you uploaded.\
                    Please ensure you are uploading a customs xml file from Asycuda.')
                form = AsycudaFileForm
                sad = False

    return render(request, 'sad/upload_asycuda_file_form.html', {'form': form, 'sad': sad} )

@login_required
def download_asycuda_xml(request):
    sad = False
    content = request.session['xml_data']
    doc_number = str(content[0][9])
    year = str(content[0][10])
    q = CustomsInventory.objects.filter(doc_number=doc_number, year=year)
    verify = len(q)
    if verify == 0:
        sad = True
        for line in content:
            records = CustomsInventory(sku=line[0], tariff=line[1], quantity=line[2],\
            country=line[3], description=line[4], weight=line[5], cost=line[6],\
            office=line[7], doc_type=line[8], doc_number=line[9],year=line[10],\
            line=line[11])
            records.save()
    else:
        sad = False
    
    recent_entry = CustomsInventory.objects.filter(doc_number=doc_number, year=year)
    return render(request, 'sad/customs_inventory_list.html', {'recent_entry': recent_entry,
                                                                'sad': sad})

@login_required
def upload_winjewel_sales(request):
    form = UploadSalesForm
    sad = False
    if request.method == 'POST':
        if form.is_valid:
            fileUploaded = request.FILES['sales_file']
            fileUploaded = str(fileUploaded)
            ext = ['csv', 'txt']
            if fileUploaded.endswith(tuple(ext)):
                form = handle_uploaded_sales(request.FILES['sales_file'])
                sad = True
                request.session['sales_file'] = form

    return render(request, 'sad/upload_sales.html', {'form': form,
                                                    'sad': sad})

@login_required
def submit_sales(request):
    sales = request.session['sales_file']
    for line in sales:
        record = UploadedSales(sku=line[0],quantity=line[1],sales_status=line[2],\
        rec_num=line[3],sales_date=line[4],first_name=line[5],last_name=line[6],\
        ticket_num=line[7],id_type=line[8],id_num=line[9],vessel=line[10], \
        country=line[11],depart_port=line[12],depart_date=line[13], \
        gender=line[14])
        record.save()
    return render(request, 'sad/sales_upload_success.html')