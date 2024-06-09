# models.py
from django.db import models


class Buyer(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)

    class Meta:
        verbose_name = "Buyer"
        verbose_name_plural = "Buyers"


class Operator(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)


class Manufacturer(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)


class Category(models.Model):
    name = models.CharField(max_length=255)


class Subcategory(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="subcategories")


class Product(models.Model):
    name = models.CharField(max_length=255)
    subcategory_list = models.ManyToManyField(Subcategory)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    description = models.TextField()
    warranty_period = models.FloatField()


class Order(models.Model):
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE, related_name="orders")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    description_creation_date = models.DateTimeField(auto_now_add=True)
    delivery_type = models.CharField(max_length=255)
    delivery_address = models.TextField()
    check_detail = models.OneToOneField("Check", on_delete=models.CASCADE, null=True, blank=True)
    status = models.CharField(max_length=255, choices=[
        ("open", "open"),
        ("closed", "closed"),
        ("sent", "sent"),
        ("received", "received"),
        ("returned", "returned"),
    ])


class Check(models.Model):
    order_detail = models.OneToOneField(Order, on_delete=models.CASCADE, related_name="check_order")
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE, related_name="checks")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add=True)
    warranty_period = models.FloatField()
    price = models.FloatField()
