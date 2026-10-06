from django.shortcuts import render
from .models import TaskModel
from .serializers import TaskSerializer

from rest_framework.views import APIView, Response


class TaskView(APIView):
    def get(self, request):
        tasks = TaskModel.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
    

class AddTaskView(APIView):
    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Task added successfully"}, status=201)
        return Response(serializer.errors, status=400)
    
    
class UpdateTaskView(APIView):
    def put(self, request, pk):
        try:
            task = TaskModel.objects.get(pk=pk)
        except TaskModel.DoesNotExist:
            return Response({"error": "Task not found"}, status=404)

        serialiser = TaskSerializer(task, data=request.data, partial=True)
        if serialiser.is_valid():
            serialiser.save()
            return Response({"message": "Task updated successfully"}, status=200)
        return Response(serialiser.errors, status=400)