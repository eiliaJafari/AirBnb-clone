from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    """
    Custom User Model
    """

    GENDER_MALE = "Male"
    GENDER_FEMALE = "Female"
    GENDER_OTHER = "Other"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )

    LANGUAGE_ENGLISH = "English"
    LANGUAGE_Farsi = "Farsi"

    LANGUAGE_CHOICES = (
        (LANGUAGE_ENGLISH, "English"),
        (LANGUAGE_Farsi, "Farsi"),
    )

    avatar = models.ImageField(blank=True, upload_to="avatars")
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, blank=True)
    bio = models.TextField(default="", blank=True)
    birthdate = models.DateField(blank=True, null=True)
    language = models.CharField(
        choices=LANGUAGE_CHOICES, max_length=10, blank=True, default=LANGUAGE_Farsi
    )
    superhost = models.BooleanField(default=False)
