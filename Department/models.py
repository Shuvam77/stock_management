from django.db import models
from stock.models import Stock, Issue, Category

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        ordering = ("name",)
        verbose_name = ("Department")
        verbose_name_plural = ("Departments")

    def __str__(self):
        return self.name


class DepartmentItem(models.Model):
    item_id = models.ForeignKey(Stock, on_delete=models.PROTECT, related_name='dep_item_name')
    dep_id = models.ForeignKey(Department, on_delete=models.PROTECT, related_name='dep_name')
    quantity = models.IntegerField(default=0, blank=True, null=True)
    last_updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)

    class Meta:
        ordering = ("-last_updated_at",)
        verbose_name = ("DepartmentItem")
        verbose_name_plural = ("DepartmentItems")

    def __str__(self):
        return self.item_id


class OrderTicket(models.Model):

    PENDING = 'PE'
    APPROVED = 'AP'
    PROCESSING = 'PR'
    REJECTED = 'RE'
    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (APPROVED, 'Approved'),
        (PROCESSING, 'Processing'),
        (REJECTED, 'Rejected'),
    ]

    category_id = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='ord_cat_name')
    order_item = models.ForeignKey(Stock, on_delete=models.PROTECT, related_name='ord_item_name')
    dep_id = models.ForeignKey(Department, on_delete=models.PROTECT, related_name='ord_dep_name')
    quantity = models.IntegerField(default=0, blank=True, null=True)
    issued_by = models.CharField(max_length=50, blank=True, null=True)
    fulfilled_by = models.CharField(max_length=50, blank=True, null=True)
    remarks = models.TextField(max_length=255, blank=False)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default=PENDING )
    last_updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)



    class Meta:
        ordering = ("-created_at",)
        verbose_name = ("OrderTicket")
        verbose_name_plural = ("OrderTickets")

    def __str__(self):
        return self.order_item