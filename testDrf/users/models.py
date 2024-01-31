from django.db import models

# Create your models here.

class user(models.Model):
    user = models.CharField(db_column="user",unique=True,max_length=255)
    password = models.CharField(db_column="password",unique=True,max_length=255)

    class Meta:
        db_table = "user"