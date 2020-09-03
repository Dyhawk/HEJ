import csv
from inventory.models import Country, Supplier

def run():
    f = open('data/country.csv')
    reader = csv.reader(f)

    Country.objects.all().delete()

    for row in reader:
        c, created = Country.objects.get_or_create(name=row[0], code=row[1])