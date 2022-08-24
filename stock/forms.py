from django import forms
from .models import Category, Department, Stock, Issue, OrderTicket
from bootstrap_modal_forms.forms import BSModalModelForm

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
    price = forms.DecimalField(max_digits=6, decimal_places=2, widget=forms.NumberInput(attrs={'placeholder':'Price'}), required=True)
    reorder_level = forms.IntegerField(max_value=100, widget=forms.NumberInput(attrs={'placeholder':'Re-Order Level'}), required=True)


    class Meta:
        model = Stock
        fields = ['category', 'item_name', 'quantity', 'price', 'reorder_level']

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


class CategoryForm(BSModalModelForm):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder':'Name'}), required=True)

    class Meta:
        model = Category
        fields = ['name']


class DepartmentForm(BSModalModelForm):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder':'Name'}), required=True)

    class Meta:
        model = Department
        fields = ['name']


class IssueItems(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ['issued_item', 'issued_to', 'order_ticket_id', 'issued_quantity']


class IssueTickets(forms.ModelForm):

    class Meta:
        model = OrderTicket
        fields = ['category_id', 'dep_id', 'order_item', 'quantity', 'remarks']


class EditTicketStatus(forms.ModelForm):

    class Meta:
        model = OrderTicket
        fields = ['dep_id', 'order_item', 'quantity', 'remarks', 'status']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["dep_id"].disabled = True
        # self.fields["dep_id"].widget.attrs["readonly"] = True
        self.fields["order_item"].disabled = True
        self.fields["quantity"].disabled = True
        self.fields["remarks"].disabled = True