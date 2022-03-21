from django.db import models
from django.contrib.auth.models import User
from django.core.validators import validate_email
from .validators import validate_url, validate_username, validate_phone


class Gender(models.TextChoices):
    Male = 'M', 'Male'
    Female = 'F', 'Female'
    Unknown = 'UN', 'Unknown'


class DogOwner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=15, blank=True)
    last_name = models.CharField(max_length=15, blank=True)
    phone_number = models.IntegerField(null=True, blank=True)
    dog_name = models.CharField(max_length=15, blank=True)
    dog_race = models.CharField(max_length=15, blank=True)
    dog_picture_url = models.CharField(max_length=1000, blank=True)
    dog_age = models.IntegerField(null=True, blank=True)
    dog_weight = models.FloatField(null=True, blank=True)
    dog_gender = models.CharField(
        max_length=2,
        choices=Gender.choices,
        default='UN', blank=True)

    def __str__(self):
        return self.first_name + self.last_name

    @staticmethod
    def create(email, username, password, dog_name,
               first_name, last_name, phone_number,
               dog_race, dog_picture_url, dog_age,
               dog_weight, dog_gender):
        # Validation
        validate_email(email)
        validate_username(username)
        validate_url(dog_picture_url)
        validate_phone(phone_number)

        # Creating the objects
        new_dog_owner = DogOwner(user=User.objects.create_user(username=username,
                                                               email=email,
                                                               password=password
                                                               ),
                                 first_name=first_name,
                                 last_name=last_name,
                                 phone_number=phone_number,
                                 dog_name=dog_name,
                                 dog_race=dog_race,
                                 dog_picture_url=dog_picture_url,
                                 dog_age=dog_age,
                                 dog_weight=dog_weight,
                                 dog_gender=dog_gender
                                 )

        new_dog_owner.user.save()
        new_dog_owner.save()
        return new_dog_owner
