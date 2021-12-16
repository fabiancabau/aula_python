from django.test import TestCase, Client, client
import json
from ..serializers import TodoItemSerializer
from ..models import TodoItem
from rest_framework import status

client = Client()

class GetAllTodosTest(TestCase):

    def setUp(self):
        TodoItem.objects.create(description='Todo python', color='black')
        TodoItem.objects.create(description='Todo Node', color='White')


    def test_get_all_todos(self):
        response = client.get('/todo')

        todos = TodoItem.objects.all()
        serializer = TodoItemSerializer(todos, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class CreateNewTodo(TestCase):

    def setUp(self):
        self.valid_payload = {
            'description': 'todo lesson',
            'color': 'blue'
        }
        self.invalid_payload = {
            'description': "",
            'color': 'blue'
        }

    def test_create_valid_todo(self):
        response = client.post('/todo', self.valid_payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_todo(self):
        response = client.post('/todo', self.invalid_payload)
        self.assertEqual((response.status_code, status.HTTP_400_BAD_REQUEST))


"""class GetSingleTodoTest(TestCase):

    def setUp(self):
        self.todo1 = TodoItem.objects.create(description='Todo 1', color='black')
        self.todo2 = TodoItem.objects.create(description='Todo 2', color='white')
        self.todo3 = TodoItem.objects.create(description='Todo 3', color='blue')

    def test_get_valid_single_todo(self):
        response = client.get(f'/todo/{self.todo2.todo_item_id}')
        todo = TodoItem.objects.get(pk=self.todo2.todo_item_id)
        serializer = TodoItemSerializer(todo)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)"""

