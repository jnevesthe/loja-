from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    email=models.EmailField()
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    photo=models.ImageField(upload_to='profiles/', blank=True, null=False)

    def __str__(self):
        return self.username
# Create your models here.
