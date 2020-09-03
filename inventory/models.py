from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy
from django.core.validators import MinValueValidator
import datetime

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=150, unique=True)
    code = models.CharField(max_length=2, unique=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Supplier(models.Model):
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=3, unique=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('supplier_list')

    def clean_fields(self, exclude=None):
        super().clean_fields(exclude=exclude)
        if self.code.isdigit():
            if len(self.code) < 3:
                if len(self.code) == 1:
                    self.code = "00"+self.code
                else:
                    self.code = "0"+self.code
        else:
            raise ValidationError( {'code':gettext_lazy('Only Digits are allowed')})

    def save(self, *args, **kwargs):
        self.name = self.name.upper()
        return super(Supplier, self).save(*args, **kwargs)

class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('department_list')

    def save(self, *args, **kwargs):
        self.name = self.name.upper()
        return super(Department, self).save(*args, **kwargs)

class Tariff(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=11, unique=True)
    description = models.TextField(blank=True)
    vat = models.FloatField()
    duty = models.FloatField()
    surcharge = models.FloatField()

    class Meta:
        ordering = ('code',)

    def __str__(self):
        return self.code

    def get_absolute_url(self):
        return reverse('tariff_list')

    def save(self, *args, **kwargs):
        self.name = self.name.upper()
        self.description = self.description.capitalize()
        return super(Tariff, self).save(*args, **kwargs)

class Stone(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True)
    picture = models.ImageField(upload_to='stone/%Y/%m/%d', blank=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = self.name.upper()
        self.description = self.description.capitalize()
        return super(Stone, self).save(*args, **kwargs)

class Catalogue(models.Model):
    sku = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    department = models.ForeignKey(Department, 
                                   related_name='catalogues',
                                   on_delete=models.CASCADE)
    retail = models.DecimalField(max_digits=10, decimal_places=2)
    introduced = models.DateField(blank=True, null=True)
    active = models.BooleanField(default=True)
    supplier = models.ForeignKey(Supplier,
                                 related_name='catalogues',
                                 on_delete=models.CASCADE)

    class Meta:
        unique_together = ('sku', 'supplier')
        indexes = [
            models.Index(fields=['sku']),
            ]

    def __str__(self):
        return self.sku

    def get_absolute_url(self):
        return reverse('catalogue_list')

    def save(self, *args, **kwargs):
        self.sku = self.sku.upper()
        self.description = self.description.upper()
        return super(Catalogue, self).save(*args, **kwargs)

class Shipper(models.Model):
    shipper = models.CharField(max_length=25, unique=True)

    class Meta:
        ordering = ('shipper',)

    def __str__(self):
        return self.shipper

    def get_absolute_url(self):
        return reverse('shipper_list')

    def save(self, *args, **kwargs):
        self.shipper = self.shipper.upper()
        return super(Shipper, self).save(*args, **kwargs)

class ShipmentType(models.Model):
    shipment_type = models.CharField(max_length=25, unique=True)
    
    def __str__(self):
        return self.shipment_type

    def get_absolute_url(self):
        return reverse('shipment_type_list')

    def save(self, *args, **kwargs):
        self.shipment_type = self.shipment_type.upper()
        return super(ShipmentType, self).save(*args, **kwargs)

class Entry(models.Model):
    batch_ID = models.SmallIntegerField(unique=True)
    shipment_type = models.ForeignKey(ShipmentType, 
                            related_name='shipment_types',
                            on_delete=models.CASCADE)
    LOCATION = (('GRE', 'GRENADA'), ('SLU', 'ST. LUCIA'))
    location = models.CharField(max_length=3, choices=LOCATION, default='SLU')
    warehousing = models.SmallIntegerField()
    invoice_number = models.CharField(max_length=150)
    cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    cif = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    shipper = models.ForeignKey(Shipper, on_delete=models.CASCADE)
    awb = models.CharField(max_length=50, blank=True, null=True)
    invoice_date = models.DateField(blank=True, null=True)
    STATUS_CHOICE = (
        ('PEN', 'PENDING'),
        ('CUS', 'AWAITING CUSTOMS'),
        ('COM', 'COMPLETED')
    )
    status = models.CharField(max_length=3, choices=STATUS_CHOICE, default='PEN')
    serialized = models.BooleanField(default=True)
    weight = models.FloatField(blank=True, null=True, verbose_name="Weight in (KG)")
    items = models.PositiveIntegerField(blank=True, null=True)
    created_date = models.DateTimeField(db_index=True, default=datetime.datetime.now)
    entered_date = models.DateField(blank=True, null=True)
    cleared_date = models.DateField(blank=True, null=True)
    racked_date = models.DateField(blank=True, null=True)
    posted_date = models.DateField(blank=True, null=True)

    class Meta:
        ordering = ('batch_ID',)

    def __str__(self):
        return str(self.batch_ID)

    def save(self, *args, **kwargs):
        self.invoice_number = self.invoice_number.upper()
        self.awb = self.awb.upper()
        return super(Entry, self).save(*args, **kwargs)

class Inventory(models.Model):
    entry = models.ForeignKey(Entry, 
                               related_name='Entries',
                               on_delete=models.CASCADE)
    sku = models.ForeignKey(Catalogue,
                            related_name='inventories',
                            on_delete=models.CASCADE)
    internalsku = models.CharField(max_length=10)
    cost = models.DecimalField(max_digits=10, decimal_places=2,\
                              validators=[MinValueValidator('0.01'),])
    cif = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    country = models.ForeignKey(Country, default=238,
                                on_delete=models.CASCADE)
    tariff = models.ForeignKey(Tariff,
                               related_name='inventories',
                               on_delete=models.CASCADE)
    quantity = models.SmallIntegerField(default=1)
    serial = models.CharField(max_length=50, blank=True, null=True)
    consignment = models.BooleanField(default=False)
    duty = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return str(self.internalsku)