from django.db import models

# Create your models here.
class ACCIDENT (models.Model):
    ACCIDENT_NO = models.CharField(max_length=20)
    ACCIDENT_DATE = models.DateTimeField()
    DAY_WEEK_DESC = models.CharField(max_length = 10)
    NODE_ID = models.CharField(max_length=10)
    SEVERITY = models.IntegerField()