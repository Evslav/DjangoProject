from django.db import models

class lead(models.Model):
    name = models.CharField(max_length=128)
    phone = models.CharField(max_length=20, default='NULL')


class uinfo(models.Model):
    user_agent = models.CharField(max_length=200, default='NULL')
    ip = models.CharField(max_length=20, default='NULL')


# Create your models here.
