from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
from django.db import models
from django.urls import reverse
from django.utils.timezone import now


class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', null=True, blank=True)
    groups = models.ManyToManyField('auth.Group', related_name='users_user_groups')
    user_permissions = models.ManyToManyField('auth.Permission', related_name='users_user_permissions')


