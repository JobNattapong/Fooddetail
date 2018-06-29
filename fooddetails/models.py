from django.db import models

class Food(models.Model):
    food_text = models.TextField(default='')
    sugar = models.IntegerField(default=0)
    protein = models.IntegerField(default=0)
