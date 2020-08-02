from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=40)
    description = models.CharField(max_length=255, null=True)
    start_date = models.DateTimeField(null=True)
    pomodoro_counts = models.IntegerField(default=1)
    project = models.ForeignKey(
        'Project',
        on_delete=models.CASCADE,
        null=True
    )

    def __str__(self):
        return f"{self.title}"


class Project(models.Model):
    title = models.CharField(max_length=40)
    description = models.CharField(max_length=255, null=True)
    start_date = models.DateTimeField(null=True)
    pomodoro_counts = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.title}"

