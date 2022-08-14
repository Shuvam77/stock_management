from django.urls import path
from . import views

app_name = "stock"

urlpatterns = [
    path("", views.home, name="home"),
    path("list_items/", views.ListItem.as_view(), name="list_items"),
    path("add_item/", views.AddItem.as_view(), name="add_item"),
    path("update_item/<int:pk>", views.UpdateItem.as_view(), name="update_item"),
    path("list_items/delete_item/<int:pk>/", views.DeleteItem.as_view(), name="delete_item"),
    path('search/', views.SearchItems.as_view(), name='search_result'),

    path("list_category/", views.ListCategory.as_view(), name="list_category"),
    path("create_category/", views.CreateCategory.as_view(), name="create_category"),
    path("update_category/<int:pk>", views.UpdateCategory.as_view(), name="update_category"),
    path("delete_category/<int:pk>", views.DeleteCategory.as_view(), name="delete_category"),



]
