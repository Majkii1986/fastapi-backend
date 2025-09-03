from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()  # 👈 toto je dôležité, inak spadne na basename error
    serializer_class = TaskSerializer
