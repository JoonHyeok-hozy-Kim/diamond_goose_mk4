from django.db import models

# Create your models here.

MARKET_CHOICES = (
    ('KSE', 'Korean Stock Exchange(KSE)'),
    ('NASDAQ', 'NASDAQ'),
    ('NYSE', 'NewYork Stock Exchange(NYSE)'),
)
CURRENCY_CHOICES = (
    ('KRW', 'KRW(￦)'),
    ('USD', 'USD($)'),
)

class Equity(models.Model):
    ticker = models.CharField(max_length=100, null=False)
    market = models.CharField(max_length=20, choices=MARKET_CHOICES, null=False)
    name = models.CharField(max_length=200, null=False)
    currency = models.CharField(max_length=20, choices=CURRENCY_CHOICES, null=False)
    image = models.ImageField(upload_to='equitymaster/', null=False)