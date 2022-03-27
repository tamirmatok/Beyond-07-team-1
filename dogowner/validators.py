from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


def username_validator(username):
    if User.objects.filter(username=username).exists():
        raise ValidationError("Invalid username")
