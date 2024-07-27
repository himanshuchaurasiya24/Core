from django.db import models

# Create your models here. vid at 04:26
class Student (models.Model):
    # id = models.AutoField() --> automatically created by django
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    phone = models.TextField(null=True, blank=True)
    # image = models.ImageField()
    # file = models.FileField()
class Car(models.Model):
    car_name = models.CharField(max_length=100)
    speed = models.IntegerField(default=50)
    def __str__(self) -> str:
        return self.car_name
