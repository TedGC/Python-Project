from django.db import models
from django.contrib.auth.models import User

# Create your models here.

MEAL_TYPE = (
    ('starters', 'Starters'),
    ('salads', 'Salads'),
    ('main_dishes', 'Main_Dishes'),
    ('desserts', 'Desserts')
)

STATUS = { 
    (0,'Unavailable'),
    (1, "Available"),
}


class Item(models.Model):
    menu_name = models.CharField(max_length=80, unique=True)
    menu_cat = models.CharField(choices=MEAL_TYPE)
    description = models.CharField(max_length=1000)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    author = models.ForeignKey(User, on_delete=models.PROTECT) #CASCADE
    status = models.IntegerField(choices=STATUS, default=1)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.menu_name
