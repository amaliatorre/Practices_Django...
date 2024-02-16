from django.db import models

# Modelo: Crea un modelo llamado Producto con campos como nombre, precio y cantidad en stock.

class Product(models.Model):
    name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.PositiveIntegerField()

