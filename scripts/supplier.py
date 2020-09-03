import csv
from inventory.models import Supplier

def run():
    f = open('data/Supplier.csv')
    reader = csv.reader(f)

    Supplier.objects.all().delete()

    for row in reader:
        c, created = Supplier.objects.get_or_create(name=row[0], code=row[1])