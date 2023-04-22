from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import RegisterUser, LoginUser

urlpatterns = [
   path('register/',RegisterUser.as_view(),name='register'),
   path('login/',LoginUser.as_view(),name='login'),
    #path('token/',,name='token'),
]