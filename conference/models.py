from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=255)
    capacity = models.PositiveIntegerField()
    projector = models.BooleanField(default=False)
    availability = models.BooleanField(default=False)
    # reservation = models.DateField(null=False)

    def __str__(self):
        return f'{self.name} {self.capacity} {self.projector} {self.availability}'
