from django.db import models

# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=256)
    email_id = models.EmailField(max_length=128, unique=True)
