from django.db import models

# Create your models here.
class Customer(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=150, unique=False)

    def __str__(self):
        return self.name