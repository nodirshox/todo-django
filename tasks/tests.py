from django.test import TestCase
from django.urls import reverse

from .models import Task

class TaskModelTest(TestCase):
    def setUp(self):
        Task.objects.create(title='first task', body='description')

    def test_text_content(self):
        task = Task.objects.get(id=1)
        expected_object_title = f'{task.title}'
        expected_object_body = f'{task.body}'
        self.assertEqual(expected_object_title, 'first task')
        self.assertEqual(expected_object_body, 'description')

class HomePageViewTest(TestCase):
    def SetUp(self):
        Post.objects.create(title='another task')

    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
    
    def test_view_by_url_name(self):
        resp = self.client.get(reverse('all_task'))
        self.assertEqual(resp.status_code, 200)
    
    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('all_task'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'all_task.html')