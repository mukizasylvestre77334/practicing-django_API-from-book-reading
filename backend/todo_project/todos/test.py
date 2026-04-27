from django.test import TestCase
from .models import Todo

class TodoModelTest(TestCase):
  @classmethod
  def setUpTestData(cls):
    Todo.objects.create(title='the real world', body='mostly entertainment')
  def test_title_content(self):
    todo=Todo.objects.get(id=1)
    expected_title_name=f'{todo.title}'
    self.assertEqual(expected_title_name,'the real world')
  def test_body_content(self):
    todo=Todo.objects.get(id=1)
    expected_body_content=f'{todo.body}'
    self.assertEqual(expected_body_content,'mostly entertainment')