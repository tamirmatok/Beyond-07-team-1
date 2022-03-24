from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Gender(models.TextChoices):
    Male = 'M', 'Male'
    Female = 'F', 'Female'
    Unknown = 'UN', 'Unknown'


class Dogowner(models.Model):
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
        default='M', blank=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Dogowner.objects.create(user=instance, dog_name=instance.dogowner.dog_name,
                                first_name=instance.dogowner.first_name,
                                last_name=instance.dogowner.last_name,
                                phone_number=instance.dogowner.phone_number,
                                dog_race=instance.dogowner.dog_race,
                                dog_picture_url=instance.dogowner.dog_picture_url,
                                dog_age=instance.dogowner.dog_age,
                                dog_weight=instance.dogowner.dog_weight,
                                dog_gender=instance.dogowner.dog_gender)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.dogowner.save()
