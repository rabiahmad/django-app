from datetime import datetime, date, timedelta
from django.conf import settings
from django.db import models
from django.utils import timezone
import uuid

class Promotion(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    promotion_type = models.CharField(max_length=50, default='Price reduction')
    start_date = models.DateField()
    end_date = models.DateField()
    discount = models.FloatField(default=0)

    def submit(self):
        self.submission_date = timezone.now()
        self.save()

    def __str__(self) -> str:
        return str(self.id)


class Transaction(models.Model):
    row_id = models.IntegerField(default=None, blank=True, null=True)
    order_id = models.CharField(primary_key=True, max_length=200)
    order_date = models.DateField()
    ship_date = models.DateField()
    ship_mode = models.CharField(max_length=50)
    customer_id = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=100)
    segment = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    postal_code = models.CharField(default=None, blank=True, null=True, max_length=10)
    region = models.CharField(max_length=50)
    product_id = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    sub_category = models.CharField(max_length=50)
    product_name = models.CharField(max_length=200)
    sales = models.FloatField()

    def __str__(self) -> str:
        return str(self.order_id)
