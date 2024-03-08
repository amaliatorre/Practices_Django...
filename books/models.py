from django.db import models

""" Libro: Atributos: Título, Autor, ISBN, Descripción, Disponibilidad (booleano). 
Métodos: prestar(), devolver().

Usuario: Atributos: Nombre, Apellido, Email. 
Relación con Libro: Muchos a muchos 
(un usuario puede tener varios libros prestados, y un libro puede estar prestado a varios usuarios). """


class Book(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    author = models.CharField(max_length=100, blank=True, null=True)
    isbn = models.CharField(max_length=17, blank=False, null=False)
    description = models.CharField(max_length=400, blank=True, null=True)
    availability = models.BooleanField(default=True)


class User(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    surname = models.CharField(max_length=50, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    book = models.ManyToManyField(Book, on_delete=models.CASCADE, )
