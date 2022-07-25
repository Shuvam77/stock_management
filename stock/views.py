from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from stock.forms import StockForm

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
        return context


class AddItem(CreateView):
    form_class = StockForm
    model = Stock
    template_name = 'add_item.html'
    success_url= reverse_lazy('stock:list_items')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)



