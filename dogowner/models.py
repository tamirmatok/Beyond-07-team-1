from django.db import models
from django.contrib.auth.models import User


class Gender(models.TextChoices):
    Male = 'M', 'Male'
    Female = 'F', 'Female'
    Unknown = 'UN', 'Unknown'


class Dogowner(models.Model):

    user = models.OneToOneField(User,
                                null=True,
                                on_delete=models.CASCADE,
                                )
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    phone_number = models.IntegerField()
    dog_name = models.CharField(max_length=15)
    dog_race = models.CharField(max_length=15)
    dog_picture_url = models.CharField(max_length=1000)
    dog_age = models.IntegerField()
    dog_weight = models.FloatField()
    dog_gender = models.CharField(
        max_length=2,
        choices=Gender.choices,
        default='M',)

    DogOwners = models.Manager()

    def __str__(self):
        return self.first_name + self.last_name
