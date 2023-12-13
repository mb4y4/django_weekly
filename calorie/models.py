from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Food(models.Model):
    name = models.CharField(max_length=255)
    calories = models.PositiveIntegerField()
    date_added = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name