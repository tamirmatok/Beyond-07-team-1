from .models import DogOwner
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
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
def dogOwner01():
    return DogOwner.create(email=EMAIL,
                           username=USERNAME,
                           password=PASSWORD,
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
    def test_persist_dog_owner(self, dogOwner01):
        dogOwner01.save()
        assert dogOwner01.user in User.objects.all()
        assert dogOwner01 in DogOwner.objects.all()

    def test_del_dogowner(self, dogOwner01):
        dogOwner01.save()
        dogOwner01.delete()
        assert dogOwner01 not in User.objects.all()
        assert dogOwner01 not in DogOwner.objects.all()


@pytest.mark.parametrize(
    "email, username, password, dog_name, first_name, last_name, phone_number, dog_race,"
    " dog_picture_url, dog_age, dog_weight, dog_gender",
    [
        ('NOT_AN_EMAIL', 'same_user_name', 'password123', 'dog_name', 'first_name', 'last_name',
         232323223, 'dog_race', 'dog_picture_url', 4, 2, 'M'),
        ('email@address.com', 'same_user_name', 'password123', 'dog_name', 'first_name', 'last_name',
         232323223, 'dog_race', 'dog_picture_url', 3, 1, 'M'),
        ('email@address.com', 'same_user_name', 'password123', 'dog_name', 'first_name', 'last_name',
         232323223, 'dog_race', 'dog_picture_url', 2, 5, 'M'),
        ('email@address.com', 'username3', 'password123', 'dog_name', 'first_name', 'last_name',
         232323223, 'dog_race', 'dog_picture_url', 1, 6, 'Not_in_gender'),
    ])
@pytest.mark.django_db
def test_value_error(email, username, password, dog_name, first_name, last_name, phone_number,
                     dog_race, dog_picture_url, dog_age, dog_weight, dog_gender):
    with pytest.raises(ValidationError, match="Enter a valid email address."):
        dogOwner = DogOwner.create(email=email,
                                   username=username,
                                   password=password,
                                   dog_name=dog_name,
                                   first_name=first_name,
                                   last_name=last_name,
                                   phone_number=phone_number,
                                   dog_race=dog_race,
                                   dog_picture_url=dog_picture_url,
                                   dog_age=dog_age,
                                   dog_weight=dog_weight,
                                   dog_gender=dog_gender)

# @pytest.mark.parametrize(
#     "email, username, password, dog_name, first_name, last_name, phone_number, dog_race,"
#     " dog_picture_url, dog_age, dog_weight, dog_gender",
#     [
#         ('email@address.com', 'username1', 'password123', 'dog_name', 'first_name', 'last_name',
#          232323223, 'dog_race', 'dog_picture_url', 'not_number_error', 2, 'M'),
#         ('', 'same_user_name', 'password123', 'dog_name', 'first_name', 'last_name',
#          232323223, 'dog_race', 'dog_picture_url', 3, 1, 'M'),
#         ('email@address.com', 'same_user_name', 'password123', 'dog_name', 'first_name', 'last_name',
#          232323223, 'dog_race', 'dog_picture_url', 2, 5, 'M'),
#         ('email@address.com', 'username3', 'password123', 'dog_name', 'first_name', 'last_name',
#          232323223, 'dog_race', 'dog_picture_url', 1, 6, 'Not_in_gender'),
#     ])
