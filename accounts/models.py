from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    profile_image = models.ImageField(upload_to="profile_images/", blank=True)
    bio = models.TextField(max_length=500, blank=True)
