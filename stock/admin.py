from django.contrib import admin
from .models import *
from .forms import StockForm

# Register your models here.

class StockFormAdmin(admin.ModelAdmin):
    list_display = ['category', 'item_name', 'quantity', 'received_by']
    # form = StockForm
    list_filter = ['category']
    search_fields = ['category', 'item_name'] 

admin.site.register(Stock, StockFormAdmin)
admin.site.register(Category)
admin.site.register(Department)
admin.site.register(DepartmentItem)
admin.site.register(OrderTicket)
admin.site.register(Issue)



