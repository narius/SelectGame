from django.db import models
from django.utils.translation import gettext

# Create your models here.


class Category(models.Model):
    '''
        Model for categories
    '''
    name = models.CharField(max_length=30,
                            verbose_name=gettext("name"))

    class Meta:
        verbose_name = gettext("category")
        verbose_name_plural = gettext("categories")
        ordering = ['name']

    def __str__(self):
        return self.name
