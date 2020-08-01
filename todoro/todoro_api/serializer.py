from rest_framework import serializers
from .models import Task
from .models import Project


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = (
            'title',
            'description',
            'start_date',
            'pomodoro_counts'
        )


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = (
            'title',
            'description',
            'start_date',
            'pomodoro_counts',
            'task'
        )
