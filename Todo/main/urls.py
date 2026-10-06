from django.urls import path
from .views import TaskView, AddTaskView, UpdateTaskView


urlpatterns = [
    path('tasks', TaskView.as_view(), name='task-list'),
    path('add-task', AddTaskView.as_view(), name='add-task'),
    path('update-task/<int:pk>', UpdateTaskView.as_view(), name='update-task'),
]