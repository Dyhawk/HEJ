import csv
from inventory.models import Catalogue, Inventory, Tariff, Entry

def run():
    f = open('data/Rolex_import.csv')
    reader = csv.reader(f)

    Inventory.objects.all().delete()

    for row in reader:
        cat = Catalogue.objects.get(sku=str(row[1]))
        entry = Entry.objects.get(id=4)
        tariff = Tariff.objects.get(id=6)
        c, created = Inventory.objects.get_or_create(internalsku=row[0], cost=row[2], cif=row[3], sku=cat, tariff=tariff, entry=entry )