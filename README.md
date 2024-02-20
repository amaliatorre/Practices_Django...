# Practices_Django...
Different nivel exercises to practice django, setquery, rest... to Junior position

Ejercicio 1: Crear un Modelo y QuerySet

Modelo:
Crea un modelo llamado Producto con campos como nombre, precio y cantidad en stock.

QuerySet:
Implementa un QuerySet que filtre los productos con un precio mayor a $50.

Ejercicio 2: Crear una estructura basica con serializadores

Modelo:
Crea un modelo llamado Tarea con los siguientes campos:
titulo (CharField)
descripcion (TextField)
fecha_creacion (DateField)
completada (BooleanField)

Serialize:
Crea un serializador llamado TareaSerializer que utilice el modelo Tarea y serialice todos los campos.
Vista de la API (views.py):

Views:
Crea una vista basada en clase llamada ListaTareasAPIView que liste todas las tareas. Utiliza el serializador TareaSerializer y el modelo Tarea.
Crea una vista llamada lista_tareas que renderice un template lista_tareas.html. Esta vista debe mostrar todas las tareas.

Template(lista_tareas.html):
Crea un template que muestre la lista de tareas. 


Ejercicio 3 
Desarrolla una aplicación web para la gestión de una biblioteca. La aplicación debe permitir a los usuarios ver la lista de libros disponibles, buscar libros por título o autor, y poder reservar o prestar libros.

Modelos:

Libro:
Atributos: Título, Autor, ISBN, Descripción, Disponibilidad (booleano).
Métodos: prestar(), devolver().

Usuario:
Atributos: Nombre, Apellido, Email.
Relación con Libro: Muchos a muchos (un usuario puede tener varios libros prestados, y un libro puede estar prestado a varios usuarios).

Vistas:
  Página principal:
    Lista de todos los libros disponibles con enlaces a detalles.
  Página de detalles del libro:
    Información detallada del libro.
    Botones para prestar o devolver el libro (si está disponible o prestado).
  Página de búsqueda:
    Formulario de búsqueda por título o autor.
    Resultados de búsqueda con enlaces a detalles.
    
Templates:
Template para la página principal que muestra la lista de libros.
Template para la página de detalles del libro.
Template para la página de búsqueda.

Tests:
Escribe tests para asegurar el funcionamiento correcto de las siguientes funcionalidades:
  
  Crear un libro y verificar que se muestra en la lista de libros.
  Prestar un libro y verificar que se marca como no disponible.
  Devolver un libro y verificar que se marca como disponible.
  Buscar libros por título y autor y verificar los resultados.

URLs:
Configura las URLs para ambas vistas (API y con templates).

Requisitos extra:
  Todo en ingles
  Documentar 
