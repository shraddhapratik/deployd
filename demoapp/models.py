from django.db import models


class Address(models.Model):
    city = models.CharField(max_length=15)
    pincode=models.IntegerField()
    state=models.CharField(max_length=300)

    class Meta:
        db_table = "Address_Info"


class Customer(models.Model):
    custName = models.CharField(max_length=15)
    custAge = models.IntegerField()
    custBalance = models.IntegerField()

    class Meta:
        db_table = "Customer_Info"
