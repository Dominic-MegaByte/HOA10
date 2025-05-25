from django.db import models

from django.db import models

class Sign(models.Model):
    name = models.CharField(max_length=100)
    months = models.CharField(max_length=100)
    element = models.CharField(max_length=100)
    symbol = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100)
    compatibility = models.CharField(max_length=300)
    personalities = models.CharField(max_length=300)
    weakness = models.CharField(max_length=300)
    modalities = models.CharField(max_length=100)

    def __str__(self):
        return self.name
