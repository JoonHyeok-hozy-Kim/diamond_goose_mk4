import os

import time
from pywinauto import application
import win32com.client
from django.db import models
import yfinance as yf

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
    class Creon:
        def __init__(self):
            self.obj_CpUtil_CpCybos = win32com.client.Dispatch('CpUtil.CpCybos')

        def kill_client(self):
            os.system('taskkill /IM coStarter* /F /T')
            os.system('taskkill /IM CpStart* /F /T')
            os.system('taskkill /IM DibServer* /F /T')
            os.system('wmic process where "name like \'%coStarter%\'" call terminate')
            os.system('wmic process where "name like \'%CpStart%\'" call terminate')
            os.system('wmic process where "name like \'%DibServer%\'" call terminate')

        def connect(self, id_, pwd, pwdcert):
            if not self.connected():
                self.disconnect()
                self.kill_client()
                app = application.Application()
                app.start(
                    'C:\CREON\STARTER\coStarter.exe /prj:cp /id:{id} /pwd:{pwd} /pwdcert:{pwdcert} /autostart'.format(
                        id=id_, pwd=pwd, pwdcert=pwdcert
                    )
                )
            while not self.connected():
                time.sleep(1)
            return True

        def connected(self):
            b_connected = self.obj_CpUtil_CpCybos.IsConnect
            if b_connected == 0:
                return False
            return True

        def disconnect(self):
            if self.connected():
                self.obj_CpUtil_CpCybos.PlusDisconnect()


    ticker = models.CharField(max_length=100, null=False)
    market = models.CharField(max_length=20, choices=MARKET_CHOICES, null=False)
    name = models.CharField(max_length=200, null=False)
    currency = models.CharField(max_length=20, choices=CURRENCY_CHOICES, null=False)
    image = models.ImageField(upload_to='equitymaster/', null=False)

    current_price = models.FloatField(default=0, null=False)

    @property
    def current_price(self):

        yfinance_markets = [
                            'NASDAQ',
                            'NYSE',
                            ]
        creon_markets = ['KSE']

        if self.market in yfinance_markets:
            data = yf.Ticker(self.ticker)
            today_data = data.history(period='1d')
            return round((today_data['Close'][0]), 2)

        elif self.market in creon_markets:
            creon = self.Creon()
            creon.connect('hozy6!','hubris6!','hubris1156$')
            print(creon.connected())

            return 0



        return -1



