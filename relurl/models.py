from django.db import models

# Create your models here.

class Device (models.Model):
    name = models.CharField(max_length=128)
    fw_version = models.CharField(max_length=32)
    serial = models.CharField(max_length=64, unique=True)
    vendor = models.CharField(max_length=64)

    def __str__(self):
        return self.name


