from django.db import models

# Create your models here.


class TodoItem(models.Model):

    description = models.TextField()
    is_done = models.BooleanField(default=False)
    created_dt = models.DateTimeField(auto_now_add=True)
    color = models.CharField(max_length=250, null=True)