from django.db import models

# Modelo: Crea un modelo ea un modelo llamado Tarea con los siguientes campos:
# titulo (CharField)
# descripcion (TextField)
# fecha_creacion (DateField)
# completada (BooleanField)

class Tarea(models.Model):
    titulo = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=300)
    fecha_creacion = models.DateField(auto_now=True)
    completada = models.BooleanField(default=False)

