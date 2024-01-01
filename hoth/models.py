from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    email = models.EmailField(unique=True,null=True,max_length=150)
    username = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gov_id = models.CharField(max_length=50)
    address = models.CharField(max_length=250)
    pob = models.CharField(max_length=50)
    dob = models.DateField(null=True, blank=False, default='1900-01-01')
    phone = models.FloatField(null=True, blank=False, default=0)
    # medical = models.CharField(max_length=50)
    # medical_date = models.DateField()
    USERNAME_FIELD  =   'email'
    REQUIRED_FIELDS =   ['username']

    def __str__(self):
        return self.email

# class Aircraft(models.Models):
#     oaci_id = models.CharField(max_length=4)
#     oaci_description = models.CharField(max_length=250)
#     type = 