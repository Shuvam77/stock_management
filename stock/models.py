from django.db import models
from django.urls import reverse

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
        return f"{self.name}"


class Stock(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_name')
    item_name = models.CharField(max_length=50, blank=True, null=True)
    quantity = models.PositiveIntegerField(default=0, blank=True, null=True)
    price = models.DecimalField(default=0.00, max_digits=6, decimal_places=2, blank=True, null=True)
    received_by = models.CharField(max_length=50, blank=True, null=True)
    reorder_level = models.PositiveIntegerField(default=0, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)

    class Meta:
        ordering = ("-created_at",)
        verbose_name = ("Stock")
        verbose_name_plural = ("Stocks")

    def __str__(self):
        return f"{self.item_name}"

    def get_absolute_url(self):
        return reverse('stock:list_items')

    def get_total_amount(self):
        return self.quantity * self.price

    def reorder_status(self):
        if self.quantity >= self.reorder_level:
            return True
        else:
            return False


class Department(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        ordering = ("name",)
        verbose_name = ("Department")
        verbose_name_plural = ("Departments")

    def __str__(self):
        return f"{self.name}"


class DepartmentItem(models.Model):
    dep_id = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='dep_name')
    item_id = models.ForeignKey(Stock, on_delete=models.CASCADE, related_name='dep_item_name')
    quantity = models.PositiveIntegerField(default=0, blank=True, null=True)
    last_updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)

    class Meta:
        ordering = ("-last_updated_at",)
        verbose_name = ("DepartmentItem")
        verbose_name_plural = ("DepartmentItems")

    def __str__(self):
        return f"{self.item_id.item_name}"


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
    dep_id = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='ord_dep_name')
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='ord_cat_name')
    order_item = models.ForeignKey(Stock, on_delete=models.CASCADE, related_name='ord_item_name')
    quantity = models.PositiveIntegerField(default=0, blank=True, null=True)
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
        return f"T: {self.quantity} {self.order_item } ordered by {self.dep_id.name}"


class Issue(models.Model):
    issued_by =  models.CharField(max_length=50, blank=True, null=True)    
    issued_item = models.ForeignKey(Stock, on_delete=models.CASCADE, related_name='issued_item_name')
    issued_to = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='department_name')
    order_ticket_id = models.ForeignKey(OrderTicket, on_delete=models.CASCADE, related_name='ord_issue', blank=True, null=True)
    issued_quantity = models.PositiveIntegerField(default=0, blank=True, null=True)
    issued_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)
    last_updated_by =  models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        ordering = ("-issued_at",)
        verbose_name = ("Issue")
        verbose_name_plural = ("Issues")

    def __str__(self):
        return f"{self.issued_to.name}"

