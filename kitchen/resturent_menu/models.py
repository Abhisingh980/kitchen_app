from django.db import models
from django.contrib.auth.models import User


MEAL_TYPE = (("starters", "Starters"),
             ("salad", "Salad"),
             ("main_dish", "Main_dishes"),
             ("desert", "Desert"))


STATUS = (
    (0, "Unavailable"),
    (1, "Available")
)


class Items(models.Model):
    meal = models.CharField(max_length=1000, unique=True)
    des = models.CharField(max_length=2000)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    meal_type = models.CharField(max_length=250, choices=MEAL_TYPE)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    status = models.IntegerField(choices=STATUS, default=0)
    date_created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.meal)