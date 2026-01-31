from django.db import models
import uuid

class Category(models.Model):
    name = models.CharField(max_length=255)
    uuid = models.UUIDField(unique=True, default=uuid.uuid4)
    create_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

# Create your models here.
class Product(models.Model):
    STATUS_ENABLED ="enabled"
    STATUS_DISABLED='disabled'
    STATUS_DELETED = 'deleted'
    STATUS_CHOICES=((STATUS_ENABLED, "Enabled"), 
                    (STATUS_DISABLED, "Disabled"),
                    (STATUS_DELETED, "Deleted"),
                  )

    # Static attributes
    name = models.CharField(max_length=255)
    uuid = models.UUIDField(unique=True, default=uuid.uuid4)
    create_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    delete_date = models.DateTimeField(default=None, null=True, blank=True)
    price= models.IntegerField(default=0)
    discount = models.FloatField(default=0)
    enabled = models.BooleanField(default=True)
    status = models.CharField(max_length=10,  choices=STATUS_CHOICES, default= STATUS_ENABLED)
    description = models.TextField(default=None)
    slug = models.SlugField(default=None)
    category = models.ForeignKey('Category', on_delete=models.PROTECT)