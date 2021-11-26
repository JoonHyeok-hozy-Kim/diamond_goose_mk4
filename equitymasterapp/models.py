from django.db import models

# Create your models here.


class Equity(models.Model):
    ticker = models.CharField(max_length=100, null=False)
    market = models.CharField(max_length=20, null=False)
    name = models.CharField(max_length=200, null=False)
    currency = models.CharField(max_length=20, null=False)
    image = models.ImageField(upload_to='equitymaster/', null=False)