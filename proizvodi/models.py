from django.db import models

class Products(models.Model):
    title = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(max_length=150,blank=True)
    novi = models.BooleanField()