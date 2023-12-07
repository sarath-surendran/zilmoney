from django.db import models

# Create your models here.

class Products(models.Model):
    name =  models.CharField(max_length=255)
    description = models.TextField()
    availiable_quantity = models.IntegerField()
    amount = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Purchase(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    purchased_quantity = models.IntegerField()
    total_amount = models.FloatField()
