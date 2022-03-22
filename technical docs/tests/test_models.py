from django.test import TestCase, Client
from locationgameapp.models import task
from django.contrib.auth import get_user_model


class TestModels(TestCase):

    # Sets up a new task
    def setUp(self):
        task.objects.create(taskName='Test', description='Description', longitude='1', latitude='2')

    # Tests that labels are correct
    def test_task_label(self):
        task_ = task.objects.get(id=1)
        label = task_._meta.get_field('taskName').verbose_name
        self.assertEqual(label, 'taskName')

    def test_description_label(self):
        description_ = task.objects.get(id=1)
        label = description_._meta.get_field('description').verbose_name
        self.assertEqual(label, 'description')

    def test_longitude_label(self):
        longitude_ = task.objects.get(id=1)
        label = longitude_._meta.get_field('longitude').verbose_name
        self.assertEqual(label, 'longitude')

    def test_latitude_label(self):
        latitude_ = task.objects.get(id=1)
        label = latitude_._meta.get_field('latitude').verbose_name
        self.assertEqual(label, 'latitude')


    # Tests the maximum length of the task name
    def test_taskName_max_length(self):
        task_ = task.objects.get(id=1)
        max_length = task_._meta.get_field('taskName').max_length
        self.assertEqual(max_length, 120)
