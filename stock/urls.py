from django.urls import path
from . import views

app_name = "stock"

urlpatterns = [
    path("", views.home, name="home"),
    path("list_items", views.ListItem.as_view(), name="list_items"),
    path("add_item", views.AddItem.as_view(), name="add_item"),

]
