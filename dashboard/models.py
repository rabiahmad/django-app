from datetime import datetime, date, timedelta
from django.conf import settings
from django.db import models
from django.utils import timezone
import uuid


class Transaction(models.Model):
    row_id = models.IntegerField(primary_key=True, default=None)
    order_id = models.CharField(max_length=200)
    order_date = models.DateField()
    ship_date = models.DateField()
    ship_mode = models.CharField(max_length=255)
    customer_id = models.CharField(max_length=255)
    customer_name = models.CharField(max_length=255)
    segment = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    postal_code = models.CharField(default=None, blank=True, null=True, max_length=255)
    region = models.CharField(max_length=255)
    product_id = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    sub_category = models.CharField(max_length=255)
    product_name = models.CharField(max_length=255)
    sales = models.FloatField()

    class Meta:
        ordering = ("row_id",)

    def __str__(self) -> str:
        return f"{self.row_id}_{self.order_id}"
