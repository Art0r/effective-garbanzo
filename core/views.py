from rest_framework import viewsets
from core.serializers import TaskSerializer
from core.models import Task
from rest_framework import permissions


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    http_method_names = ('get', 'put', 'post', 'delete')
    permission_classes = (permissions.AllowAny,)
    serializer_class = TaskSerializer
