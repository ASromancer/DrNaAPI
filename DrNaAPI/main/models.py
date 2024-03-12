from django.db import models


class Consumables(models.Model):
    ID = models.CharField(primary_key=True, max_length=6)
    NAME = models.TextField(null=True)
    COST = models.IntegerField(null=True)
    QTY = models.IntegerField(null=True)
    NOTE = models.TextField(null=True)

    class Meta:
        managed = False
        db_table = 'consumables'


class Customers(models.Model):
    ID = models.CharField(primary_key=True, max_length=6)
    NAME = models.TextField(null=True)
    GENDER = models.TextField(null=True)
    DOB = models.DateField(null=True)
    ADDRESS = models.TextField(null=True)
    PHONE_NUMBER = models.CharField(max_length=15, null=True)
    NOTE = models.TextField(null=True)

    class Meta:
        managed = False
        db_table = 'customers'


class OrderDetails(models.Model):
    ID = models.IntegerField(primary_key=True)
    ORDER = models.ForeignKey('Orders', on_delete=models.CASCADE, null=True, db_column='ORDER')
    SERVICE = models.ForeignKey('Services', on_delete=models.CASCADE, null=True, db_column='SERVICE')
    DISCOUNT = models.IntegerField(null=True)
    NOTE = models.TextField(null=True)

    class Meta:
        db_table = 'order_details'


class Orders(models.Model):
    ID = models.AutoField(primary_key=True)
    CUSTOMER = models.ForeignKey('Customers', on_delete=models.CASCADE, null=True, db_column='CUSTOMER')
    TIME = models.DateTimeField(auto_now_add=True, null=True)
    NOTE = models.TextField(null=True)

    class Meta:
        managed = False
        db_table = 'orders'


class Services(models.Model):
    ID = models.CharField(primary_key=True, max_length=6)
    NAME = models.TextField(null=True)
    PRICE = models.IntegerField(null=True)
    CONSUMABLE = models.ForeignKey('Consumables', on_delete=models.CASCADE, null=True, db_column='CONSUMABLE')

    class Meta:
        managed = False
        db_table = 'services'
