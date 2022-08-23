from django.urls import path
from . import views

app_name = "stock"

urlpatterns = [
    path("", views.home, name="home"),


    path("list_items/", views.ListItem.as_view(), name="list_items"),
    path("add_item/", views.AddItem.as_view(), name="add_item"),
    path("update_item/<int:pk>/", views.UpdateItem.as_view(), name="update_item"),
    path("list_items/delete_item/<int:pk>/", views.DeleteItem.as_view(), name="delete_item"),
    path("item_detail/<int:pk>/", views.DetailItem.as_view(), name="item_detail"),


    path('search/', views.SearchItems.as_view(), name='search_result'),
    path("export_csv/", views.ExportCSV, name="export_csv"),


    path("list_category/", views.ListCategory.as_view(), name="list_category"),
    path("create_category/", views.CreateCategory.as_view(), name="create_category"),
    path("update_category/<int:pk>/", views.UpdateCategory.as_view(), name="update_category"),
    path("delete_category/<int:pk>/", views.DeleteCategory.as_view(), name="delete_category"),


    path("list_departments/", views.ListDepartment.as_view(), name="list_departments"),
    path("add_department/", views.CreateDepartment.as_view(), name="add_department"),
    path("update_department/<int:pk>/", views.UpdateDepartment.as_view(), name="update_department"),
    path("delete_department/<int:pk>/", views.DeleteDepartment.as_view(), name="delete_department"),


    path("issue_item/", views.IssueItem.as_view(), name="issue_item"),
    path("issue_list/", views.IssueList.as_view(), name="issue_list"),


    path("department_item_list/", views.DepartmentItemList.as_view(), name="dep_item_list"),


    path("issue_ticket/", views.IssueTicket.as_view(), name="issue_ticket")


]
