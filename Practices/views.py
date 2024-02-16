from Practices.models import Product
from django.shortcuts import render
# views.py

# la realidad es que el metodo no devuelve una lista sino una respuesta donde apunto a una vista html
# a la cual le pasas la lista


def up_to_50_euros(request):

    # traer de la bbdd todos los productor que cumplan esta condicion mayor igual...
    # "crear la lista para mandar" - no hace falta ya que la respuesta de queryset ya te lo trae en forma de lista

    listo_of_products_up_to_50 = Product.objects.filter(price__gte=50)

    return render(request, 'template.html', {'listo_of_products_up_to_50': listo_of_products_up_to_50})
