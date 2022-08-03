from django.urls import path
from . import views

app_name = "stock"

urlpatterns = [
    path("", views.home, name="home"),
    path("list_items/", views.ListItem.as_view(), name="list_items"),
    path("add_item/", views.AddItem.as_view(), name="add_item"),
    path("update_item/<int:pk>", views.UpdateItem.as_view(), name="update_item"),
    path("delete_item/<int:pk>", views.DeleteItem.as_view(), name="delete_item"),
    path('search/', views.SearchItems.as_view(), name='search_result'),


]
