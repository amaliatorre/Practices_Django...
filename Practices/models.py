from django.db import models
#models.py
# Modelo:
# Crea un modelo llamado Producto con campos como nombre, precio y cantidad en stock.
# QuerySet:
# Implementa un QuerySet que filtre los productos con un precio mayor a $50.

class Product(models.Model):
    name = models.CharField(max_length=40)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.PositiveIntegerField()







