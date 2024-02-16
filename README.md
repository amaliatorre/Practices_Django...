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
Serializador (serializers.py):

Serialize:
Crea un serializador llamado TareaSerializer que utilice el modelo Tarea y serialice todos los campos.
Vista de la API (views.py):

Views:
Crea una vista basada en clase llamada ListaTareasAPIView que liste todas las tareas. Utiliza el serializador TareaSerializer y el modelo Tarea.
Crea una vista llamada lista_tareas que renderice un template lista_tareas.html. Esta vista debe mostrar todas las tareas.

URLs:
Configura las URLs para ambas vistas (API y con templates).

Template(lista_tareas.html):
Crea un template que muestre la lista de tareas. 
