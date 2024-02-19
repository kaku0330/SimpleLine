from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(db_column="username",unique=True,null=True,max_length=255)
    password = models.CharField(db_column="password",max_length=255)

    class Meta:
        db_table = "user"
