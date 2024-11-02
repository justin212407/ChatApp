from django.db import models

class User(models.Model):
    email = models.EmailField(unique=True)  # Unique and required email field
    password = models.CharField(max_length=255)
    ...

# Create your models here.
