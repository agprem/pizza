from django.db import models

# Create your models here.
class Pizza(models.Model):
    Regular='Regular'
    Square='Small'
    type_choices=((Regular,'Regular'),(Square,'Square'))

    types=models.CharField(max_length=30,choices=type_choices,default=Regular)
    size=models.CharField(max_length=10,null=False)
    toppings=models.CharField(max_length=20,null=False)

    def _str_():
        return "Pizza created"
