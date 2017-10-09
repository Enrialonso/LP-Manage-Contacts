from django.db import models

# Create your models here.

class db_usuarios (models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=False)
    last = models.CharField(max_length=50, null=False)
    email = models.EmailField(max_length=254, unique=True, null=False)
    password = models.CharField(max_length=200, null=False)

class db_manage_contacts (models.Model):

    id = models.AutoField(primary_key=True)
    associated_user = models.CharField(max_length=254, null=True)
    name = models.CharField(max_length=50, null=True)
    last = models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=254, null=True)
    phone_local = models.CharField(max_length=20, null=True)
    phone_mov = models.CharField(max_length=20, null=True)
    street = models.CharField(max_length=150, null=True)
    street_number = models.CharField(max_length=150, null=True)
    population = models.CharField(max_length=30, null=True)
    state = models.CharField(max_length=150, null=True)
    postalcode = models.CharField(max_length=12, null=True)
    country = models.CharField(max_length=20, null=True)
    url_web = models.URLField(max_length=1024, null=True)
