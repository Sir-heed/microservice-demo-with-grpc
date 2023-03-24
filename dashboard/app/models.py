from django.db import models
from core.models import AuditableModel

class Product(AuditableModel):
    title = models.CharField(max_length=200)
    image = models.CharField(max_length=200, null=True)
    likes = models.PositiveBigIntegerField(default=0)


class User(AuditableModel):
    pass