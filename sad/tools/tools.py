import csv
import io
import datetime
from defusedxml import ElementTree
import re
import math
from inventory.models import Entry

def gather_data(pk):
    entry = Entry.objects.get(batch_ID=pk)
    name = entry.batch_ID
    awb = entry.awb
    return name, awb

def handle_uploaded_file(csv_file, weight, name, itemNum, AWB):
    record_set = []
    weight = float(weight)
    itemNum = int(itemNum)
    unitWeight = weight / itemNum
    content = []
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for value in csv.reader(io_string, delimiter='#'):
        sku = value[0]
        description = value[1]
        description = re.sub(r'[^A-Za-z0-9 ]+', '', str(description))
        quantity = value[2]
        tariff = value[3][:8]
        cost = value[4]
        cost = float(cost) * int(quantity)
        cost = '%.2f' % cost
        country = value[5]
        weight = int(quantity) * float(unitWeight)
        weight = '%.2f'% weight
        line = [name, sku, description, tariff, country, quantity,\
         cost, weight, AWB]
        record_set.append(line)
    content = record_set
    return content

def asycuda_entry_id(f):
    for item in f:
        if item.tag == 'Identification':
            for o in item.find('.//Office_segment'):
                if o.tag == 'Customs_clearance_office_code':
                    office = o.text
            for s in item.find('.//Registration'):
                if s.tag == 'Serial_number':
                    cnum = s.text
                if s.tag == 'Number':
                    num = s.text
                if s.tag == 'Date':
                    d = s.text
                    year = datetime.datetime.strptime(d, '%m/%d/%y').year
            return office, cnum, num, year

def asycuda_itemizer(f):
    for hs in f.find('.//Tarification/HScode'):
        if hs.tag == 'Precision_4':
            item_code = hs.text
        if hs.tag == 'Commodity_code':
            com_code = hs.text
    for sup in f.find('.//Tarification/Supplementary_unit'):
        if sup.tag == 'Suppplementary_unit_quantity':
            quantity = sup.text
    for country in f.find('.//Goods_description'):
        if country.tag == 'Country_of_origin_code':
            cn = country.text
        if country.tag == 'Description_of_goods':
            desc = country.text
    for weight in f.find('.//Valuation_item/Weight_itm'):
        if weight.tag == 'Net_weight_itm':
            net = weight.text
    for cif in f.find('.//Valuation_item'):
        if cif.tag == 'Total_CIF_itm':
            cost = cif.text
    return item_code, com_code, quantity, cn, desc, net, cost

def handle_uploaded_xml(xfile):
    try:
        tree = ElementTree.parse(xfile)
    except:
        return 'XML file failed defuser. Please verify the source of the file.'
    root = tree.getroot()
    count = 0
    record = list()
    prev_entry = asycuda_entry_id(root)
    for item in root:
        if item.tag == 'Item':
            count += 1
            itm = asycuda_itemizer(item)
            line = [itm[0], itm[1], itm[2], itm[3], itm[4], itm[5], itm[6] ,\
            prev_entry[0], prev_entry[1], prev_entry[2], prev_entry[3], count ]
            
            if line[0] != '\n':
                record.append(line)
    return record
    
def handle_uploaded_sales(sales_file):
    record = []
    data_set = sales_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    for value in csv.reader(io_string, delimiter='#'):
        if len(value) > 4:
            value[0] = value[0].replace("*", "")
            sales_date, receipt, id_num = value[0].upper(), value[1].upper(), value[2].upper()
            ticket_num, country, id_type = value[3].upper(), value[4].upper(), value[5].upper()
            ship, depart_date, sex = value[6].upper(), value[-7].upper(), value[-1].upper()
            first_name, last_name, depart_port = value[-5].upper(), value[-4].upper(), value[-6].upper()
        else:
            if value[2] == "E":
                value[2] = "Duty Free"
            else:
                value[2] = "Duty Paid"
            value.append(receipt), value.append(sales_date), value.append(first_name)
            value.append(last_name), value.append(ticket_num), value.append(id_type)
            value.append(id_num), value.append(ship), value.append(country)
            value.append(depart_date), value.append(depart_port), value.append(sex)

            record.append(value)

    return record
