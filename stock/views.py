from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from stock.forms import StockForm, StockSearchForm
from django.db.models import Q

from stock.models import Stock
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

    # def post(self, request, *args, **kwargs):
    #     if request.method == 'POST':
    #         Stock.objects.filter(pk=1).delete()
    #     return redirect('stock:list_items')


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
            Q(category__icontains=query1), Q(item_name__icontains = query2)
        )
        return queryset



