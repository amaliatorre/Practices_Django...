
from django.urls import path, include
from rest_framework import routers

from practice2 import views

router = routers.DefaultRouter()
router.register(r'tarea', views.TareaViewSet)
router.register(r'tarea2', views.TareaViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('', views.lista_tareas, name='lista_tareas'),
    path('lista', views.ListaTarea.as_view(), name='lista_tareas2'),
    path('delete/<int:tarea_id>', views.borrar_tareas, name='delete'),
    path('api/lista_tareas/', views.TareaViewSet.as_view({'get': 'list'}), name='lista_tareas_api_view'),
    path('api/lista_tareas/<int:pk>', views.TareaViewSet.as_view({'get': 'retrieve'}), name='tareas_api_view'),
    path('new', views.create_task_form, name='create_task'),
    path('new2', views.CreateTask.as_view(), name='new_create_task'),
]

app_name = "practice2"
