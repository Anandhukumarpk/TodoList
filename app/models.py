from django.db import models
from django.utils import timezone


class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    completed = models.BooleanField(default=False)
    created_at = models.CharField(max_length=30 , default=timezone.now)



    def __str__(self):
        return self.title
