from rest_framework import serializers
from core.models import Task


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'title', 'description', 'department',)
