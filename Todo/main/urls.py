from django.urls import path
from .views import TaskView, AddTaskView, UpdateTaskView, DeleteTaskView


urlpatterns = [
    path('tasks', TaskView.as_view(), name='task-list'),
    path('add-task', AddTaskView.as_view(), name='add-task'),
    path('update-task/<int:pk>', UpdateTaskView.as_view(), name='update-task'),
    path('delete-task/<int:pk>', DeleteTaskView.as_view(), name='delete-task'),
]