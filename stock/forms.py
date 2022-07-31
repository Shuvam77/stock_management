from django import forms
from .models import Stock

Category = (
    ('', 'Choose...'),
    ('CHOCO', 'Chocolate'),
    ('BEER', 'Beer'),
    ('WHI', 'Whisky'),
    ('CHIPS', 'Chips')

)

class StockForm(forms.ModelForm):

    category = forms.ChoiceField(choices=Category)
    item_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder':'Name'}))
    quantity = forms.IntegerField(max_value=50, widget=forms.NumberInput(attrs={'placeholder':'Quantity'}))

    class Meta:
        model = Stock
        fields = ['category', 'item_name', 'quantity']