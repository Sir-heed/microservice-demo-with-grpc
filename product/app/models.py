from django.db import models
from core.models import AuditableModel

# Create your models here.
class Product(AuditableModel):
    product_id = models.UUIDField(null=True)
    title = models.CharField(max_length=200)
    image = models.CharField(max_length=200, null=True, blank=True)


class ProductUser(AuditableModel):
    user_id = models.UUIDField()
    product_id = models.UUIDField()

    class Meta:
        unique_together = ['user_id', 'product_id']