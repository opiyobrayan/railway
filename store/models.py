from django.db import models

# Create your models here.
class Store(models.Model):

    product=models.CharField(max_length=200)
    quantity=models.IntegerField()
    price=models.IntegerField()

    def __str__(self):
        return self.product 
