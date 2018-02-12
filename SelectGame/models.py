from django.db import models

# Create your models here.

#Model for categories
class model_category(models.Model):
    name = models.CharField(max_length=30,
                            verbose_name="Name")
    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"
    def __str__(self):
        return self.name

#Model for games
#toppings = models.ManyToManyField(Topping)

#Model for ratings
