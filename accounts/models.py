from django.db import models


class user(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.TextField() 
    def __str__(self):
        return self.first_name

# Create your models here.
