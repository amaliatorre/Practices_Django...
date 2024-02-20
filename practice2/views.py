from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView
from rest_framework import viewsets

from .forms.create_task_form import TareaForm
from .models import Tarea
from .serializes import MinTareaSerializer



# Crea una vista basada en clase llamada ListaTareasAPIView que liste todas las tareas.
# (Utiliza el serializador TareaSerializer y el modelo Tarea).
# Crea una vista llamada lista_tareas que renderice un template lista_tareas.html.
# (Esta vista debe mostrar todas las tareas.)

# para uso de front externos


class TareaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Tarea.objects.all()
    serializer_class = MinTareaSerializer


class ListaTarea(TemplateView):
    template_name = 'lista_tareas.html'

    def get_context_data(self, **kwargs):
        list_all_task = Tarea.objects.all().distinct()
        return {'list_all_task': list_all_task}


# uso con las pantillas de django
def lista_tareas(request):
    # list_all_task = Tarea.objects.all().order_by('-fecha_creacion')
    list_all_task = Tarea.objects.all().distinct()

    return render(request, 'lista_tareas.html', {'list_all_task': list_all_task})


def borrar_tareas(request, tarea_id=None):
    tareas_a_borrar = Tarea.objects.filter(id=tarea_id)
    tareas_a_borrar.delete()
    return redirect(reverse("practice2:lista_tareas"))


def create_task_form(request: HttpRequest) -> HttpResponse:

    form = TareaForm(instance=Tarea.objects.get(), data=request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()

            new_titulo = form.cleaned_data['titulo']
            new_desciption = form.cleaned_data['descripcion']

            new_task = Tarea.objects.create(titulo=new_titulo, descripcion=new_desciption)
            a = Tarea.objects.all()
            for i in a.values('titulo'):
                print(i.titulo)

        else:
            form = TareaForm()

    return render(request, 'create.html', {'form': form})


class CreateTask(TemplateView):
    template_name = 'create.html'

    def get_context_data(self, **kwargs):
        form = TareaForm(self.request.POST)
        return {'form': form}

    def post(self, request, *args, **kwargs):
        context = self.get_context_data()
        form = context["form"]
        if form.is_valid():
            new_titulo = form.cleaned_data['titulo']
            new_desciption = form.cleaned_data['descripcion']

            new_task = Tarea(titulo=new_titulo, descripcion=new_desciption)
            new_task.save()
        return render(request, self.template_name, context)



