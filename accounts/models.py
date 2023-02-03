# lines 2- 10 added in template
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    email = models.EmailField()
    # add additional fields in here

    def __str__(self):
        return self.username
