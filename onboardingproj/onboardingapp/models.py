from django.db import models

# Create your models here.
class ACCIDENT (models.Model):
    ACCIDENT_NO = models.CharField(max_length=20)
    ACCIDENT_DATE = models.DateTimeField()
    DAY_WEEK_DESC = models.CharField(max_length = 10)
    NODE_ID = models.CharField(max_length=10)
    SEVERITY = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.ACCIDENT_NO} - {self.ACCIDENT_DATE.strftime('%Y-%m-%d')} - Severity: {self.SEVERITY}"

class NODE (models.Model):
    ACCIDENT_NO = models.CharField(max_length=20)
    LGA_NAME = models.CharField(max_length = 20)
    LATITUDE = models.DecimalField(max_digits=22, decimal_places=16)
    LONGITUDE = models.DecimalField(max_digits=22, decimal_places=16)
    POSTCODE_CRASH = models.CharField(max_length=5)

    def __str__(self) -> str:
        return super().__str__()