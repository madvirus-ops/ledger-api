from django.db import models

# Create your models here.
from apps.common.models import TimedUUIDModel



class RecordsModel(TimedUUIDModel):
    product_name = models.CharField(max_length=30)
    product_description = models.TextField()
    price = models.DecimalField(decimal_places=6,max_digits=56)