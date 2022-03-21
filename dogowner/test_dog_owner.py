from .models import Dogowner
from django.contrib.auth.models import User
import pytest


EMAIL = 'testuser@gmail.com'
USERNAME = 'testuser'
PASSWORD = 'testpassowrd'
DOG_NAME = 'kliford'
FIRST_NAME = 'NEW'
LAST_NAME = 'USER'
PHONE_NUMBER = 389450357
DOG_RACE = 'lavrador'
DOG_PICTURE_URL = 'http....'
DOG_AGE = 10
DOG_WEIGHT = 6
DOG_GENDER = 'M'


@pytest.fixture
def dog_owner_0():
    return Dogowner(user=User(email=EMAIL,
                              username=USERNAME,
                              password=PASSWORD,),
                    dog_name=DOG_NAME,
                    first_name=FIRST_NAME,
                    last_name=LAST_NAME,
                    phone_number=PHONE_NUMBER,
                    dog_race=DOG_RACE,
                    dog_picture_url=DOG_PICTURE_URL,
                    dog_age=DOG_AGE,
                    dog_weight=DOG_WEIGHT,
                    dog_gender=DOG_GENDER
                    )


@pytest.mark.django_db
class TestDogOwnerModel:

    def test_create_dogowner(self, dog_owner_0):
        assert dog_owner_0.user.username == USERNAME
        assert dog_owner_0.user.email == EMAIL
        assert dog_owner_0.dog_name == DOG_NAME
        assert dog_owner_0.dog_race == DOG_RACE
        assert dog_owner_0.dog_picture_url == DOG_PICTURE_URL
        assert dog_owner_0.dog_age == DOG_AGE
        assert dog_owner_0.dog_weight == DOG_WEIGHT
        assert dog_owner_0.dog_gender == DOG_GENDER

    def test_persist_member(self, dog_owner_0):
        dog_owner_0.user.save()
        dog_owner_0.save()
        assert dog_owner_0.user in User.objects.all()
        assert dog_owner_0 in Dogowner.DogOwners.all()

    def test_del_dog_owner(self, dog_owner_0):
        dog_owner_0.user.save()
        dog_owner_0.save()
        dog_owner_0.user.delete()
        assert dog_owner_0 not in Dogowner.DogOwners.all()
        assert dog_owner_0.user not in User.objects.all()
