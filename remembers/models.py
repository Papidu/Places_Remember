from django.contrib.auth.models import User
# from django.db import models
from django.contrib.gis.db import models


class RememberCards(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location_name = models.CharField(max_length=255)
    location = models.PointField(srid=4326)
    image = models.CharField(max_length=255)
    notes = models.TextField(blank=True, null=True)
    #mpoly = MultiPolygonField()

    def __str__(self):
        return f"{self.user} - {self.location} - {self.location_name}: {self.notes[:20]}..."

    class Meta:
        verbose_name = 'Воспоминание'
        verbose_name_plural = 'Воспоминания'




















