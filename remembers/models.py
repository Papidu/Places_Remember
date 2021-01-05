from django.contrib.auth.models import User
from django.db import models
from django.contrib.gis.db.models import PointField

class RememberCards(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location_name = models.CharField(max_length=255)
    location = PointField(srid=4326)
    image = models.CharField(max_length=255)
    notes = models.TextField(blank=True, null=True)
    # - {self.location} -

    def __str__(self):
        return f"{self.user} - {self.location} - {self.location_name}: {self.notes[:20]}..."
