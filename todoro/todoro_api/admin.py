from django.contrib import admin
from .models import Task
from .models import Project


class TaskAdmin(admin.ModelAdmin):
    pass

admin.site.register(Task, TaskAdmin)

class ProjectAdmin(admin.ModelAdmin):
    pass

admin.site.register(Project, ProjectAdmin)

