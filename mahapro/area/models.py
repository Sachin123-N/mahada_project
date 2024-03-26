from django.db import models


class Maha(models.Model):
    PAYMENT_MODE = [("OC", "ON Cash"), ("EMI ", " Monthly Finance")]
    plot_name = models.CharField(max_length=20)
    plot_area = models.IntegerField()
    plot_price = models.IntegerField()
    payment_mode = models.CharField(max_length=10, choices=PAYMENT_MODE)
