from django.contrib import admin
from .models import Stock
from .forms import StockForm

# Register your models here.

class StockFormAdmin(admin.ModelAdmin):
    list_display = ['category', 'item_name', 'quantity']
    form = StockForm
    list_filter = ['category']
    search_fields = ['category', 'item_name'] 

admin.site.register(Stock, StockFormAdmin)

