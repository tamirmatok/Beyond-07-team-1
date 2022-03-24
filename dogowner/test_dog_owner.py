from .models import Dogowner
from django.contrib.auth.models import User
import pytest
import logging

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

LOGGER = logging.getLogger(__name__)


@pytest.fixture
def dog_owner_0():
    return User(email=EMAIL,
                username=USERNAME,
                password=PASSWORD,
                dogowner=Dogowner(dog_name=DOG_NAME,
                                  first_name=FIRST_NAME,
                                  last_name=LAST_NAME,
                                  phone_number=PHONE_NUMBER,
                                  dog_race=DOG_RACE,
                                  dog_picture_url=DOG_PICTURE_URL,
                                  dog_age=DOG_AGE,
                                  dog_weight=DOG_WEIGHT,
                                  dog_gender=DOG_GENDER
                                  )
                )


@pytest.mark.django_db
class TestDogOwnerModel:
    def test_create_dogowner(self, dog_owner_0):
        assert dog_owner_0.username == USERNAME
        assert dog_owner_0.email == EMAIL
        assert dog_owner_0.dogowner.dog_name == DOG_NAME
        assert dog_owner_0.dogowner.dog_race == DOG_RACE
        assert dog_owner_0.dogowner.dog_picture_url == DOG_PICTURE_URL
        assert dog_owner_0.dogowner.dog_age == DOG_AGE
        assert dog_owner_0.dogowner.dog_weight == DOG_WEIGHT
        assert dog_owner_0.dogowner.dog_gender == DOG_GENDER

    def test_persist_member(self, dog_owner_0):
        dog_owner_0.save()
        assert dog_owner_0 in User.objects.all()
        assert dog_owner_0.dogowner in Dogowner.objects.all()

    def test_del_dog_owner(self, dog_owner_0):
        dog_owner_0.save()
        dog_owner_0.delete()
        assert dog_owner_0 not in User.objects.all()
        assert dog_owner_0.dogowner not in Dogowner.objects.all()
