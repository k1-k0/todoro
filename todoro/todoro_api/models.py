from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=40)
    description = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    pomodoro_counts = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.title}"


class Project(models.Model):
    title = models.CharField(max_length=40)
    description = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    pomodoro_counts = models.IntegerField(default=1)

    task = models.ForeignKey(
        'Task',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.title}"

