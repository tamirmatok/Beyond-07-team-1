from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import URLValidator


def validate_username(username):
    if User.objects.filter(username=username).exists():
        raise ValidationError("Invalid username")


def validate_url(url):
    if url:
        URLValidator(url)


def validate_phone(value):
    if isinstance(value, int):
        if len(str(value)) != 10:
            raise ValidationError("Invalid phone - phone should be 10 digits")
    else:
        raise ValidationError("Invalid phone - phone should be number")
