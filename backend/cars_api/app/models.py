from django.db import models

class Car(models.Model):
    make = models.TextField()
    model = models.TextField()
    year = models.PositiveSmallIntegerField()

    def __str__(self):
        return f'${self.year} ${self.make} ${self.model}'
