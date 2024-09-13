from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

#class UserProfile(models.Model):
#    user = models.OneToOneField(
#        'auth.User',
#        primery_key=True,
#        on_delete=models.CASCADE
#    )

class BlogUser(AbstractUser):
   # USERNAME_FIELD = 'email'
  #  email = models.EmailField('email address', unique=True)
    bio =models.TextField(blank=True)