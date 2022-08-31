from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.forms import ValidationError
from stock.models import DepartmentItem, Issue, OrderTicket, Stock

@receiver(pre_save, sender=Issue)
def validate_issue_number(sender, instance, **kwargs):
    if instance.issued_quantity > instance.issued_item.quantity:
        raise ValidationError("Issue is greater than available quantity.")
        
    
@receiver(post_save, sender=Issue)
def del_quantity_stock(sender, created, instance, **kwargs):
    if created:
        item = Stock.objects.get(id=instance.issued_item.id)
        item.quantity = item.quantity - instance.issued_quantity
        item.save()

@receiver(post_save, sender=Issue)
def add_departmentItem(sender, created, instance, **kwargs):
    if created:
                    
        search = DepartmentItem.objects.filter(dep_id = instance.issued_to.id, item_id=instance.issued_item.id)
        if search.exists():
            item = DepartmentItem.objects.get(dep_id=instance.issued_to.id, item_id=instance.issued_item.id)
            item.quantity = item.quantity + instance.issued_quantity
            item.save()
        else:
            add = DepartmentItem.objects.create(
                dep_id = instance.issued_to,
                item_id = instance.issued_item,
                quantity = instance.issued_quantity,
                )
            add.save()

@receiver(post_save, sender=Issue)
def ticket_status_chg(sender, created, instance, **kwargs):
    if created:
        if not instance.order_ticket_id:
            pass
        else:
            search_ticket = OrderTicket.objects.get(id=instance.order_ticket_id.id, quantity = instance.issued_quantity, order_item = instance.issued_item.id)
            search_ticket.status = "AP"
            search_ticket.save()
