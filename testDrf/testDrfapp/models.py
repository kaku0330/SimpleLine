from django.db import models

# Create your models here.
class testDrf(models.Model):
    test_id = models.CharField(db_column="test_id",unique= True,max_length=128)
    test_name = models.CharField(db_column='test_name',unique= False,max_length=10)
    
    class Meta:
        db_table = "testDrf"