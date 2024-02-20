
from django.test import TestCase

from practice2.models import Tarea


class TareaTestCase(TestCase):

    def setUp(self):
        Tarea.objects.create(titulo='primera tarea', descripcion='prueba test primera tarea')
        Tarea.objects.create(titulo='segunda tarea', descripcion='prueba test segunda tarea')

    @staticmethod
    def test_get_tasks():
        result = []

        try:

            first_task = Tarea.objects.get(titulo='primera tarea')
            second_task = Tarea.objects.get(titulo='segunda tarea')

            result = [first_task, second_task]
        except Tarea.DoesNotExist:
            print(f'Some task doesn´t exist, please try later')

        return result

    def test_tarea_description(self):

        list_task = self.test_get_tasks()

        for task in list_task:
            if task.titulo == 'primera tarea':
                self.assertEqual(task.descripcion, 'prueba test primera tarea')

            if task.titulo == 'segunda tarea':
                self.assertEqual(task.descripcion, 'prueba test segunda tarea')

    def test_not_complete_new_task(self):
        list_task = self.test_get_tasks()

        for task in list_task:
            if task:
                self.assertFalse(task.completada)

