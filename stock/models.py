from django.db import models
from django.urls import reverse

from Department.models import Department

# Create your models here.

class Category(models.Model):
    name= models.CharField(max_length=50, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)

    class Meta:
        ordering = ("-created_at",)
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")

    def __str__(self):
        return self.name

class Stock(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_name')
    item_name = models.CharField(max_length=50, blank=True, null=True)
    quantity = models.IntegerField(default=0, blank=True, null=True)
    price = models.DecimalField(default=0.00, max_digits=6, decimal_places=2, blank=True, null=True)
    received_by = models.CharField(max_length=50, blank=True, null=True)
    reorder_level = models.IntegerField(default=0, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)

    class Meta:
        ordering = ("-created_at",)
        verbose_name = ("Stock")
        verbose_name_plural = ("Stocks")

    def __str__(self):
        return self.item_name

    def get_absolute_url(self):
        return reverse('stock:list_items')

    def get_total_amount(self):
        return self.quantity * self.price



class Issue(models.Model):
    issued_by =  models.CharField(max_length=50, blank=True, null=True)
    issued_to = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='department_name')
    issued_item = models.ForeignKey(Stock, on_delete=models.CASCADE, related_name='issued_item_name')
    issued_quantity = models.IntegerField(default=0, blank=True, null=True)
    issued_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)
    last_updated_by =  models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        ordering = ("-issued_at",)
        verbose_name = ("Issue")
        verbose_name_plural = ("Issues")

    def __str__(self):
        return self.issued_to


