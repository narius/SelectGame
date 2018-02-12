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
class model_game(models.Model):
    name=models.CharField(max_length=30, verbose_name="Name")
    category=models.ManyToManyField(model_category)
    comment=models.TextField(verbose_name="Comment")
    class Meta:
        verbose_name = "game"
        verbose_name_plural = "games"
    def __str__(self):
        return self.name
#toppings = models.ManyToManyField(Topping)

#Model for ratings
