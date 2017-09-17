from django.db import models

class lead(models.Model):
    name = models.CharField(max_length=128)
    phone = models.CharField(max_length=20)


# Create your models here.
