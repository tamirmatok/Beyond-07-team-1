from .models import DogOwner
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import pytest

EMAIL = 'testuser@gmail.com'
USERNAME = 'testuser01'
PASSWORD = 'testpassowrd'
DOG_NAME = 'kliford'
FIRST_NAME = 'NEW'
LAST_NAME = 'USER'
PHONE_NUMBER = 1234567890
DOG_RACE = 'lavrador'
DOG_PICTURE_URL = 'https://www.google.com/'
DOG_AGE = 10
DOG_WEIGHT = 6
DOG_GENDER = 'M'


@pytest.fixture
def dogOwner_01():
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
    def test_persist_dog_owner(self, dogOwner_01):
        dogOwner_01.save()
        assert dogOwner_01.user in User.objects.all()
        assert dogOwner_01 in DogOwner.objects.all()

    def test_del_dogowner(self, dogOwner_01):
        dogOwner_01.save()
        dogOwner_01.delete()
        assert dogOwner_01 not in User.objects.all()
        assert dogOwner_01 not in DogOwner.objects.all()

    def test_invalid_email(self, dogOwner_01):
        with pytest.raises(ValidationError, match="'Enter a valid email address.'"):
            DogOwner.create(email='INVALID_EMAIL', username='testuser02', password=PASSWORD,
                            dog_name=DOG_NAME, first_name=FIRST_NAME, last_name=LAST_NAME,
                            phone_number=PHONE_NUMBER, dog_race=DOG_RACE, dog_picture_url=DOG_PICTURE_URL,
                            dog_age=DOG_AGE, dog_weight=DOG_WEIGHT, dog_gender=DOG_GENDER
                            )

    def test_same_username(self, dogOwner_01):
        dogOwner_01.save()
        with pytest.raises(ValidationError, match="Invalid username"):
            DogOwner.create(email=EMAIL, username='testuser01', password=PASSWORD,
                            dog_name=DOG_NAME, first_name=FIRST_NAME, last_name=LAST_NAME,
                            phone_number=PHONE_NUMBER, dog_race=DOG_RACE, dog_picture_url=DOG_PICTURE_URL,
                            dog_age=DOG_AGE, dog_weight=DOG_WEIGHT, dog_gender=DOG_GENDER
                            )

    # def test_invalid_url(self, dogOwner_01):
    #     with pytest.raises(ValidationError, match="Enter a valid URL."):
    #         DogOwner.create(email=EMAIL, username='testuser03', password=PASSWORD,
    #                         dog_name=DOG_NAME, first_name=FIRST_NAME, last_name=LAST_NAME,
    #                         phone_number=PHONE_NUMBER, dog_race=DOG_RACE, dog_picture_url='NOT_A_URL',
    #                         dog_age=DOG_AGE, dog_weight=DOG_WEIGHT, dog_gender=DOG_GENDER
    #                         )

    def test_phone_as_txt(self, dogOwner_01):
        with pytest.raises(ValidationError, match="Invalid phone - phone should be number"):
            DogOwner.create(email=EMAIL, username='invalid_phone', password=PASSWORD,
                            dog_name=DOG_NAME, first_name=FIRST_NAME, last_name=LAST_NAME,
                            phone_number='tests', dog_race=DOG_RACE, dog_picture_url=DOG_PICTURE_URL,
                            dog_age=DOG_AGE, dog_weight=DOG_WEIGHT, dog_gender=DOG_GENDER
                            )

    def test_phone_short(self, dogOwner_01):
        with pytest.raises(ValidationError, match="Invalid phone - phone should be 10 digits"):
            DogOwner.create(email=EMAIL, username='invalid_phone', password=PASSWORD,
                            dog_name=DOG_NAME, first_name=FIRST_NAME, last_name=LAST_NAME,
                            phone_number=123456789, dog_race=DOG_RACE, dog_picture_url=DOG_PICTURE_URL,
                            dog_age=DOG_AGE, dog_weight=DOG_WEIGHT, dog_gender=DOG_GENDER
                            )

    def test_phone_long(self, dogOwner_01):
        with pytest.raises(ValidationError, match="Invalid phone - phone should be 10 digits"):
            DogOwner.create(email=EMAIL, username='invalid_phone', password=PASSWORD,
                            dog_name=DOG_NAME, first_name=FIRST_NAME, last_name=LAST_NAME,
                            phone_number=1234567890123, dog_race=DOG_RACE, dog_picture_url=DOG_PICTURE_URL,
                            dog_age=DOG_AGE, dog_weight=DOG_WEIGHT, dog_gender=DOG_GENDER
                            )
