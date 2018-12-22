from django.db import models
from django.contrib.auth.models import AbstractUser


class Accountuser(AbstractUser):
    avatar=models.ForeignKey(
        'images.image',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
    phone=models.CharField(
        max_length=11,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.username

# Create your models here.
