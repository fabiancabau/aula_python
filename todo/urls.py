from django.urls import path

from todo.views import TodoView, TodoDetailView

urlpatterns = [
    path('', TodoView.as_view()),
    path('/<int:todo_item_id>', TodoDetailView.as_view())
]