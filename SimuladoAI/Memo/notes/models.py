from typing import Text
from django.db import models


class Note(models.Model):
    title = models.CharField(max_length=100)
    details = models.TextField(max_length=400)
    def __str__(self):
        id = self.id
        content =str(id)+"."+self.title
        return content
