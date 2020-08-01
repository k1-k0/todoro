from django.shortcuts import render

from rest_framework import viewsets

from .serializer import TaskSerializer
from .serializer import ProjectSerializer

from .models import Task
from .models import Project


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('title')
    serializer_class = TaskSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all().order_by('title')
    serializer_class = ProjectSerializer

