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
