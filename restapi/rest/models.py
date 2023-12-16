from typing import Any
from django.db import models

# Create your models here.

class taskManager(models.Model):
    title = models.CharField(max_length=150)
    description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    is_completed=models.BooleanField(default=False)

    def __str__(self) :
        return self.title