from django import forms
from .models import Category, Stock

# Category = (
#     ('', 'Choose...'),
#     ('CHOCO', 'Chocolate'),
#     ('BEER', 'Beer'),
#     ('WHI', 'Whisky'),
#     ('CHIPS', 'Chips')

# )

class StockForm(forms.ModelForm):

    category = forms.ModelChoiceField(required=True, queryset= Category.objects.all())
    item_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder':'Name'}), required=True)
    quantity = forms.IntegerField(max_value=50, widget=forms.NumberInput(attrs={'placeholder':'Quantity'}), required=True)

    class Meta:
        model = Stock
        fields = ['category', 'item_name', 'quantity']

    # Important in (forms.Form)
    def clean(self):
        cleaned_data = super(StockForm, self).clean()
        category = cleaned_data.get('category')
        item_name = cleaned_data.get('item_name')
        quantity = cleaned_data.get('quantity')
        if not category:
            raise forms.ValidationError('This field is required')
        elif not item_name:
            raise forms.ValidationError('This field is required')
        elif not quantity:
            raise forms.ValidationError('This field is required')


class StockSearchForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['category', 'item_name']


class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder':'Name'}), required=True)

    class Meta:
        model = Category
        fields = ['name']