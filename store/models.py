from django.db import models
from inventory.models import Country

# Create your models here.
class ContactType(models.Model):
    contact_type = models.CharField(max_length=50)

    def __str__(self):
        return str(self.contact_type)
    
class Customers(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        name = str(self.first_name) + ' '+ str(self.last_name)
        return name

class Contacts(models.Model):
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE)
    contact_type = models.ForeignKey(ContactType, on_delete=models.CASCADE)
    contact_data = models.CharField(max_length=100)

    def __str__(self):
        return str(self.customer)

class Address(models.Model):
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE)
    address_line_1 = models.CharField(max_length=100)
    address_line_2 = models.CharField(max_length=100)
    mail_code = models.CharField(max_length=50)
    Country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.customer)
    

class Company(models.Model):
    company_name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.company_name)
    

class Stores(models.Model):
    company_name = models.ForeignKey(Company, on_delete=models.CASCADE)
    store_name = models.CharField(max_length=50)
    store_code = models.CharField(max_length=20, unique=True)
    

class Sales(models.Model):
    pass