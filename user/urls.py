from django.urls import path
from .views import SignupPageView, UserChangePageView, UserList


app_name = "user"


urlpatterns = [
    path('signup/', SignupPageView.as_view(), name='signup'),
    path('updateUser/<int:pk>', UserChangePageView.as_view(), name='user_update'),
    path('user_list/', UserList.as_view(), name="user_list")

]