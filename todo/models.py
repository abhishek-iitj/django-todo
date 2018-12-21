from django.db import models


class ToDo(models.Model):
    message = models.CharField(max_length=500)
    name = models.CharField(max_length=500)
    time = models.DateTimeField()
