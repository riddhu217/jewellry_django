from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager, User
from .managers import CustomUserManager


class CustomUser(AbstractUser):
    MALE = 'male'
    FEMALE = 'female'

    GENDER_CHOICES = (
        (MALE, 'male'),
        (FEMALE, 'female'),
    )
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30, null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, null=True, blank=True)
    Address = models.TextField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=30, null=True, blank=True)
    state = models.CharField(max_length=30, null=True, blank=True)
    contact_number = models.CharField(max_length=20, null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def has_module_perms(self, app_label):
        return True


