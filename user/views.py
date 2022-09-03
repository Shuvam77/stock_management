from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin


from .form import CustomUserChangeForm, CustomUserCreationForm

# Create your views here.

class SignupPageView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class UserChangePageView(PermissionRequiredMixin, UpdateView):
    form_class = CustomUserChangeForm
    model = get_user_model()
    permission_required = 'user.change_user'
    success_url = reverse_lazy('user:user_list')
    template_name = 'registration/user_update.html'

class UserList(LoginRequiredMixin, ListView):
    model = get_user_model()
    paginate_by= 10
    context_object_name = 'employees'
    template_name = 'department/employees_list.html'
    success_url= reverse_lazy('user:user_list')

