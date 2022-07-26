import json
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from stock.forms import CategoryForm, DepartmentForm, StockForm, StockSearchForm, IssueItems, IssueTickets, EditTicketStatus
from django.db.models import Q
from bootstrap_modal_forms.generic import BSModalCreateView, BSModalUpdateView, BSModalDeleteView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import csv

from stock.models import Category, Department, Issue, OrderTicket, Stock, DepartmentItem
# Create your views here.


@login_required
def home(request):
    something = "Page working!"
    if request.user.is_superuser:
        order_tickets = OrderTicket.objects.all()
    else:
        order_tickets = OrderTicket.objects.filter(dep_id = request.user.role)

    context = {'items':order_tickets, 'something': something}
    return render(request, "home.html", context)


class ListItem(LoginRequiredMixin, ListView):
    model = Stock
    paginate_by= 10
    context_object_name = 'stock_list'
    template_name = 'stock/list_items.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "List of Stock Items"
        context['tag'] = 'list'
        return context


class AddItem(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = StockForm
    model = Stock
    template_name = 'stock/add_item.html'
    success_message = 'Success: Item was added.'
    success_url= reverse_lazy('stock:list_items')
    permission_required = 'Stock.add_Stock'



class UpdateItem(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    form_class = StockForm
    model= Stock
    template_name = 'stock/update_item.html'
    permission_required = 'Stock.update_Stock'
    success_message = 'Success: Item was updated.'
    success_url= reverse_lazy('stock:list_items')


class DeleteItem(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    model= Stock
    template_name= 'stock/stock_delete_confirm.html'
    permission_required = 'Stock.delete_Stock'
    success_message = 'Success: Item was deleted.'
    success_url= reverse_lazy('stock:list_items')


class DetailItem(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model= Stock
    template_name= 'stock/stock_detail.html'
    permission_required = 'Stock.view_Stock'
    context_object_name = 'item'


class SearchItems(LoginRequiredMixin, ListView):
    form_class = StockSearchForm
    model = Stock
    template_name = 'stock/list_items.html'
    context_object_name = 'stock_list'

    # def dispatch(self, request, *args, **kwargs):
    #     if not request.user.is_superuser:
    #         return HttpResponseRedirect('/')

    def get_queryset(self):
        query1 = self.request.GET.get('category')
        query2 = self.request.GET.get('item_name')

        queryset = Stock.objects.filter(
            Q(category__name__icontains=query1), Q(item_name__icontains = query2)
        )
        return queryset


@login_required
def ExportCSV(request):
    if not request.user.is_superuser:
        return HttpResponseRedirect('/')
    else:
        response = HttpResponse(content_type = 'text/csv')
        response['Content-Disposition'] = 'attachment; filename="List_of_stock.csv"'
        writer = csv.writer(response)
        writer.writerow(['CATEGORY', 'ITEM NAME', 'QUANTITY'])
        instance = Stock.objects.all()
        for stock in instance:
            writer.writerow([stock.category, stock.item_name, stock.quantity])
        return response


class ListCategory(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Category
    paginate_by= 10
    permission_required = 'Stock.view_category'
    context_object_name = 'categories'
    template_name = 'category/list_categories.html'


class CreateCategory(LoginRequiredMixin, PermissionRequiredMixin, BSModalCreateView):
    form_class = CategoryForm
    model = Category
    permission_required = 'Stock.add_category'
    template_name = 'category/create_category.html'
    success_message = 'Success: Category was created.'
    success_url= reverse_lazy('stock:list_category')


class UpdateCategory(LoginRequiredMixin, PermissionRequiredMixin, BSModalUpdateView):
    form_class = CategoryForm
    model = Category
    permission_required = 'Stock.update_category'
    template_name = 'category/update_category.html'
    success_message = 'Success: Category was updated.'
    success_url= reverse_lazy('stock:list_category')


class DeleteCategory(LoginRequiredMixin, PermissionRequiredMixin, BSModalDeleteView):
    model = Category
    template_name = 'category/delete_category.html'
    permission_required = 'Stock.delete_category'
    success_message = 'Success: Category was deleted.'
    success_url= reverse_lazy('stock:list_category')


class ListDepartment(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Department
    paginate_by= 10
    permission_required = 'Stock.view_department'
    context_object_name = 'departments'
    template_name = 'department/list_departments.html'


class CreateDepartment(LoginRequiredMixin, PermissionRequiredMixin, BSModalCreateView):
    form_class = DepartmentForm
    model = Department
    permission_required = 'Stock.add_department'
    template_name = 'department/add_department.html'
    success_message = 'Success: Department was created.'
    success_url= reverse_lazy('stock:list_departments')


# def createDepartment(request):
#     if request.POST.get('action') == 'post':
#         name = request.POST.get('name')
#         Department.objects.create(
#             name = name
#         )
#         messages.add_message(request, messages.SUCCESS, 'Success: Department Added.')
        
#         response = {'status': 200, 'message': ("Success: Department Added")} 
#         return JsonResponse(response)
#     return render(request, 'add_department.html')


class UpdateDepartment(LoginRequiredMixin, PermissionRequiredMixin, BSModalUpdateView):
    form_class = DepartmentForm
    model = Department
    permission_required = 'Stock.update_department'
    template_name = 'department/update_department.html'
    success_message = 'Success: Department was updated.'
    success_url= reverse_lazy('stock:list_departments')


class DeleteDepartment(LoginRequiredMixin, PermissionRequiredMixin, BSModalDeleteView):
    model = Department
    permission_required = 'Stock.delete_department'
    template_name = 'department/delete_department.html'
    success_message = 'Success: Department was deleted.'
    success_url= reverse_lazy('stock:list_departments')


class IssueItem(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = IssueItems
    model = Issue
    permission_required = 'Stock.add_issue'
    template_name = 'issue/issue_item.html'
    success_message = 'Success: Item was issued successfully!.'
    pk_url_kwarg = 'pk'
    success_url= reverse_lazy('stock:list_items')

    def form_valid(self, form):
        form.instance.issued_by = self.request.user
        # item = Stock.objects.get(pk = self.kwargs['pk'])
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["available_ticket"] = OrderTicket.objects.filter(Q(status = "PE") | Q(status = "PR"))
        context["department_name"] = Department.objects.all()
        context["issue_item"] = Stock.objects.filter(~Q(quantity = 0))
        context["product"] = Stock.objects.get(pk = self.kwargs['pk'])
        return context


@login_required
def get_items(request):
    data = json.loads(request.body)
    cat_id = data["id"]
    item_list = Stock.objects.filter(category = cat_id)
    return JsonResponse(list(item_list.values("id", "item_name")), safe=False)


class IssueList(LoginRequiredMixin, ListView):
    model = Issue
    paginate_by= 10
    context_object_name = 'issues'
    template_name = 'issue/issue_list.html'

    def get_queryset(self):
        if self.request.user.is_superuser:
            issue = Issue.objects.all()
            return issue
        else:
            issue = Issue.objects.filter(issued_to=self.request.user.role)
            return issue


class DepartmentItemList(LoginRequiredMixin, ListView):
    model = DepartmentItem
    paginate_by= 10
    context_object_name = 'items'
    template_name = 'departmentItem/department_items_list.html'

    def get_queryset(self):
        if self.request.user.is_superuser:
            issue = DepartmentItem.objects.all()
            return issue
        else:
            issue = DepartmentItem.objects.filter(dep_id=self.request.user.role)
            return issue


class IssueTicket(LoginRequiredMixin, CreateView):
    form_class = IssueTickets
    model = OrderTicket
    template_name = 'department/issue_ticket.html'
    success_message = 'Success: Item was ordered successfully!.'
    success_url= reverse_lazy('stock:home')


class EditTicketStatus(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = EditTicketStatus
    model = OrderTicket
    permission_required = 'Stock.change_OrderTicket'
    template_name = 'department/edit_ticket_status.html'
    success_url= reverse_lazy('stock:home')


class IssueTicketItem(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = IssueItems
    model = Issue
    permission_required = 'Stock.add_issue'
    template_name = 'issue/issue_ticket_item.html'
    success_message = 'Success: Item was issued successfully!.'
    pk_url_kwarg = 'pk'
    success_url= reverse_lazy('stock:home')


    def form_valid(self, form):
        form.instance.issued_by = self.request.user
        # item = Stock.objects.get(pk = self.kwargs['pk'])
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context["available_ticket"] = OrderTicket.objects.filter(Q(status = "PE") | Q(status = "PR"))
        # context["department_name"] = Department.objects.all()
        # context["issue_item"] = Stock.objects.filter(~Q(quantity = 0))
        context["product"] = OrderTicket.objects.get(pk = self.kwargs['pk'])
        return context



