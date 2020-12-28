from django.contrib.auth.models import User
from django.db import models


class RememberCards(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user} - {self.location}: {self.notes[:20]}..."
