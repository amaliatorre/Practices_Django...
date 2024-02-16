from Practices.models import Product
from typing import List
from django.shortcuts import render
#views.py
def up_to_50_euros(request) -> List[Product]:

    # traer de la bbdd todos los productor que cumplan esta condicion...
    # crear la lista para mandar

    query_up_to_50_euros = Product.objects.filter(price__gte=50)
    listo_of_products_up_to_50 = list(query_up_to_50_euros)

    return render(request, 'mi_app/template.html', {'listo_of_products_up_to_50': listo_of_products_up_to_50})


