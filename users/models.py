from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):

    """ Custom User Model """

    # GENDER CHOICES
    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )

    # LANGUAGE CHOICES
    LANGUAGE_ENGLISH = "english"
    LANGUAGE_KOREAN = "korean"
    LANGUAGE_JAPANESE = "japanese"
    LANGUAGE_CHINESE = "chinese"

    LANGUAGE_CHOICES = (
        (LANGUAGE_ENGLISH, "ENG"),
        (LANGUAGE_KOREAN, "KOR"),
        (LANGUAGE_JAPANESE, "JPN"),
        (LANGUAGE_CHINESE, "CHN"),
    )

    avatar = models.ImageField(null=True, blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, null=True, blank=True)
    bio = models.TextField(default="", blank=True)
    birthday = models.DateField(null=True)
    languages = models.CharField(choices=LANGUAGE_CHOICES, max_length=20, null=True)
    business_member = models.BooleanField(default=False)