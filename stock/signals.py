from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.forms import ValidationError
from stock.models import DepartmentItem, Issue, Stock
from django.db import transaction

@transaction.atomic
@receiver(pre_save, sender=Issue)
def validate_issue_number(sender, instance, **kwargs):
    if instance.issued_quantity > instance.issued_item.quantity:
        raise ValidationError("Issue is greater than available quantity.")
        

    with transaction.atomic():
        @receiver(post_save, sender=Issue)
        def del_quantity_stock(sender, created, instance, **kwargs):
            if created:
                item = Stock.objects.get(id=instance.issued_item.id)
                item.quantity -= instance.issued_quantity
                item.save()

    with transaction.atomic():       
        @receiver(post_save, sender=Issue)
        def add_departmentItem(sender, created, instance, **kwargs):
            if created:
                #Need to change this to get or create!
                add = DepartmentItem.objects.create(
                    dep_id = instance.issued_to,
                    item_id = instance.issued_item,
                    quantity = instance.issued_quantity,
                )
                add.save()
