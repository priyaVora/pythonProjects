from django.db import models

# Create your models here.
class Animal(models.Model):
    animal_id = models.AutoField(primary_key=True)
    animal_type = models.CharField(max_length=20)
    sound = models.CharField(max_length=10)
    def __int__(self, type ,sound):
        self.sound = sound
        self.type = type


class Dog(Animal):
    name = models.CharField(max_length=30, null=False)
    def __int__(self, name, type, sound):
       self.name = name
       super().__int__(self, type, sound)
