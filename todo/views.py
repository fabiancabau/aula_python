import traceback

from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from todo.models import TodoItem
from todo.serializers import TodoItemSerializer


class TodoView(APIView):

    def get(self, request):
        items = TodoItem.objects.all()
        serialized_items = TodoItemSerializer(items, many=True).data

        return Response(serialized_items, status=status.HTTP_200_OK)

    def post(self, request):
        item = TodoItem.objects.create(
            description=request.data.get("description"),
            color=request.data.get("color", "branco")
        )

        serialized_item = TodoItemSerializer(item).data
        return Response(serialized_item, status=status.HTTP_201_CREATED)

class TodoDetailView(APIView):

    def get(self, request, todo_item_id: int):
        try:
            todo_item = TodoItem.objects.get(id=todo_item_id)
            serialized_item = TodoItemSerializer(todo_item).data
            return Response(serialized_item)
        except TodoItem.DoesNotExist:
            return Response({"message": "Item does not exist"}, status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return Response({"message": "Error"}, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, todo_item_id: int) -> Response:

        try:
            todo_item = TodoItem.objects.get(id=todo_item_id)
            todo_item.delete()

            return Response({"message": "Item removed successfully"})
        except TodoItem.DoesNotExist:
            return Response({"message": "Item does not exist"}, status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return Response({"message": "Error"}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, todo_item_id):

        try:
            todo_item = TodoItem.objects.get(id=todo_item_id)
            todo_item.description = request.data.get("description", todo_item.description)
            todo_item.color = request.data.get("color", todo_item.color)
            todo_item.save()

            return Response(TodoItemSerializer(todo_item).data)
        except TodoItem.DoesNotExist:
            return Response({"message": "Item does not exist"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print(traceback.format_exc())
            return Response({"message": "Error"}, status=status.HTTP_400_BAD_REQUEST)




#
# @api_view(http_method_names=['GET', 'POST'])
# def get_nome(request):
#
#     if request.method == 'GET':
#         return Response("oi")
#
#     if request.method == "POST":
#         return Response("post")