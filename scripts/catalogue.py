import csv
from inventory.models import Catalogue, Supplier, Department

def run():
    f = open('data/Catalogue.csv')
    reader = csv.reader(f)

    Catalogue.objects.all().delete()

    for row in reader:
        dep = Department.objects.get(name=row[3])
        sup = Supplier.objects.get(code=row[0])
        c, created = Catalogue.objects.get_or_create(sku=row[2], description=row[1], department=dep, retail=row[4], supplier=sup)