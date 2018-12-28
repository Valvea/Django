from django.db import models
from .utills import get_default_category


class Category(models.Model):
    name = models.CharField(
        max_length=250,
    )
    description = models.TextField(
        null=True,
        blank=True,
    )



    modified = models.DateTimeField(
        auto_now=True,

    )

    created = models.DateTimeField(
        auto_now_add=True,

    )

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=250)

    description = models.TextField(
        null=True,
        blank=True
    )

    image=models.ForeignKey(
        'images.image',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )


    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        default=get_default_category
        #default=1

    )

    cost = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0,
    )

    modified = models.DateTimeField(
        auto_now=True,

    )

    created = models.DateTimeField(
        auto_now_add=True,

    )

    short_description = models.TextField()

    def __str__(self):
        return self.name
