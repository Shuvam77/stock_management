from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from stock.forms import CategoryForm, DepartmentForm, StockForm, StockSearchForm
from django.db.models import Q
from bootstrap_modal_forms.generic import BSModalCreateView, BSModalUpdateView, BSModalDeleteView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.template.loader import render_to_string



from django.http import HttpResponse, JsonResponse
import csv

from stock.models import Category, Department, Stock
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


class AddItem(SuccessMessageMixin, CreateView):
    form_class = StockForm
    model = Stock
    template_name = 'add_item.html'
    success_message = 'Success: Item was added.'
    success_url= reverse_lazy('stock:list_items')

    def form_valid(self, form):
        form.instance.received_by = self.request.user
        return super().form_valid(form)


class UpdateItem(SuccessMessageMixin, UpdateView):
    form_class = StockForm
    model= Stock
    template_name = 'update_item.html'
    success_message = 'Success: Item was updated.'
    success_url= reverse_lazy('stock:list_items')


class DeleteItem(SuccessMessageMixin, DeleteView):
    model= Stock
    template_name= 'stock_delete_confirm.html'
    success_message = 'Success: Item was deleted.'
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
    success_message = 'Success: Category was created.'
    success_url= reverse_lazy('stock:list_category')


class UpdateCategory(BSModalUpdateView):
    form_class = CategoryForm
    model = Category
    template_name = 'update_category.html'
    success_message = 'Success: Category was updated.'
    success_url= reverse_lazy('stock:list_category')

class DeleteCategory(BSModalDeleteView):
    model = Category
    template_name = 'delete_category.html'
    success_message = 'Success: Category was deleted.'
    success_url= reverse_lazy('stock:list_category')


class ListDepartment(ListView):
    model = Department
    paginate_by= 10
    context_object_name = 'departments'
    template_name = 'list_departments.html'

# class CreateDepartment(CreateView):
#     form_class = DepartmentForm
#     model = Department
#     template_name = 'add_department.html'
#     success_message = 'Success: Department was created.'
#     success_url= reverse_lazy('stock:list_departments')


def createDepartment(request):

    if request.POST.get('action') == 'post':
        name = request.POST.get('name')
        Department.objects.create(
            name = name
        )
        messages.add_message(request, messages.SUCCESS, 'Success: Department Added.')
        
        response = response = {'status': 200, 'message': ("Success: Department Added")} 
        return JsonResponse(response)
    return render(request, 'add_department.html')


