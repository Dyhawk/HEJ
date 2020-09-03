from django.db import models

# Create your models here.
class CustomsInventory(models.Model):
    sku = models.CharField(max_length=8, unique=True)
    tariff = models.CharField(max_length=8)
    quantity = models.SmallIntegerField()
    country = models.CharField(max_length=2)
    description = models.CharField(max_length=200)
    weight = models.FloatField()
    cost = models.DecimalField(decimal_places=2, max_digits=10)
    office = models.CharField(max_length=20)
    doc_type = models.CharField(max_length=3)
    doc_number = models.CharField(max_length=20)
    year = models.CharField(max_length=4)
    line = models.SmallIntegerField()
    LOCATION = (('GRE', 'GRENADA'), ('SLU', 'ST. LUCIA'))
    location = models.CharField(max_length=3, choices=LOCATION, default='GRE')

    def __str__(self):
        return str(self.doc_number)

class UploadedSales(models.Model):
    sku = models.CharField(max_length=8)
    quantity = models.SmallIntegerField()
    sales_status = models.CharField(max_length=20)
    rec_num = models.CharField(max_length=10)
    sales_date = models.CharField(max_length=10)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    ticket_num = models.CharField(max_length=50)
    id_type = models.CharField(max_length=50)
    id_num = models.CharField(max_length=150)
    vessel = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    depart_date = models.CharField(max_length=10)
    depart_port = models.CharField(max_length=20)
    gender = models.CharField(max_length=10)

    def __str__(self):
        return str(self.rec_num)

