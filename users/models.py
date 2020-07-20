import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    # customizing fields
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    email = models.EmailField(verbose_name='email', max_length=256, unique=True)

    USERNAME_FIELD = 'email'  # now user can log in using email
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name'] # here, email is already a required field

    def __str__(self):
        return self.username