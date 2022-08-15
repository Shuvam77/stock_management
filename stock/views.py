from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from stock.forms import CategoryForm, StockForm, StockSearchForm
from django.db.models import Q
from bootstrap_modal_forms.generic import BSModalCreateView, BSModalUpdateView, BSModalDeleteView

from django.http import HttpResponse
import csv

from stock.models import Category, Stock
# Create your views here.


def home(request):
    something = "Page working!"
    return render(request, "home.html", {"something": something})


class ListItem(ListView):
    model = Stock
    paginate_by= 10
    context_object_name = 'stock_list'
    template_name = 'list_items.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "List of Stock Items"
        context['tag'] = 'list'
        return context


class AddItem(CreateView):
    form_class = StockForm
    model = Stock
    template_name = 'add_item.html'
    success_url= reverse_lazy('stock:list_items')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class UpdateItem(UpdateView):
    form_class = StockForm
    model= Stock
    template_name = 'update_item.html'
    success_url= reverse_lazy('stock:list_items')


class DeleteItem(DeleteView):
    model= Stock
    template_name= 'stock_delete_confirm.html'
    success_url= reverse_lazy('stock:list_items')


class SearchItems(ListView):
    form_class = StockSearchForm
    model = Stock
    template_name = 'list_items.html'
    context_object_name = 'stock_list'

    def get_queryset(self):
        query1 = self.request.GET.get('category')
        query2 = self.request.GET.get('item_name')

        queryset = Stock.objects.filter(
            Q(category__name__icontains=query1), Q(item_name__icontains = query2)
        )
        return queryset


def ExportCSV(request):
    response = HttpResponse(content_type = 'text/csv')
    response['Content-Disposition'] = 'attachment; filename="List_of_stock.csv"'
    writer = csv.writer(response)
    writer.writerow(['CATEGORY', 'ITEM NAME', 'QUANTITY'])
    instance = Stock.objects.all()
    for stock in instance:
        writer.writerow([stock.category, stock.item_name, stock.quantity])
    return response


class ListCategory(ListView):
    model = Category
    paginate_by= 10
    context_object_name = 'categories'
    template_name = 'list_categories.html'


class CreateCategory(BSModalCreateView):
    form_class = CategoryForm
    model = Category
    template_name = 'create_category.html'
    success_message = 'Success: Book was created.'
    success_url= reverse_lazy('stock:list_category')


class UpdateCategory(BSModalUpdateView):
    form_class = CategoryForm
    model = Category
    template_name = 'update_category.html'
    success_message = 'Success: Book was updated.'
    success_url= reverse_lazy('stock:list_category')

class DeleteCategory(BSModalDeleteView):
    model = Category
    template_name = 'delete_category.html'
    success_message = 'Success: Book was deleted.'
    success_url= reverse_lazy('stock:list_category')


