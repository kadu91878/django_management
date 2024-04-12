from rest_framework import generics

from models.tasks import Tasks
from serializers.tasks_serializer import TasksSerializer


class TasksListCreateAPIView(generics.ListCreateAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer


class TasksRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer