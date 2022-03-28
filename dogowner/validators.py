from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import URLValidator


def validate_username(username):
    if User.objects.filter(username=username).exists():
        raise ValidationError("Invalid username")


def validate_url(url):
    validator = URLValidator()
    if url:
        validator(url)
