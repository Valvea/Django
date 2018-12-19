from django.db import models


class Product(models.Model):
    name=models.CharField(max_length=250)
    description = models.TextField()
    short_description = models.TextField()